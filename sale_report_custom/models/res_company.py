from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    sc_bank_logo = fields.Image(
        string='Report Bank Logo', max_width=400, max_height=200,
        help='Bank logo printed in the footer of the quotation report.')
    sc_bank_details = fields.Html(
        string='Report Bank Details', sanitize=True,
        help='Bank account details printed in the footer of the quotation report.')
