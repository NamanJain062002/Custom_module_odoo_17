{
    'name': 'Practice Odoo',
    'version': '1.0',
    'summary': 'Practice purpose',
    'author': 'Naman Jain',
    'depends': ['base', 'sale', 'sale_management', 'stock', 'mail', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/practice_view.xml',
        'views/sale.xml',
        'views/salePerson.xml',
        'views/commission_sale_order_view.xml',
        'views/commission_admin_view.xml',
        'views/submenu_reporting_excel.xml',
        'views/menu_inherit.xml',
        'wizards/print_report_sale_view.xml',
        'views/res_partner_view.xml',
        'data/email_template_view.xml',
        'reports/report.xml',
        'wizards/print_sale_excel_view.xml',
        'views/res_partner_inherit_view.xml',
        'data/birthday_template.xml',
        'views/tree_view_inherit.xml'
    ],

    'installable': True,
    'application': True,
    'sequence': -20,
}
