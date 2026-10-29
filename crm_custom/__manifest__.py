{
    'name': 'CRM Custom',
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'summary': 'Configure item request types and requested items on CRM opportunities',
    'author': 'Mohamed Awad',
    'depends': ['crm', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'security/item_request_security.xml',
        'views/item_request_type_views.xml',
        'views/crm_lead_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
