from odoo import http
from odoo.http import request

class Main(http.Controller):

    @http.route('/shopping_mall/hello', type='http', auth='public', website=True)
    def hello(self, **kwargs):
        return request.render("shopping_mall.shopping_template", {
            'names': ['NAMAN', 'Veera', 'Anubhav', 'rohit']
        })
        # customers = request.env['shopping.customer'].search([])
        # return request.render("shopping_mall.shopping_customer_id", {
        #     'customers': customers
        # })

    # @http.route('/shopping_mall/<name>', auth='public')
    # def show_name(self, name):
    #     return '<h1>{}</h1>'.format(name)


    # @http.route('/shopping_mall/veera_web', auth='public')
    # def veera(self, **kwargs):
    #     return request.render("shopping_mall.veera_custom_id", {})

    # @http.route('/shopping_mall/create_sale_order', auth='public')
    # def show_sale_order(self):
    #     data = request.env['sale.order'].search([])
    #     return request.render("shopping_mall.sale_order_data", {
    #         'sale_data': data
    #     })
