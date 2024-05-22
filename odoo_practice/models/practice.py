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

class ResPartner(models.Model):
    _inherit = 'res.partner'
    dob = fields.Date(string="DOB")

    @api.model
    def send_birthday_mail(self):
        today = fields.Date.today()
        today_month_day = today.strftime('%m-%d')
        all_records = self.search([])
        for rec in all_records:
            if rec.dob and rec.dob.strftime('%m-%d') == today_month_day:
                email_values = {
                    'email_to': rec.email,
                    'subject': f"Happy Birthday {rec.name}"
                }
                mail_template = self.env.ref('odoo_practice.birthday_email_template')
                mail_template.send_mail(rec.id, email_values=email_values, force_send=True)
        # mail_template = self.env.ref('odoo_practice.mail_template_res_partner_id')
        # mail_template.send_mail(
        #     force_send=True  # Set to True to send the email immediately
        # )

    def print_report(self):
        return self.env.ref('odoo_practice.res_partner_customer_report_action').report_action(self)

    def _get_customer_information(self):
        # Implement the logic to retrieve customer information here
        return {'name': self.function}

    def send_email(self):
        self.ensure_one()
        # self.order_line._validate_analytic_distribution()
        lang = self.env.context.get('lang')
        mail_template = self.env.ref('odoo_practice.mail_template_res_partner_id')
        if mail_template and mail_template.lang:
            lang = mail_template._render_lang(self.ids)[self.id]
        ctx = {
            'default_model': 'sale.order',
            'default_res_ids': self.ids,
            'default_template_id': mail_template.id if mail_template else None,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'default_email_layout_xmlid': 'mail.mail_notification_layout_with_responsible_signature',
            'proforma': self.env.context.get('proforma', False),
            'force_email': True,

        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }

