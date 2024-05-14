from odoo import fields, models

class department(models.Model):
    _name = 'hospital.department'
    _description = 'Information of departments'

    name = fields.Char(string="Department Name")
    doc_ids = fields.One2many('hospital.docter','dep_id',string="Docters")