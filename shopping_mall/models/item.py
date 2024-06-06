from odoo import models, fields, api, _

class item(models.Model):
    _name = 'shopping.item'
    _description = "Includes the items in shopping mall"
    _rec_name = 'item_name'

    item_name = fields.Char(string="Item Name")
    item_id = fields.Char(string="Item ID", readonly=1)
    item_img = fields.Image(string="Item Image")
    price = fields.Monetary(string="Price")

    # total_price = fields.Monetary(string='My Monetary Field')
    currency_id = fields.Many2one('res.currency', string='Currency')



   # ORM METHOD create method
    @api.model
    def create(self, vals):
        products = self.env['shopping.item'].search([])

        # Get a list of names of the products
        product_names = products.mapped('item_name')

        # Print the list of product names
        print(product_names)

        if vals.get('item_id', _('New')) == _('New'):
            vals['item_id'] = self.env['ir.sequence'].next_by_code('item.sequence') or _('New')
        return super(item, self).create(vals)

    def default_get(self, fields_list):
        print(fields_list)
        default = super(item, self).default_get(fields_list)

        default['item_name'] = 'ITEM'
        default['price'] = 100

        return default

    def get_read_group(self):
        data = self.env['shopping.item'].read_group(
            domain=[('price', '>', 99)],
            fields=['item_name', 'item_id'],
            groupby=['item_name'],
        )
        print(data)
