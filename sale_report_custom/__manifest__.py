{
    'name': 'Sales Custom - Quotation Report',
    'version': '19.0.2.0.0',
    'category': 'Sales',
    'summary': 'Custom printable quotation / sales order with repeating header and bank footer',
    'description': """
Sale-order specific report overrides:
- always show the discount column on the quotation / sale order report.

The bank footer style was moved to the separate 'print_custom' addon,
which applies it to Sales, Accounting and Purchase reports.
    """,
    'depends': ['sale_management'],
    'author': 'Mohamed Awad',

    'data': [
        'report/sale_report_templates.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
