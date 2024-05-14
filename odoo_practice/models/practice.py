from odoo import fields, models, api

from odoo.exceptions import ValidationError


class practice(models.Model):
    _name = 'pratice.pratice'
    _description = "For Practice purpose"

# class ResPartner(models.Model):
#     _inherit = 'res.partner'
#     commission = fields.Float(string="Commission")


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    new_data = fields.Char(string="New Data")
    commission = fields.Float(string="Commission", compute="calc_commission")

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        partner_name = self.env['res.partner'].browse(vals.get('partner_id')).name if vals.get('partner_id') else False
        user_name = self.env['res.users'].browse(vals.get('user_id')).name if vals.get('user_id') else False
        total_amount = res.amount_total
        rec = self.env['sale.commission'].create({
            'order_no': vals.get('name'),
            'customer': partner_name,
            'salesperson': user_name,
            'commission_percentage': 5,
            'commission': vals.get('commission'),
            'total': total_amount
        })
        return res

    @api.depends('amount_total')
    def calc_commission(self):
        for rec in self:
            rec.commission = (5 * rec.amount_total) / 100

    def action_confirm(self):
        for rec in self:
            for record in rec.order_line:
                if record.product_uom_qty <= 0:
                    raise ValidationError("Quantity should be positive")
        print("NAMAN>>>>>>>>>>>>>>>>")
        return super(SaleOrder, self).action_confirm()

    def _get_order_lines_to_report(self):
        if self._context.get('my_report'):
            print(" \m\\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nhn\self<>>>>>>", self._context.get('order_lines'))
            order_line = self.env['sale.order.line'].browse(self._context.get('order_lines'))
            return order_line
            # return self._cont//ext.get('order_lines')
        else:
            return super(SaleOrder, self)._get_order_lines_to_report()


class stockPicking(models.Model):
    _inherit = 'stock.picking'
    new_data = fields.Char(string="New Data")

class ResPartner(models.Model):
    _inherit = 'res.partner'
    commission = fields.Float(string="Commission")
    commission_percent = fields.Float(string="Percentage")

    @api.model
    def name_get(self):
        print("NAME GET")
        result = []
        for rec in self:
            name = rec.name+rec.email
            result.append((rec.id, name))
        return result
