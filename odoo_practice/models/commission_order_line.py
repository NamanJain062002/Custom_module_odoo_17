from odoo import fields, models, api

class Commission(models.Model):
    _name = 'sale.commission'
    _description = "Information about sale commission"

    order_no = fields.Char(string="Order Number")
    customer = fields.Char(string="Customer")
    salesperson = fields.Char(string="Salesperson")
    commission_percentage = fields.Float(string="Commission Percentage")
    commission = fields.Float(string="Commission Amount", compute="calc_commission")
    total = fields.Float(string="Amount Total")

    @api.depends('total')
    def calc_commission(self):
        for rec in self:
            rec.commission = (5 * rec.total) / 100
