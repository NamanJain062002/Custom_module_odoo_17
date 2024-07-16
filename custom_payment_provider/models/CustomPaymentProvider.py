from odoo import models, fields, api

class CyberSource(models.Model):
    _inherit = 'payment.provider'

    # code = fields.Selection(selection_add=[
    #     ('custom', 'Custom Payment Provider')
    # ], ondelete={'custom': 'set default'})


    merchant_id = fields.Char('Merchant ID')
    api_key_id = fields.Char('API KEY')
    secret_key = fields.Char('Secret KEY')


