from odoo import models, fields

class demoWizard(models.Model):
    _name = 'demo.demo'
    _description = "Example model of wizard"
    # sub = fields.Selection([('payment', 'Payement'),('driver', 'Driver'), ('location', 'Location'),('vehicle', 'Vehicle')], string="Related to")
    sub = fields.Char(string="Subject")
    query = fields.Char(string="Query")

    def submit(self):
        pass
