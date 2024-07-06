from odoo import models, fields, api

class SaleOrderinherit(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[
        ('to_approve', 'To Approve'),
    ])

    def sale_approval(self):
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

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_image = fields.Image(string="Image", related="product_template_id.image_1920")

class StockPicking(models.Model):
    _inherit = 'stock.move'

    product_stock = fields.Image(string="Image", related="product_id.image_1920")

class AccountMove(models.Model):
    _inherit = 'account.move.line'

    account_item_image = fields.Image(string="Image", related="product_id.image_1920")




