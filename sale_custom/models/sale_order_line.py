from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    base_uom_id = fields.Many2one(
        comodel_name='uom.uom',
        string='Base Unit',
        compute='_compute_base_uom',
        store=True,
        readonly=True,
        help="Unit of measure configured on the product.",
    )
    base_uom_qty = fields.Float(
        string='Base Unit Value',
        compute='_compute_base_uom',
        store=True,
        readonly=True,
        digits='Product Unit',
        help="Ordered quantity converted to the product's base unit.",
    )

    @api.depends('product_id', 'product_id.uom_id', 'product_uom_id', 'product_uom_qty')
    def _compute_base_uom(self):
        for line in self:
            base_uom = line.product_id.uom_id
            line.base_uom_id = base_uom
            if not base_uom or not line.product_uom_id or not line.product_uom_qty:
                line.base_uom_qty = 0.0
                continue
            line.base_uom_qty = line.product_uom_id._compute_quantity(
                line.product_uom_qty,
                base_uom,
                rounding_method='HALF-UP',
            )
