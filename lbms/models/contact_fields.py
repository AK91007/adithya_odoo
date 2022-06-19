#This file defines the fields in the contact module related to LBMS
from odoo import fields,models,api

class LibraryContacts(models.Model):
	_inherit='res.partner'

	library_member = fields.Many2one('library.contact.type',string="Library Member",copy=False,default=None)
	

class LibraryContactType(models.Model):
	_name='library.contact.type'
	_description='contact_type_definition'
	_rec_name='library_contact_type'

	library_contact_type = fields.Char(string="Contact Type",copy=False,default=None)
	contact_type_description = fields.Char(string="Contact Description",default=None,copy=False)