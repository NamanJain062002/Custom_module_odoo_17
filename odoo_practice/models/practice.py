import base64
from datetime import datetime, timedelta
import io

import dateutil.utils
import xlsxwriter
# from lxml import etree
from lxml import etree

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
    invisible_field = fields.Char(string="Invisible Field")
    flag = fields.Boolean(string="flag", default=False)

    @api.onchange('partner_id')
    def invisible_method(self):
        if self.partner_id:
            self.flag = True
        else:
            self.flag = False
    def demo(self):
        pass

    def print_montly_orders(self):
        print('1')
        admin = self.env.user.name
        today_date = datetime.today()
        last_month_date = today_date - timedelta(days=today_date.day)

        last_month_orders = self.search(
            [('user_id', '=', admin), ('date_order', '>=', last_month_date), ('date_order', '<=', today_date)])

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        sheet = workbook.add_worksheet('Orders')

        bold_format = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 12, 'valign': 'center', 'bg_color': '#00008B',
             'color': '#FFFFFF',
             'border': True})
        normal_format = workbook.add_format(
            {'text_wrap': True, 'valign': 'center', 'align': 'center', 'bg_color': '#ADD8E6', 'border': True,
             'font_size': 10})
        number_format = workbook.add_format(
            {'text_wrap': True, 'valign': 'center', 'align': 'right', 'bg_color': '#ADD8E6', 'border': True,
             'font_size': 10})
        date_format = workbook.add_format(
            {'num_format': 'dd/mm/yy', 'align': 'center', 'valign': 'center', 'bg_color': '#ADD8E6', 'border': True,
             'font_size': 10})
        dollar_format = workbook.add_format(
            {'num_format': '$#,##0.00', 'text_wrap': True, 'valign': 'center', 'align': 'right',
             'bg_color': '#ADD8E6', 'border': True, 'font_size': 10})
        sheet.set_column('A:G', 18)  # Adjust the width as needed
        sheet.set_default_row(30)  # Adjust the height as needed
        row = 1
        col = 0
        print('2')
        # Write headers with bold format
        sheet.write('A1', 'Number', bold_format)
        sheet.write('B1', 'Date', bold_format)
        sheet.write('C1', 'Customer', bold_format)
        sheet.write('D1', 'Sale Person', bold_format)
        sheet.write('E1', 'Status', bold_format)
        sheet.write('F1', 'Total', bold_format)

        for rec in last_month_orders:
            print('3')
            sheet.write(row, col, rec.name or '', number_format)
            sheet.write(row, col + 1, rec.date_order.strftime('%Y-%m-%d') if rec.date_order else '', date_format)
            sheet.write(row, col + 2, rec.partner_id.name or '', normal_format)
            sheet.write(row, col + 3, rec.user_id.name or '', normal_format)
            sheet.write(row, col + 4, rec.invoice_status or '', normal_format)
            sheet.write(row, col + 5, rec.amount_total or 0.0, dollar_format)
            row += 1

        workbook.close()
        output.seek(0)
        excel_file = base64.b64encode(output.read())
        # Create an attachment
        attachment = self.env['ir.attachment'].create({
            'name': f'Sale_Order_report.xlsx',
            'type': 'binary',
            'datas': excel_file,
            'res_model': 'sale.order',
            'res_id': self.id,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        })

        # Return the action to open/download the attachment
        print('4')
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'self'
        }

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
            name = rec.name + rec.email
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


class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'

    def name_get(self):
        print("HIIIII")
        res = []
        for rec in self:
            name = rec.name + " NAMAN"
            res.append((rec.id, name))
        return res

class PosInherit(models.Model):
    _inherit = 'pos.order'

    custom_note = fields.Char(string="Custom Note")
    amount_total = fields.Float(string="Total Amount")
    location = fields.Char(string="Location")


    def get_Partner(self):
        ans = self.env['res.partner'].browse(63)
        print(ans.name)
        return ans.name

    @api.model
    def _order_fields(self, ui_order):
        res = super(PosInherit, self)._order_fields(ui_order)
        res['custom_note'] = ui_order.get('notes')
        res['note'] = ui_order.get('notes')
        res['amount_total'] = ui_order.get('amount_total')
        res['location'] = ui_order.get('location_pos')

        return res

    def get_dis(self):
        print(self)
        param_obj = self.env['ir.config_parameter'].sudo()
        discount_percent = param_obj.get_param('discount_percent')
        # if float(discount_percent) > 100 or float(discount_percent) <= 0:
        #     print("Invalid")
        #     ValidationError("Invalid Discount Percentage")
        # else:
        return float(discount_percent)
        # for i in disc:
        #     print(i.discount_percent)
        #     return i.discount_percent
    # @api.onchange('custom_note')
    # def temp(self):
    #     if self.custom_note:
    #         self.note = self.custom_note


    # @api.model
    # def create(self, vals_list):
    #   session = self.env['pos.session'].browse(vals_list['session_id'])
    #   print(session)
    #   if session:
    #       orders = self.env['pos.order'].search([('session_id', '=', session.id)])
    #       print(orders)

      # vals = self._complete_values_from_session(session, vals_list)


      # return super().create(vals_list)

class ResConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    discount_percent = fields.Integer(
        string="Discount %",
        config_parameter='discount_percent'
    )


    location = fields.Many2many(
        string='Locations',
        related='pos_config_id.location_ids',
        readonly=False,
    )






    @api.constrains('discount_percent')
    def set_discount(self):
        for rec in self:
            if rec.discount_percent <= 0 or rec.discount_percent > 100:
                raise ValidationError("Invalid Discount Percent")


class ResSettingShoppingMall(models.TransientModel):
    _inherit = 'res.config.settings'

    tax = fields.Float(string="Tax %",  config_parameter='tax')

class PosConfig(models.Model):
    _inherit = 'pos.config'
    location_ids = fields.Many2many('res.location', string='Locations')

    def get_locations(self):
       result = []
       data = self.env['pos.config'].search([])
       for i in data:
          for j in i.location_ids:
             result.append(j.location)

       return result




