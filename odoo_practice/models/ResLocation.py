from odoo import fields, models, api
class ResLocation(models.Model):
    _name = 'res.location'
    _description = "Location for POS shop"
    _rec_name = 'location'

    location = fields.Char(string="Location")