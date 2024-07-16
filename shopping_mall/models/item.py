from lxml import etree

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

    extra_info = fields.Char('Extra Info')



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

        print(default)

        return default

    def get_read_group(self):
        data = self.env['shopping.item'].read_group(
            domain=[('price', '>', 99)],
            fields=['item_name', 'item_id'],
            groupby=['item_name'],
        )
        print(data)

    # @api.model
    # def _get_view(self, view_id=None, view_type='form', **options):
    #     def make_delegated_fields_readonly(node):
    #         for child in node.iterchildren():
    #             if child.tag == 'field' and child.get('name') in delegated_fnames:
    #                 child.set('attrs', "{'readonly': [('parent_id', '!=', False)]}")
    #             else:
    #                 make_delegated_fields_readonly(child)
    #         return node
    #
    #     delegated_fnames = set(self._get_company_root_delegated_field_names())
    #     arch, view = super()._get_view(view_id, view_type, **options)
    #     arch = make_delegated_fields_readonly(arch)
    #     return arch, view

    # def _get_view(self, view_id=None, view_type='form', **options):
    #     print("test Case 1")
    #     # Call the super method to get the default view architecture
    #     result = super(item, self)._get_view(view_id=view_id, view_type=view_type, **options)
    #
    #     if view_type == 'form' and self.currency_id.name == 'USD':
    #         print("test Case 2")
    #         doc = etree.XML(result['arch'])
    #
    #         # Find the location to insert the new field
    #         for node in doc.xpath("//sheet"):
    #             extra_field = etree.Element('field', name='extra_info')
    #             node.append(extra_field)
    #
    #         result['arch'] = etree.tostring(doc, encoding='unicode')
    #     print("test Case 3")
    #     return result
