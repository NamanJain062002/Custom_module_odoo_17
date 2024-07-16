{
    'name': 'Hospital Management System',
    'version': '1.0',
    'summary': 'Mange Hospital work',
    'author': 'Naman Jain',
    'depends': ['base', 'mail', 'account'],
    'data': ['security/ir.model.access.csv',
        'views/paitent_view.xml',
        'views/docter_view.xml',
             'views/department_view.xml',
        'views/menu_view.xml',
             'views/medicine_view.xml',
             'views/hospital_medicine_view.xml'
             ],
    'assets': {
        'web.assets_backend': [
            # 'hospital/static/src/xml/button.xml'
        ],
    },
    'installable': True,
    'application': True,
}
