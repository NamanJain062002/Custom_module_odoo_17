import uuid

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrderinherit(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[
        ('to_approve', 'To Approve'),
    ])


    @api.model
    def create(self, vals):
        res = super(SaleOrderinherit, self).create(vals)

        if res.partner_id.name == 'ABC':
            res.with_context(Name='Naman').sale_approval()
        return res



    def sale_approval(self):
        # token_model = self.env['ir.attachment']
        # token_model.generate_access_token()
        # self.env.context.get('active_id')
        print(str(uuid.uuid4()))
        active_id_value = self.env.context.get('Name')
        show_context = self.env.context
        print(show_context)
        # sale_object = self.env['sale.order'].browse(active_id_value)
        # # print(sale_object)
        # sale_object.created_by = "NAMAN"
        self.created_by = active_id_value
        self.state = 'sale'

    def action_confirm(self):
        # total = self.amount_total
        param_obj = self.env['ir.config_parameter'].sudo()
        limit = param_obj.get_param('sale_limit')

        # print(type(total))
        # print(type(limit))
        to_approve_orders = None
        for order in self:
            if order.amount_total > float(limit):
                order.state = 'to_approve'

            else:
                # Proceed with the default action_confirm logic for other cases
                super(SaleOrderinherit, order).action_confirm()

        return True



class ResConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_limit = fields.Float(
        string="Sale Limit",
        config_parameter='sale_limit'
    )

    @api.constrains('sale_limit')
    def chk_limit(self):
        for limit in self:
            if limit.sale_limit <= 0:
                raise ValidationError("The sale limit can only be in positive")



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_image = fields.Image(string="Image", related="product_template_id.image_1920")

class StockPicking(models.Model):
    _inherit = 'stock.move'

    product_stock = fields.Image(string="Image", related="product_id.image_1920")

class AccountMove(models.Model):
    _inherit = 'account.move.line'

    account_item_image = fields.Image(string="Image", related="product_id.image_1920")




