from odoo import models, fields

class EstateProperty(models.Model):
	_name = 'estate.property'
	_description = 'Test Model'

	name = fields.Char(string='Title', default='Unknown', required=True)
	description = fields.Text()
	postcode = fields.Char()
	date_availability = fields.Date(default = lambda self: fields.Datetime.now())
	expected_price = fields.Float()
	selling_price = fields.Float()
	bedrooms = fields.Integer()
	living_area = fields.Integer()
	facades = fields.Integer()
	garage = fields.Boolean()
	garden = fields.Boolean()
	garden_area = fields.Integer()
	garden_orientation = fields.Selection([('north','North'),('south','South'),('west','West'),('east','East')])
	active = fields.Boolean()

