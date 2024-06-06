from odoo import fields, models, api
from odoo.exceptions import ValidationError

class reviewRecord(models.Model):
    _name = 'shopping.reviewrecord'
    _description = "Review of items in mall"

    item_name = fields.Char(string="Item")
    item_id = fields.Char(string="Item ID")
    rating = fields.Char(string="Rating")
    reviews = fields.Text(string="Review")


