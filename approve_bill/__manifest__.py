{
    'name': "Invoice Approval",
    'version': '19.0.2.0.0',
    'summary': """This module add the multiple approval option for invoice,
    			  bill,refund and credit notes.""",
    'description': """This module add the multiple approval option for invoice,
    bill,refund and credit notes.""",
    'category': 'Accounting',
    'author': 'Omar abd alrahim',
    'website': "https://www.cybrosys.com",
    'depends': ['account'],
    'data': [

        'views/account_move_inherited.xml',
    ],
    'license': "AGPL-3",
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
}
