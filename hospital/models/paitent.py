from odoo import fields, models, api
from odoo.exceptions import ValidationError


class paitent(models.Model):
    _name = "hospital.paitent"
    _description = "details about paitents"
    _rec_name = 'name'

    name = fields.Char(string="Name")
    ward_number = fields.Integer(string="Ward Number")
    bed_number = fields.Integer(string="Bed Number")
    mobile = fields.Integer(string="Mobile Number")
    assigned_doc = fields.Many2many('hospital.docter', string="Assigned Docters")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    payment_done = fields.Boolean(string="Payment Done")
    add_medicine = fields.One2many('hospiatal.paitent.medicine', 'name', string="Medicine added")

    def get_data(self):
        for rec in self:
            if self.payment_done == True:
                for medi in rec.add_medicine:
                    qty_reduce = medi.qty
                    if qty_reduce > medi.med_name.stock_available:
                        raise ValidationError("You adding more medicine quantity than stock")
                    else:
                         medi.med_name.stock_available -= qty_reduce
    # def get_write_data(self, vals):

    @api.model
    def create(self, vals):
        order = super(paitent, self).create(vals)
        order.get_data()
        return order

    # def write(self, vals):
    #     order = super(paitent, self).write(vals)
    #     if order:
    #         self.get_data()
    #     return order
