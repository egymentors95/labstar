from odoo import fields,api,models,_
from odoo.exceptions import UserError

class ApprovalAccount(models.Model):
    _inherit = 'account.move'

    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('approved', 'Approved'),
            ('posted', 'Posted'),
            ('cancel', 'Cancelled'),
        ],
        string='Status',
        required=True,
        readonly=True,
        copy=False,
        tracking=True,
        default='draft',
    )
    status_in_payment = fields.Selection(selection_add=[('approved', 'Approved'),])

    def button_draft(self):
        if any(move.state not in ('cancel', 'posted', 'approved') for move in self):
            raise UserError(_("Only posted/cancelled journal entries can be reset to draft."))
        if any(move.need_cancel_request for move in self):
            raise UserError(_("You can't reset to draft those journal entries. You need to request a cancellation instead."))

        self._check_draftable()
        # We remove all the analytics entries for this journal
        self.line_ids.analytic_line_ids.with_context(skip_analytic_sync=True).unlink()
        self.state = 'draft'
        self.sending_data = False

        self._detach_attachments()

    def action_approved(self):
        for line in self:
            line.state = 'approved'

