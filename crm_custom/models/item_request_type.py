import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ItemRequestType(models.Model):
    _name = 'item.request.type'
    _description = 'Item Category'
    _order = 'sequence, name, id'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10, index=True)
    active = fields.Boolean(default=True)
