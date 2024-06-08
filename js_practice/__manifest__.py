{
    'name': 'Practice',
    'summary': 'JS',
    'author': 'Naman Jain',
    'depends': ['base', 'web', 'hr_expense', 'website_sale'],
    'data': [
        # 'views/connection.xml'
    ],

    'assets': {
        'web.assets_backend': [
          'js_practice/static/src/js/add_btn.js',
          'js_practice/static/src/xml/add_btn.xml',
           'js_practice/static/src/js/class_a.js',
            'js_practice/static/src/js/class_b.js',
            'js_practice/static/src/js/hello.js',
            'js_practice/static/src/xml/add_icon.xml'

        ],
        'web.assets_frontend': [
'js_practice/static/src/js/include_example.js'
        ]
        # 'point_of_sale.assets': [
        #     'js_practice/static/src/js/wb_js.js',
        #     'js_practice/static/src/xml/wb_btn.xml'
        # ]
    },


    'installable': True,
    'application': True,
    'sequence': -200,
}
