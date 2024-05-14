from odoo import fields, models, api

class bills(models.Model):
    _name = 'shopping.bill'
    _description = "Details about the paid and unpaid bills"

    name = fields.Char(string="Name")
    cus_id = fields.Char(string="CUS ID")
    payment_status = fields.Char(string="Payment Status")
    shopping_date = fields.Date(string="Shopping Date")
    total_payment = fields.Float(string="Total Payment")

