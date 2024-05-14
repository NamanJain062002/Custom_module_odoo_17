from odoo import models, fields, api

class CommissionAdmin(models.Model):
    _name = 'sale.admin'
    _description = "ABC"

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    saleperson = fields.Many2one('res.users', string="Saleperson")
    notebook_data = fields.Many2many('sale.order', string='Notebook Data', compute="get_saleperson_order")


    @api.depends('start_date', 'end_date')
    def get_saleperson_order(self):
        for rec in self:
            if rec.start_date and rec.end_date and rec.saleperson.name:
                print(rec.saleperson.name)
                domain = [(['date_order', '>=', rec.start_date]), (['date_order', '<=', rec.end_date]), (['user_id', '=', rec.saleperson.name])]
                records = self.env['sale.order'].search(domain)
                rec.notebook_data = [(6, 0, records.ids)]
            else:
                rec.notebook_data = False

    def get_orders(self):
        pass
