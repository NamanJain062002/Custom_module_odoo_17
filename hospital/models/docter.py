from odoo import models, fields, api
from odoo.exceptions import ValidationError


class docter(models.Model):
    _name = "hospital.docter"
    _description = "Information of docters"

    name = fields.Char(string="Name")
    doc_id = fields.Integer(string="Docter ID")
    assigned_pat = fields.Many2many('hospital.paitent',string="Assigned Paitent",domain=[('bed_number','>','5')])
    dep_id = fields.Many2one('hospital.department',string="Department")
    base_salary = fields.Integer(string="Base Salary")
    allowance = fields.Integer(string="Allowance Amount")
    ctc = fields.Integer(string="Total CTC",compute='calc_ctc')
    active = fields.Boolean('Active', default=True)  # used for Archived

    # _sql_constraints = [('unique_name', 'UNIQUE (name)', 'docter name must be unique.')]

    # @api.onchange('base_salary')
    # def on_change(self):
    #     if self.base_salary <= 1000:
    #         raise ValidationError("Ivalid Salary")


    @api.depends('base_salary','allowance')
    def calc_ctc(self):
        for record in self:
            ctc = 0
            if record.base_salary:
                ctc += record.base_salary
            if record.allowance:
                ctc += record.allowance
            record.ctc = ctc

    @api.model
    def create(self, vals):
        print("self", self)
        print("vals", vals) # vals['name']
        print(vals['name'])
        res = super(docter, self).create(vals)
        print("self", self)
        print("vals", vals)
        print("res", res) # res['name']
        print(res.name)
        return res

    def write(self, vals):
        print("self>>>>>", self)
        print("vals>>>>>>", vals)
        res = super(docter, self).write(vals)
        print("self>>>>>", self)
        print("vals>>>>>>", vals)
        print("res>>>>>", res)

        return res


