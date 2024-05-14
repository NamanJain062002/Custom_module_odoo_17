from odoo import models, fields

class fourWheeler(models.Model):
    _name = "vehicle.fourwheeler"
    _description = "Information about four wheelers"

    name = fields.Char(string="Vehicle Name")
    is_rented = fields.Boolean(string="Available", default=True)
    fourwheeler_driver_name_id = fields.Many2one('vehicle.driver', string="Allocated Driver")
    locations = fields.Many2many('vehicle.location',string="Locations available")

