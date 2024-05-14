from odoo import fields, models, api

class PaidBill(models.Model):
    _inherit = 'shopping.bill'
    _name = 'shopping.paidbill'
