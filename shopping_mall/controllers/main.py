from odoo import http
from odoo.http import request

class Main(http.Controller):

    @http.route('/shopping_mall/hello', type='http', auth='public', website=True)
    def hello(self, **kwargs):
        return request.render("shopping_mall.shopping_template", {})
