from odoo import models, fields

class ShoppingReport(models.Model):
    _name = 'shopping.report'
    _description = "For reports"

    signed_by = fields.Char(
        string="Signed By", copy=False)
    signed_on = fields.Datetime(
        string="Signed On", copy=False)
    origin = fields.Char(
        string="Source Document",
        help="Reference of the document that generated this sales order request")
    reference = fields.Char(
        string="Payment Ref.",
        help="The payment communication of this sale order.",
        copy=False)

    def _select(self):
        return "signed_by,signed_on,origin,reference"

    def _from(self):
        return "sale_order"

    def _query(self):
        return f"""
                SELECT {self._select()}
                FROM {self._from()}
            """

    @property
    def _table_query(self):
        return self._query()