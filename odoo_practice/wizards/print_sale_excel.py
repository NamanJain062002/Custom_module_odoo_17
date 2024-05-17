import base64
import io
import xlsxwriter

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PrintSaleExcel(models.TransientModel):
    _name = 'sale.excel'
    _description = "Sale Excel Report Wizard"

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)

    def submit(self):
        start = self.start_date
        end = self.end_date
        if start > end:
            raise ValidationError('Start date cannot be greater than end date.')

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        sheet = workbook.add_worksheet('Transactions')

        bold_format = workbook.add_format(
            {'bold': True, 'align': 'center', 'font_size': 12, 'valign': 'center', 'bg_color': '#00008B', 'color': '#FFFFFF',
             'border': True})
        normal_format = workbook.add_format({'text_wrap': True, 'valign': 'center', 'align': 'center', 'bg_color': '#ADD8E6', 'border': True, 'font_size': 10})
        number_format = workbook.add_format({'text_wrap': True, 'valign': 'center', 'align': 'right', 'bg_color': '#ADD8E6', 'border': True, 'font_size': 10})
        date_format = workbook.add_format({'num_format': 'dd/mm/yy', 'align': 'center', 'valign': 'center', 'bg_color': '#ADD8E6', 'border': True, 'font_size': 10})
        dollar_format = workbook.add_format({'num_format': '$#,##0.00', 'text_wrap': True, 'valign': 'center', 'align': 'right', 'bg_color': '#ADD8E6', 'border': True, 'font_size': 10})
        sheet.set_column('A:G', 18)  # Adjust the width as needed
        sheet.set_default_row(30)  # Adjust the height as needed
        row = 1
        col = 0
        data = self.env['sale.order'].search([('date_order', '>=', start), ('date_order', '<=', end)])

        # Write headers with bold format
        sheet.write('A1', 'Number', bold_format)
        sheet.write('B1', 'Date', bold_format)
        sheet.write('C1', 'Customer', bold_format)
        sheet.write('D1', 'Sale Person', bold_format)
        sheet.write('E1', 'Status', bold_format)
        sheet.write('F1', 'Total', bold_format)

        for rec in data:
            sheet.write(row, col, rec.name or '', number_format)
            sheet.write(row, col + 1, rec.date_order.strftime('%Y-%m-%d') if rec.date_order else '', date_format)
            sheet.write(row, col + 2, rec.partner_id.name or '', normal_format)
            sheet.write(row, col + 3, rec.user_id.name or '', normal_format)
            sheet.write(row, col + 4, rec.invoice_status or '', normal_format)
            sheet.write(row, col + 5, rec.amount_total or 0.0, dollar_format)
            row += 1

        workbook.close()
        output.seek(0)

        # Create an attachment
        attachment = self.env['ir.attachment'].create({
            'name': f'Sale_Order_report.xlsx',
            'type': 'binary',
            'datas': base64.b64encode(output.getvalue()),
            'res_model': 'sale.excel',
            'res_id': self.id,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        })

        # Return the action to open/download the attachment
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'self',
        }
