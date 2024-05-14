from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class driver(models.Model):
    _name = "vehicle.driver"
    _description = "Information about drivers"


    name = fields.Char(string="Driver Name")
    photo = fields.Binary(string="Profile Photo", attachment=True)
    dri_id = fields.Integer(string="Driver ID")
    allocated_fourwheeler_ids = fields.One2many('vehicle.fourwheeler', 'fourwheeler_driver_name_id',string="Four Wheelers")
    allocated_twowheeler_ids = fields.One2many("vehicle.twowheeler", 'driver_name_id',string="Two Wheeler")
    age = fields.Integer(string="Age")
    address = fields.Char(string="Address")
    _sql_constraints = [('unique_id', 'UNIQUE(dri_id)', 'driver id must be unique')]

    @api.model
    def create(self, vals):
        rec = super(driver, self).create(vals)
        print("Create method is triggered", vals)
        return rec

    def write(self, vals):
        print("write method is triggered", vals)
        rec = super().search([('age',">",30)])
        browse_rec = self.browse([12,1])
        for i in browse_rec:
            print("Browse records>>>>>>>",i.name)
        print("REC--------", rec)
        for record in self:
            print("Names-----------", record.name)
        return super(driver, self).write(vals),rec

    def unlink(self):
      for record in self:
        if record.dri_id == 123:
            raise ValidationError(_("You can not delete driver with premium id 123"))
        else:
            print("unlink method is triggered....", record.name)
        return super(driver,self).unlink()


    def copy(self,default=None):
        if self.dri_id == 123:
            raise ValidationError(_("Can't duplicate this record"))
        return super(driver,self).copy(default)



    @api.onchange('age')
    def is_valid(self):
        if self.age and self.age <= 18:
            raise ValidationError("The driver age is not valid")

    def ReadGroup(self):
        print("read group called>>>")
        order_totals = self.read_group([('age', '>', 20)], ['name', 'dri_id'], ['age'])
        print(order_totals)

    def name_get(self):
        result = []
        for rec in self:
            record = rec.name+' '+rec.dri_id
            result.append((rec.id, record))
        return result


