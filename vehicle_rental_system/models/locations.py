from odoo import models, fields

class location(models.Model):
    _name = "vehicle.location"
    _description = "Information about location where vehicle can go"
    _rec_name = 'location_name'

    location_name = fields.Char(string="Location")
    two_wheelers = fields.Many2many('vehicle.twowheeler',string="Two wheeler vehicle available")
    four_wheelers = fields.Many2many('vehicle.fourwheeler',string="Four wheeler vehicle available")

    def create_new_record(self, value1, value2, value3):
        new_record = self.env['vehicle.location'].create({'Location': value1,
                               'Two wheeler vehicle available': value2,
                               'Four wheeler vehicle available': value3})
        return new_record

class SaleOrderuu(models.Model):
    _inherit = "sale.order"

    created_by = fields.Char(string="Created By")
