from odoo import models, fields

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





