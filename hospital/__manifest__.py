{
    'name': 'Hospital Management System',
    'version': '1.0',
    'summary': 'Mange Hospital work',
    'author': 'Naman Jain',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv',
        'views/paitent_view.xml',
        'views/docter_view.xml',
             'views/department_view.xml',
        'views/menu_view.xml'
             ],
    'installable': True,
    'application': True,
}
