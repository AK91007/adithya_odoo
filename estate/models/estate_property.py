from odoo import models, fields, api
import datetime

class EstatePropertyType(models.Model):
	_name = 'estate.property.type'
	_description = 'Estate Property Type'

	name = fields.Char()
class EstatePropertyTag(models.Model):
	_name = 'estate.property.tag'
	_description = 'Estate Property Tag'

	name = fields.Char()

class EstatePropertyOffer(models.Model):
	_name = 'estate.property.offer'
	_description = 'Estate Property Offer'
	_rec_name = 'property_id'
	property_id = fields.Many2one('estate.property')
	offer_partner_id = fields.Many2one('res.partner')
	offer_status = fields.Selection([('accepted','Accepted'),('refused','Refused')])
	offer_price = fields.Float()
	offer_create_date = fields.Date(default=lambda self: fields.Date.today())
	offer_validity = fields.Integer(string='Validity', default=7)
	offer_deadline = fields.Date(compute='_compute_deadline', inverse='_compute_validity')

	@api.depends('offer_create_date','offer_validity')
	def _compute_deadline(self):
		for record in self:
			record.offer_deadline = record.offer_create_date + datetime.timedelta(days = record.offer_validity)

	def _compute_validity(self):
		for record in self:
			record.offer_validity = (record.offer_deadline - record.offer_create_date).days

	
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
	image = fields.Image()
	property_type_id = fields.Many2one('estate.property.type', string = 'Property Type')
	salesman_id=fields.Many2one('res.users')
	buyer_id=fields.Many2one('res.partner')
	property_tag_id=fields.Many2many('estate.property.tag', string = 'Property Tag')
	property_offer_id = fields.One2many('estate.property.offer', 'property_id')
	total_area=fields.Integer(compute='_compute_area', inverse='_inverse_area')
	best_price = fields.Float(compute='_compute_best_price')

	@api.onchange('garden')
	def _onchange_garden(self):
		for record in self:
			if record.garden:
				record.garden_area = 100
				record.garden_orientation = 'north'
			else:
				record.garden_area = 0
				record.garden_orientation = None

	@api.depends('property_offer_id.offer_price')
	def _compute_best_price(self):
		for record in self: #This loop is required to loop through the record set of properties
			max_price=0
			for offer in record.property_offer_id:
				if offer.offer_price > max_price:
					max_price = offer.offer_price
			record.best_price = max_price

	@api.depends('living_area','garden_area')
	def _compute_area(self):
		for record in self:
			record.total_area=record.living_area+record.garden_area

	def _inverse_area(self):
		for record in self:
			record.living_area = record.garden_area = record.total_area/2




