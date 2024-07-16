from odoo import models, fields

class DelegationInheritance(models.Model):
    _name = 'demo.demo'
    _inherits = {'res.partner': 'partner_id'}

    name = fields.Char(string="Demo Name")
