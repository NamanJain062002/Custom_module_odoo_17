from odoo import models, fields, api, _

class PublicForm(models.Model):
    _name = 'shopping.public'
    _description = "form data"


    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    address = fields.Char(string="Address")
    mobile = fields.Char(string="Mobile")
