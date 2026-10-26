{
    'name': 'Sales Custom - Quotation Report',
    'version': '19.0.1.0.1',
    'category': 'Sales',
    'summary': 'Custom printable quotation / sales order with repeating header and bank footer',
    'depends': ['sale_management'],
    'author': 'Mohamed Awad',

    'data': [
        'report/paperformat_sale_bank.xml',
        'report/sale_report_templates.xml',
        'views/res_company_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
