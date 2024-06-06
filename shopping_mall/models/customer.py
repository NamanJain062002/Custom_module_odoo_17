import io
from calendar import month
from datetime import date, datetime

import xlsxwriter

from odoo import models, fields, api, _
import xlwt
import base64
from io import BytesIO


class customer(models.Model):
    _name = 'shopping.customer'
    _inherit = ['mail.thread']
    _description = 'information about customers'

    name = fields.Char(string="Name", required=1)
    dob = fields.Date(string="Date Of Birth")
    email = fields.Char(string="Email")
    cus_id = fields.Char(string="Customer ID", readonly=1)
    shopping_date = fields.Date(string="Shopping Date")
    billing_counter = fields.Selection(
        [('counter 1', 'Counter 1'), ('counter 2', 'Counter 2'), ('counter 3', 'Counter 3'), ('counter 4', 'Counter 4'),
         ('counter 5', 'Counter 5'), ], string="Billing Counter")
    amount_paid = fields.Boolean(string="Amount Paid", default=False)
    supper_customer = fields.Boolean(string=" Is Super Customer")
    items = fields.Many2many(string="Items", comodel_name='shopping.item')
    bill_amount = fields.Float(string="Bill Amount", default=0, compute="calc_bill_amount")
    gst = fields.Float(string="GST", default=0, readonly=1, compute="calc_gst")
    total_amount = fields.Float(string="Total Amount", compute="_calc_total_amount")
    status = fields.Selection([('unpaid', 'Unpaid'), ('paid', 'Paid')], string="Status", readonly="1", default="unpaid")
    dob_day = fields.Integer(string='Day of Birth', compute='_compute_dob_day', store=True)
    dob_month = fields.Integer(string='Month of Birth', compute='_compute_dob_month', store=True)
    super_customer_count = fields.Integer(compute="calc_count_super_costomer")


    @api.depends('dob')
    def _compute_dob_day(self):
        # This code is for calculating date from dob which we use in cron method temp_method
        for rec in self:
            if rec.dob:
                rec.dob_day = rec.dob.day
            else:
                rec.dob_day = False

    @api.depends('dob')
    def _compute_dob_month(self):
        # This code is for calculating month from dob which we use in cron method temp_method
        for rec in self:
            if rec.dob:
                rec.dob_month = rec.dob.month
            else:
                rec.dob_month = False

    @api.model
    def temp_method(self):
        today_time = datetime.today()
        customer_with_birthday = self.search([('dob_day', '=', today_time.day), ('dob_month', '=', today_time.month)])
        for rec in customer_with_birthday:
            print("Happy birthday ", rec.name)




    def print_excel(self):
        # fileName = self.name
        # workbook = xlwt.Workbook(encoding='utf-8')
        # sheet1 = workbook.add_sheet('customer', cell_overwrite_ok=True)
        # format1 = xlwt.easyxf()
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        sheet = workbook.add_worksheet('Transactions')

        bold_format = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 10, 'valign': 'vcenter', 'bg_color': '#f2eee4',
             'border': True})
        normal_format = workbook.add_format({'text_wrap': True, 'align': 'center', 'valign': 'top'})
        date_format = workbook.add_format({'num_format': 'dd/mm/yy', 'align': 'center'})
        sheet.set_column('A:G', 15)  # Adjust the width as needed
        # Set row height
        sheet.set_default_row(30)  # Adjust the height as needed
        row = 1
        col = 0

        # Write headers with bold format
        sheet.write('A1', 'Customer Name', bold_format)
        sheet.write('B1', 'Customer ID', bold_format)
        sheet.write('C1', 'Shopping Date', bold_format)
        sheet.write('D1', 'Billing Counter', bold_format)
        sheet.write('E1', 'Bill Amount', bold_format)
        sheet.write('F1', 'GST', bold_format)
        sheet.write('G1', 'Total Amount', bold_format)

        sheet.write(row, col, self.name, normal_format)
        sheet.write(row, col + 1, self.cus_id, date_format)
        sheet.write(row, col + 2, self.shopping_date, normal_format)
        sheet.write(row, col + 3, self.billing_counter, normal_format)
        sheet.write(row, col + 4, self.bill_amount, normal_format)
        sheet.write(row, col + 5, self.gst, normal_format)
        sheet.write(row, col + 6, self.total_amount, normal_format)

        workbook.close()
        output.seek(0)

        # Encode the file to base64
        excel_file = base64.b64encode(output.read())
        output.close()

        # Create an attachment
        attachment = self.env['ir.attachment'].create({
            'name': f'{self.name}_report.xlsx',
            'type': 'binary',
            'datas': excel_file,
            'res_model': 'bank.transaction',
            'res_id': self.id,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }

    def _get_customer_information(self):
        # Implement the logic to retrieve customer information here
        return {'name': self.name}


    def send_email(self):
        # template_id = self.env.ref('school.mail_template_blog')  # Replace 'your_module.email_template_id' with the actual ID of your email template
        # template_id.send_mail(self.id, force_send=True)
        # self.order_line._validate_analytic_distribution()
        lang = self.env.context.get('lang')
        mail_template = self.env.ref('shopping_mall.mail_template_shopping_customer_id')

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



    @api.onchange('amount_paid')
    def change_status_bar(self):
        for rec in self:
            if rec.amount_paid:
                rec.status = 'paid'
            else:
                rec.status = 'unpaid'


    @api.depends('items.price')
    def calc_bill_amount(self):
        for cus in self:
            cus.bill_amount = sum(cus.items.mapped('price'))

    def calc_count_super_costomer(self):
        for rec in self:
            rec.super_customer_count = self.env['shopping.customer'].search_count(
                [('cus_id', '=', self.cus_id)])

    def get_super_customers(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Super Customer',
            'view_mode': 'tree,form',
            'res_model': 'shopping.customer',
            'domain': [('cus_id', '=', self.cus_id)],
            'context': "{'create': False}"
        }

    @api.model
    def create(self, vals):

        # Code for ir sequence
        if vals.get('cus_id', _('New')) == _('New'):
            vals['cus_id'] = self.env['ir.sequence'].next_by_code('customer.sequence') or _('New')



        res = super(customer, self).create(vals)

        if res.email:
            template = self.env.ref('shopping_mall.template_shopping_customer_mail_id')
            template.send_mail(res.id, force_send=True)

        # code to create new record in paid bills
        if vals.get('amount_paid'):
            record = self.env['shopping.paidbill'].create({
                'name': vals.get('name'),
                'cus_id': vals.get('cus_id'),
                'payment_status': 'Paid',
                'shopping_date': vals.get('shopping_date'),
                'total_payment': vals.get('total_amount')
            })
        # Code to create new record in unpaid bills
        else:
            record = self.env['shopping.unpaidbill'].create({
                'name': vals.get('name'),
                'cus_id': vals.get('cus_id'),
                'payment_status': 'Unpaid',
                'shopping_date': vals.get('shopping_date'),
                'total_payment': vals.get('total_amount')
            })

        return res

    @api.depends('bill_amount')
    def calc_gst(self):
        for rec in self:
            if rec.bill_amount >= 1000:
                rec.gst += (18 * rec.bill_amount) / 100
            else:
                rec.gst = 0

    @api.depends('bill_amount', 'gst')
    def _calc_total_amount(self):
        total = 0
        for rec in self:
            total = rec.bill_amount + rec.gst
            rec.total_amount = total

    # unlink code
    def unlink(self):
        print("HI 1")
        temp_id = self.cus_id
        if self.amount_paid:
            record = self.env['shopping.paidbill'].search([('cus_id', '=', temp_id)])
            for rec in record:
                rec.unlink()
        else:
            record = self.env['shopping.unpaidbill'].search([('cus_id', '=', temp_id)])
            for rec in record:
                rec.unlink()

        return super(customer, self).unlink()
