from odoo import models, fields

class Medicine(models.Model):
    _name = 'hospital.medicine'
    _description = 'Medicine stock hospital have'
    _rec_name = 'medicine_name'

    medicine_name = fields.Char(string="Medicine")
    stock_available = fields.Integer(string="Stock Available")



