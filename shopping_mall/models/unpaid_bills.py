from odoo import fields, models, api

class UnpaidBill(models.Model):
    _inherit = 'shopping.bill'
    _name = 'shopping.unpaidbill'
