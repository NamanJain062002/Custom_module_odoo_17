{
    'name': 'Sales Approval',
    'version': '1.0',
    'summary': 'Backend Task',
    'author': 'Naman Jain',
    'depends': ['base', 'sale', 'sale_management'],
    'data': [
        'views/sale_configuration.xml',
        'views/approve_button.xml',
        'security/security.xml',
        'views/approve_order_menu.xml',
        'views/SaleOrderLine_inherit.xml',
        'report/sale_order_report_inherit.xml'
    ],

    'installable': True,
    'application': True,
    'sequence': -20,
}
