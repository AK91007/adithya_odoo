from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class EstateProperty(models.Model):
	_inherit = 'estate.property'

	def action_sold(self):
		print("\n \n Sold button clicked")
