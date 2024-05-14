from odoo import models, fields, api, _

class item(models.Model):
    _name = 'shopping.item'
    _description = "Includes the items in shopping mall"

    item_name = fields.Many2one(string="Item Name", comodel_name='shopping.customer')
    item_id = fields.Char(string="Item ID", readonly=1)
    item_img = fields.Binary(string="Item Image")
    price = fields.Float(string="Price")


   # ORM METHOD create method
    @api.model
    def create(self, vals):
        if vals.get('item_id', _('New')) == _('New'):
            vals['item_id'] = self.env['ir.sequence'].next_by_code('item.sequence') or _('New')
        return super(item, self).create(vals)

    #



