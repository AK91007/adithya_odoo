from odoo import models,fields

class Book(models.Model):
	_name = 'book'
	_rec_name='book_name'
	book_name=fields.Char(string='Book Name', default='Book Name', required=True)
	book_author=fields.Char(string='Author', default='Author Name', required=True)
	book_category=fields.Selection([('fiction','Fiction'),('thriller','Thriller'),('biography','Biography'),('comics','Comics')])
	book_price=fields.Float(string='Price')
	book_publication=fields.Char(string='Published By')
	book_image=fields.Image()
	