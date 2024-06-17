from odoo import fields, models, api


class Saleperson(models.Model):
    _name = 'sale.person'
    _description = 'Information about the sale person sales'

    name = fields.Many2one(string="Sale Person", comodel_name='res.users')
    no_of_orders = fields.Integer(string="Number of orders", readonly=1)
    total_sale_amount = fields.Float(string="Total sales",  readonly=1)

    @api.onchange('name')
    def get_sale_orders(self):
        count = 0
        print(self.name.name)
        orders = self.env['sale.order'].search([])
        for order in orders:
            if order.user_id.name == self.name.name:
                count += 1
        self.no_of_orders = count

    @api.onchange('name')
    def get_total_sale_amount(self):
        count = 0
        print(self.name.name)
        orders = self.env['sale.order'].search([])
        for order in orders:
            if order.user_id.name == self.name.name:
                count += order.amount_total
        self.total_sale_amount = count