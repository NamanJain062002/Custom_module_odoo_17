from odoo import fields, models, api
from odoo.exceptions import ValidationError

class reviewRecord(models.Model):
    _name = 'shopping.reviewrecord'
    _description = "Review of items in mall"

    item_name = fields.Char(string="Item", readonly=1)
    item_id = fields.Char(string="Item ID", readonly=1)
    rating = fields.Char(string="Rating", readonly=1)
    reviews = fields.Text(string="Review", readonly=1)


