from odoo import models, fields, api
from odoo.exceptions import ValidationError


class twoWheeler(models.Model):
    _name = "vehicle.twowheeler"
    _description = "Information about two wheelers"

    name = fields.Char(string="Vehicle Name")
    is_rented = fields.Boolean(string="Available", default=True)
    driver_name_id = fields.Many2one('vehicle.driver', string="Allocated Driver")
    locations = fields.Many2many('vehicle.location', string="Locations available")


    def check_orm(self):
        # search method
        rec = self.env['vehicle.twowheeler'].search([('is_rented', '=', 'True')])
        # search count method
        rec2 = self.env['vehicle.twowheeler'].search_count([('is_rented', '=', 'True')])
        #---- Filtered ------#
        filt_data = self.env['vehicle.twowheeler'].search([]).filtered(lambda r:r.is_rented == True)
        print("Filtered Method triggered", filt_data)
        #---- Search Read Method --------#
        sec_red = self.env['vehicle.twowheeler'].search_read([('is_rented', '=', 'True')], ['name', 'locations'])
        print("Search Read data------->",sec_red)
        print(type(rec))
        print(type(rec2))


        return rec, rec2, filt_data, sec_red

    @api.model
    # create method
    def create(self, vals_list):
        res = super(twoWheeler, self).create(vals_list)
        if vals_list['is_rented'] == True:
            raise ValidationError("Cant Create is rented record...")
        print("res----->", type(res), "vals_list----->", vals_list, "self----->", self)

        return res
    # write method
    def write(self, vals):
        res = super(twoWheeler, self).write(vals)
        # Search Method
        sec = super().search([('is_rented', '=', 'True')])
        print("res---->",res, "vals----->", vals, "self----->", self)
        print("sec---->", sec,"self---->", self)

        return res,sec

    # unlink method
    def unlink(self):
        res = super(twoWheeler, self).unlink()
        print("res---->", res, "self----->", self)

        return res

    # Copy method
    def copy(self, default=None):
        res = super(twoWheeler, self).copy(default)
        print("res---->", res, "default----->", default, "self----->", self)
        return res




