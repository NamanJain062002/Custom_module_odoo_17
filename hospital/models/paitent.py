from odoo import fields, models

class paitent(models.Model):
    _name = "hospital.paitent"
    _description = "details about paitents"

    name = fields.Char(string="Name")
    ward_number = fields.Integer(string="Ward Number")
    bed_number = fields.Integer(string="Bed Number")
    mobile = fields.Integer(string="Mobile Number")
    assigned_doc = fields.Many2many('hospital.docter',string="Assigned Docters")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")