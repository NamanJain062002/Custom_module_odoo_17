from odoo import fields, models, api, _


class review(models.Model):
    _name = 'shopping.review'
    _description = 'Review of products'

    stars = fields.Selection([('1 star', '1 Star'), ('2 star', '2 Star'), ('3 star', '3 Star'), ('4 star', '4 Star'), ('5 star', '5 Star')], string="Rating")
    review = fields.Char(string="Review")

    def submit(self):
        review_model = self.env['shopping.reviewrecord']
        # item_model = self.env['shopping.item']

        review_model.create({
            'item_name': 'Item Name',
            'item_id': 'Item ID',
            'rating': self.stars,
            'reviews': self.review
        })
