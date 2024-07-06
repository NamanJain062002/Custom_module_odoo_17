{
    'name': 'Practice',
    'summary': 'JS',
    'author': 'Naman Jain',
    'depends': ['base', 'web', 'hr_expense', 'website_sale', 'web_gantt', 'point_of_sale', 'pos_sale'],
    'data': [
        'views/connection.xml'
    ],

    'assets': {
        'web.assets_backend': [
            'js_practice/static/src/js/add_btn.js',
            'js_practice/static/src/js/patch.js',
            'js_practice/static/src/xml/add_btn.xml',
            'js_practice/static/src/js/class_a.js',
            'js_practice/static/src/js/class_b.js',
            'js_practice/static/src/js/hello.js',
            'js_practice/static/src/xml/add_icon.xml',
            'js_practice/static/src/js/custom_controller.js',
            'js_practice/static/src/xml/custom_controller_template.xml',
            'js_practice/static/src/js/custom_list_controller.js'
            # 'js_practice/static/src/xml/pos_logo.xml'

            # 'js_practice/static/src/xml/pos_logo.xml'
            # 'js_practice/static/src/xml/portal_sidebar_inherit.xml'
        ],
        'web.assets_frontend': [
            # 'js_practice/static/src/js/publicWidget_example.js',
            # 'js_practice/static/src/js/include_example.js'
            # 'js_practice/static/src/xml/portal_sidebar_inherit.xml',

        ],

        'point_of_sale._assets_pos': [
            'js_practice/static/src/js/pos_btn.js',
            'js_practice/static/src/xml/pos_btn.xml',
            'js_practice/static/src/js/pos_paymentScreenbtn.js',
            'js_practice/static/src/js/customNote_pos.js',
            'js_practice/static/src/js/discount_task.js',
            'js_practice/static/src/js/SuntryCustomer.js',
            'js_practice/static/src/js/location_button.js',
            'js_practice/static/src/js/CustomPopUp.js',
            'js_practice/static/src/js/emi_button.js',
            'js_practice/static/src/xml/EMI_popup.xml',
            'js_practice/static/src/js/emi_popup.js',
        ]
    },

    'installable': True,
    'application': True,
    'sequence': -200,
}
