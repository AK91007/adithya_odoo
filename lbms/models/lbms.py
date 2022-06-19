from odoo import api,models,fields,_
import datetime
from datetime import timedelta

class BookGenre(models.Model):
	_name='book.genre'
	_description='Defines the category of the book'
	_rec_name='genre_master'

	genre_master=fields.Char(string='Genre',default=None,copy=False)

class BookGenre(models.Model):
	_name='book.publisher'
	_description='Defines the publisher of the book'
	_rec_name='publisher_master'

	publisher_master=fields.Char(string='Publisher',default=None,copy=False)

class BookLocation(models.Model):
	_name='book.location'
	_description='Designated place in the library for the book'
	_rec_name='location_master'

	location_master=fields.Char(string='Book Location',default=None,copy=False,store=True)
	parent_location=fields.Many2one('book.location',default=None,copy=False,store=True)
	
	location_complete_name=fields.Char(string='Full Name',compute='_get_location_name')
	


	@api.depends('location_master','parent_location')
	def _get_location_name(self):
		for rec in self:
			if rec.parent_location is not set:
				# rec.location_complete_name='%s/%s'%(rec.parent_location.location_master,rec.location_master)
				
				rec.location_complete_name="{}/{}".format(rec.parent_location.location_master,rec.location_master)
				
			else:
				# rec.location_complete_name='%s'%(rec.location_master)
				rec.location_complete_name="{}{}".format(None,rec.location_master)
				

			return rec.location_complete_name
				
				
class LibraryManagement(models.Model):
	_name='library.management'
	_description='Used to manage library operations'
	_rec_name='book_name'

	book_name=fields.Char(string='Book Name',copy=False,default=None)
	author_name=fields.Char(string='Author',copy=False,default=None)
	book_genre=fields.Many2one('book.genre',string='Genre',copy=False,default=None)
	book_publisher=fields.Many2one('book.publisher',string='Publisher',copy=False,default=None)
	publication_date=fields.Date(string='Published Date',copy=False,default=None)
	image=fields.Image()
	book_availability=fields.Boolean(string="Available",copy=False)



class LibraryTrnSequence(models.Model):
	_name='library.sequence'
	_description='Model to define library transactions sequence'
	_rec_name='transaction_sequence'

	transaction_sequence=fields.Many2one('ir.sequence',string='Transaction Sequence',copy=False,store=True)
	
class LibraryTransactions(models.Model):
	_name='library.transaction'
	_description='Model to manage the library transactions'


	name=fields.Char(string='Name',copy=False,index=True,default=lambda self:_('New'))
	borrower_name=fields.Many2one('res.partner',string='Borrower')
	borrowed_book=fields.Many2one('library.management',string='Borrowed Book')
	date_issue=fields.Datetime(string='Issue Date',copy=False,default=None)
	date_expected=fields.Datetime(string='Tentative Return',copy=False,default=None)
	date_return=fields.Datetime(string='Return Date',copy=False,default=None)
	

	def action_lost(self):
		for rec in self:
			if rec.borrowed_book.book_availability==True:
				rec.borrowed_book.book_availability==False
	def action_issue():
		pass
	def action_return():
		pass


	@api.model
	def create(self,vals):
		if vals.get('name',_('New'))==_('New'):
			# vals['name']=self.env['library.sequence'].next_by_id()
			vals['name']=self.env['ir.sequence'].next_by_code('library.trn.sequence')
		result=super(LibraryTransactions,self).create(vals)
		return result

