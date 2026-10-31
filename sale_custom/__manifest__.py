{
    'name': 'Sales Custom - Base Unit',
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'summary': 'Show the base unit and base unit value on sale order lines',
    'description': """
Adds Base Unit and Base Unit Value fields on sale order lines.

The base unit is the unit of measure configured on the product.
The base unit value is the ordered quantity converted to that unit.
Example: product unit = Gram, sale order line unit = Kilogram, quantity = 1
=> Base Unit = Gram, Base Unit Value = 1000.
    """,
    'author': 'Mohamed Awad',
    'depends': ['sale_management', 'uom'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
