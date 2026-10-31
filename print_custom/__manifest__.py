{
    'name': 'Print Custom - Bank Footer',
    'version': '19.0.1.0.0',
    'category': 'Hidden/Tools',
    'summary': 'Bank footer on Sales, Accounting and Purchase reports, configured in the company tab',
    'depends': ['sale', 'account', 'purchase'],
    'author': 'Mohamed Awad',

    'data': [
        'report/print_custom_templates.xml',
        'views/res_company_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
