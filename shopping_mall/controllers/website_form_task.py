from odoo import http
from odoo.http import request
import json

class CustomEmailController(http.Controller):
    @http.route('/website/form/<string:model_name>', type='json', auth='public', methods=['POST'], website=True)
    def create_email(self, **kwargs):
        # print(**kwargs)
        values = json.loads(request.httprequest.data)
        print(values)
        if values:
            request.env['mail.mail'].sudo().create(values.get('data_value'))
            return {'status': 'success', 'message': 'Email created successfully'}
        return {'status': 'error', 'message': 'Missing values'}