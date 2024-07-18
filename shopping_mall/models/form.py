from odoo import models, fields, api, _

class Form(models.Model):
    _name = 'shopping.form'
    _description = "form data"


    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    address = fields.Char(string="Address")
    mobile = fields.Char(string="Mobile")
