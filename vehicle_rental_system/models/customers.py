from odoo import models, fields, api, _


class customer(models.Model):
    _name = 'vehicle.customer'
    _description = 'information about customer'

    name = fields.Char(string="Customer Name")
    cus_id = fields.Char(string="Customer ID", readonly=True, copy=False)
    is_premium = fields.Boolean(string="Is Premium", default=False)
    location = fields.Many2one('vehicle.location', string="Location")
    vehicle_type = fields.Selection([('two wheeler', 'Two Wheeler'), ('four wheeler', 'Four Wheeler')],
                                    string="Vehicle Type", required=True)
    rent_date = fields.Datetime(string="Rent Date")
    return_date = fields.Datetime(string="Return date")
    discount = fields.Boolean(string="Discount Available", readonly=1)
    total_days = fields.Integer(string="Total Days", compute="calc_days")

    is_premium_list = fields.Integer(string='is_premium_list', compute='_compute_listed_property_count')
    customer_with_fourwheeler = fields.Integer(string="Customer With Fourwheeler", compute="calc_customer_with_fourwheeler")



    @api.depends('vehicle_type')
    def calc_customer_with_fourwheeler(self):
        self.customer_with_fourwheeler = self.env['vehicle.customer'].search_count([('vehicle_type', '=', 'four wheeler')])

    def get_four_wheeler(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Customer With Fourwheeler',
            'res_model': 'vehicle.customer',
            'view_mode': 'tree,form',
            'target': 'new',
            'domain': [('vehicle_type', '=', 'four wheeler')]
        }

    def action_order_list(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Is Premium LIST',
            'res_model': 'vehicle.customer',
            'view_mode': 'tree,form',
            'target': 'new',
            'domain': [('is_premium', '=', 'True')]
        }

    @api.depends('is_premium')
    def _compute_listed_property_count(self):
        for record in self:
            listed_premium_count = self.env['vehicle.customer'].search_count(
                [('is_premium', '=', 'True')])
            record.is_premium_list = listed_premium_count

    @api.model
    def create(self, vals):
        res = super(customer, self).create(vals)

        if 'is_premium' in vals and vals['is_premium']:
            # If the customer is premium, create a record in PremiumCustomer model
            self.env['vehicle.premium'].create({
                'name': vals.get('name'),
                'cus_id': vals.get('cus_id'),
                'vehicle_type': vals.get('vehicle_type'),
                'rent_date': vals.get('rent_date'),
                'return_date': vals.get('return_date')
            })
        return res

    @api.model
    def create(self, vals):
        if vals.get('cus_id', _('New')) == _('New'):
            vals['cus_id'] = self.env['ir.sequence'].next_by_code('customer.sequence') or _('New')
        return super(customer, self).create(vals)

    @api.depends('rent_date', 'return_date')
    def calc_days(self):
        for record in self:
            if record.rent_date and record.return_date:
                start = fields.Datetime.from_string(record.rent_date)
                end = fields.Datetime.from_string(record.return_date)

                delta = end - start
                record.total_days = delta.days

            else:
                record.total_days = 0

    @api.onchange('is_premium')
    def toggle_premium(self):
        if self.is_premium == True:
            self.env['vehicle.premium'].create({
                'name': self.name,
                'cus_id': self.cus_id,
                'vehicle_type': self.vehicle_type,
                'rent_date': self.rent_date,
                'return_date': self.return_date,
                'total_days': self.total_days
            })

    def unlink(self):
        self.ensure_one()

        return super(customer, self).unlink()
