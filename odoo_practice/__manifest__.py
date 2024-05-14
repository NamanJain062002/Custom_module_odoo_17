{
    'name': 'Practice Odoo',
    'version': '1.0',
    'summary': 'Practice purpose',
    'author': 'Naman Jain',
    'depends': ['base', 'sale', 'sale_management', 'stock'],
    'data': ['security/ir.model.access.csv',
             'views/practice_view.xml',
             'views/sale.xml',
             'views/commission_sale_order_view.xml',
             'views/commission_admin_view.xml',
             'views/menu_inherit.xml',
             'wizards/print_report_sale_view.xml'
             ],

    'installable': True,
    'application': True,
    'sequence': -20,
}
