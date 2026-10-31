import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ItemRequestLine(models.Model):
    _name = 'item.request.line'
    _description = 'Item Request Line'
    _order = 'id'

    lead_id = fields.Many2one(
        comodel_name='crm.lead',
        string='Opportunity',
        required=True,
        ondelete='cascade',
        index=True,
    )
    item_request_type = fields.Many2one(
        comodel_name='item.request.type',
        string='Product Category',
        ondelete='set null',
    )
    name = fields.Char(string='Product / Item', required=True)
    current_supplier_id = fields.Many2one(
        comodel_name='res.partner',
        string='Current Supplier (Competitor)',
        ondelete='set null',
        context={'res_partner_search_mode': 'supplier'},
    )
    quantity = fields.Float(string='Quantity', default=1.0, digits=(16, 2))
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        related='lead_id.company_currency',
        string='Currency',
        readonly=True,
    )
    price = fields.Monetary(string='Competitor Price', currency_field='currency_id')
