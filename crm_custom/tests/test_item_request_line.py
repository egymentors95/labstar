from odoo.tests.common import TransactionCase


class TestItemRequestLineReport(TransactionCase):
    def test_group_report_with_monetary_total(self):
        lead = self.env['crm.lead'].create({
            'name': 'Item requirements test',
            'type': 'opportunity',
        })
        self.env['item.request.line'].create({
            'lead_id': lead.id,
            'name': 'Test item',
            'price': 42.0,
        })

        lines = self.env['item.request.line']
        for groupby in ('agent_id', 'item_request_type', 'current_supplier_id', 'lead_id', 'create_date:month'):
            groups = lines._read_group(
                [('lead_id', '=', lead.id)],
                groupby=[groupby],
                aggregates=['price:sum', 'quantity:sum'],
            )
            self.assertEqual(len(groups), 1)
            self.assertEqual(groups[0][1:], (42.0, 1.0))
