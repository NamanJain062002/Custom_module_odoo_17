{
    'name': 'Shopping Mall',
    'version': '1.0',
    'summary': 'Mange the buisness activity in mall',
    'author': 'Naman Jain',
    'depends': ['base', 'mail', 'sale', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/review_view.xml',
        'views/customer_view.xml',
        'views/item_view.xml',
        'views/review_record_view.xml',
        'views/paid_bill_view.xml',
        'views/unpaid_bill_view.xml',
        'data/sequence_view.xml',
        'reports/report.xml',
        'views/menu_view.xml',
        'data/email_template.xml'
        # 'views/shopping_report_view.xml'
    ],

    'installable': True,
    'application': True,
    'sequence': -20,
}
