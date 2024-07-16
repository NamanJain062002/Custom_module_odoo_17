from odoo import fields, models, api
from odoo.exceptions import ValidationError


class paitent(models.Model):
    _name = "hospital.paitent"
    _inherit = ['mail.thread', 'mail.activity.mixin']
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



    @api.model
    def create(self, vals):
        res = super(paitent, self).create(vals)

        # change medicine stock according to order
        selected_medicine = res['add_medicine']
        for medicine in selected_medicine:
            if medicine.med_name.stock_available - medicine.qty < 0:
                raise ValidationError("Out of Stock, Please select quantity in available stock")
            else:
                medicine.med_name.stock_available = medicine.med_name.stock_available - medicine.qty

        return res
    def write(self, vals):
        res = super(paitent, self).write(vals)

        # selected_medicine = res['add_medicine']
        # for medicine in selected_medicine:
        #     medicine.med_name.stock_available = medicine.med_name.stock_available - medicine.qty
        # print(self.add_medicine)
        print(vals)
        # print(vals['add_medicine'])
        # print(vals['add_medicine'][0][1])

        # for i in self.add_medicine:
        #     print(i)
        if 'add_medicine' in vals:
            # selected_medicine = res['add_medicine']
            # for medicine in selected_medicine:
            for medicine in self.add_medicine:
                print(medicine.qty)
                # medicine.med_name.stock_available = medicine.med_name.stock_available - medicine.qty


        # print(vals)
        return res


    # @api.model
    # def create(self, vals):
    #     print(self)
    #     order = super(paitent, self).create(vals)
    #     print(self)
    #
    #     order.get_data()
    #     return order
    #
    # # def write(self, vals):
    # #     order = super(paitent, self).write(vals)
    # #     if order:
    # #         self.get_data()
    # #     return order
    # def copy(self, default=None):
    #     print("self>>>>>", self)
    #     print("default>>>>>>", default)
    #     res = super(paitent, self).copy(default)
    #     print("self>>>>>", self)
    #     print("default>>>>>>", default)
    #     print("res>>>>>", res)
    #
    #     return res
    #
    # def unlink(self):
    #     print("self>>>", self)
    #     res = super(paitent, self).unlink()
    #     print("self>>>>>", self)
    #     print("res>>>>", res)
    #     return res
