from odoo import models, fields

class fourWheeler(models.Model):
    _name = "vehicle.fourwheeler"
    _description = "Information about four wheelers"

    name = fields.Char(string="Vehicle Name")
    is_rented = fields.Boolean(string="Available", default=True)
    fourwheeler_driver_name_id = fields.Many2one('vehicle.driver', string="Allocated Driver")
    locations = fields.Many2many('vehicle.location',string="Locations available")
    vechile_rent = fields.Float(string="Vehicle Rent/ Day", inverse="calc_driver_rent")
    driver_charge = fields.Float(string="Driver Rent/ Day")

# created a inverse attribute in vehicle rent and cal driver charge
    def calc_driver_rent(self):
        for rec in self:
            rec.driver_charge = (10*rec.vechile_rent)/100

