from odoo import fields, api, models
from odoo.exceptions import UserError, ValidationError

class ResPartner(models.Model):
	_inherit = 'res.partner'

	offer_ids = fields.One2many('estate.property.offer','offer_partner_id')