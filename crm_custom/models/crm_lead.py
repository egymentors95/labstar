import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    agent = fields.Many2one(
        comodel_name='hr.employee',
        string='Agent',
        help='Employee assigned as the agent for this lead or opportunity.',
        check_company=True,
        tracking=True,
    )
    item_request_type = fields.Many2one(
        comodel_name='item.request.type',
        string='Request Type',
        ondelete='set null',
        tracking=True,
    )
    item_request_line_ids = fields.One2many(
        comodel_name='item.request.line',
        inverse_name='lead_id',
        string='Requested Items',
    )
