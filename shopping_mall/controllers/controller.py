from odoo import http
from odoo.http import request
import json


class SaleOrderController(http.Controller):

    @http.route('/create_sale_order', type='json', auth='public', methods=['POST'], csrf=False)
    def create_sale_order(self, **kwargs):
        try:
            # Extract data from the request
            data = json.loads(request.httprequest.data)

            # Define sale order values
            order_vals = {
                'partner_id': data.get('partner_id'),
                'order_line': [(0, 0, {
                    'product_id': line.get('product_id'),
                    'product_uom_qty': line.get('quantity'),
                    'price_unit': line.get('price_unit'),
                }) for line in data.get('order_lines', [])]
            }
            print(order_vals['partner_id'])

            # Create the sale order
            sale_order = request.env['sale.order'].sudo().create(order_vals)

            return {'status': 'success', 'sale_order_id': sale_order.id}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}



class CustomWebsite(http.Controller):
    @http.route('/custom', type='http', auth='public', website=True, csrf=False)
    def website(self, **post):
        # print(post)
        # print(request.env.user.name)
        return request.render('shopping_mall.my_model_image_form')

    @http.route('/custom/thankyou', type='http', auth='public', website=True, csrf=False)
    def thankyou(self, **post):
        print(post)
        print(">>>>>>>", request.env.user.name)
        if request.env.user.name == 'Public user':
          request.env['shopping.public'].sudo().create({
              'name': post.get('name'),
              'email': post.get('email'),
              'address': post.get('address'),
              'mobile': post.get('mobile')
          })
        else:
            request.env['shopping.form'].sudo().create({
                'name': post.get('name'),
                'email': post.get('email'),
                'address': post.get('address'),
                'mobile': post.get('mobile')
            })


        return request.render('shopping_mall.thankyou')
