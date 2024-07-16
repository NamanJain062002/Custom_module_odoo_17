from odoo import fields, models, api


class StockPicking(models.Model):
   _inherit = "sale.order"
   @api.model
   def _get_view(self, view_id=None, view_type='form', **options):
       arch, view = super()._get_view(view_id, view_type, **options)
       print("arch>>>>>>>>", arch)
       print("view>>>>>>>>", view)
       active_company = self.env.user
       user_has_group = active_company.has_group('sales_approval.group_sale_approve_button_access')
       if view_type == 'form' and not(user_has_group):
               for node in arch.xpath("//field"):
                   node.set('readonly', '1')
       return arch, view
