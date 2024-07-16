from odoo import fields, models, api

class department(models.Model):
    _name = 'hospital.department'
    _description = 'Information of departments'

    name = fields.Char(string="Department Name")
    doc_ids = fields.One2many('hospital.docter','dep_id',string="Docters")


    # @api.model
    # def copy(self, default=None):
    #     print("self>>>>>", self)
    #     print("default>>>>>>", default)
    #     res = super(department, self).copy(default)
    #     print("self>>>>>", self)
    #     print("default>>>>>>", default)
    #     print("res>>>>>", res)
    #
    #     return res