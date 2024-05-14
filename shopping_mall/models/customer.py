from odoo import models, fields, api, _


class customer(models.Model):
    _name = 'shopping.customer'
    _description = 'information about customers'

    name = fields.Char(string="Name", required=1)
    cus_id = fields.Char(string="Customer ID", readonly=1)
    shopping_date = fields.Date(string="Shopping Date")
    billing_counter = fields.Selection(
        [('counter 1', 'Counter 1'), ('counter 2', 'Counter 2'), ('counter 3', 'Counter 3'), ('counter 4', 'Counter 4'),
         ('counter 5', 'Counter 5'), ], string="Billing Counter")
    amount_paid = fields.Boolean(string="Amount Paid")
    supper_customer = fields.Boolean(string=" Is Super Customer")
    items = fields.One2many(string="Items", comodel_name='shopping.item', inverse_name='item_name')
    bill_amount = fields.Float(string="Bill Amount", default=0, compute="calc_bill_amount")
    gst = fields.Float(string="GST", default=0, readonly=1, compute="calc_gst")
    total_amount = fields.Float(string="Total Amount", compute="_calc_total_amount")
    status = fields.Selection([('unpaid', 'Unpaid'), ('paid', 'Paid')], string="Status", readonly="1", default="unpaid")


    super_customer_count = fields.Integer(compute="calc_count_super_costomer")


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

        # code to create new record in paid bills

        res = super(customer, self).create(vals)
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
        print(temp_id)
        if self.amount_paid:
            record = self.env['shopping.paidbill'].search([('cus_id', '=', temp_id)])
            for rec in record:
                rec.unlink()
        else:
            record = self.env['shopping.unpaidbill'].search([('cus_id', '=', temp_id)])
            for rec in record:
                rec.unlink()

        return super(customer, self).unlink()
