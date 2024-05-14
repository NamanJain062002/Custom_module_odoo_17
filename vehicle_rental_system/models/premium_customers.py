from odoo import models, fields, api

class PremiumCustomer(models.Model):
    _name = 'vehicle.premium'
    _inherit = 'vehicle.customer'
    _description = "Information about premium customers"




