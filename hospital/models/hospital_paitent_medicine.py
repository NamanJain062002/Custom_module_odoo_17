from odoo import models, fields, api

class MedicinePaitent(models.Model):
    _name = 'hospiatal.paitent.medicine'
    _description = "ABC"

    name = fields.Many2one('hospital.paitent', string="Name")
    med_name = fields.Many2one('hospital.medicine', string="Medicine Name")
    qty = fields.Integer(string="Quantity")



