
from odoo import api, fields, models

class MyTest(models.Model):
	_name = 'my.test'
	_description = 'My Test'

	name = fields.Char()
	address = fields.Char()
	pincode = fields.Integer()


class MyInherit(models.Model):
	_inherit = 'my.test'

	country = fields.Char()
	state = fields.Char()
	city = fields.Char()

class MyInherit2(models.Model):
	_name = 'my_inherit_2'
	_inherit = 'my.test'

	pancard = fields.Char()
	aadhar = fields.Char()

class BankProperty(models.Model):
	_inherit = 'estate.property'

	bank_name = fields.Char()
	bank_interest = fields.Float()