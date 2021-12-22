from odoo import models,fields

class BookGenre(models.Model):
	_name = 'book.genre'
	_description = 'Book Genre'

	name = fields.Char()

class BookDepartment(models.Model):
	_name = 'book.department'
	_description = 'Book Department'

	name = fields.Char()

class BookWriter(models.Model):
	_name = 'book.writer'
	_description = 'Book Writer'

	name = fields.Char()

class Book(models.Model):
	_name = 'book'
	_rec_name='book_name'
	_sql_constrints=[('isbn_unique','unique(book_isbn)','Duplicate ISBN not allowed')]
	book_name=fields.Char(string='Book Name', default='Book Name', required=True)
	book_author=fields.Char(string='Author', default='Author Name', required=True)
	book_category=fields.Selection([('fiction','Fiction'),('thriller','Thriller'),('biography','Biography'),('comics','Comics')])
	book_price=fields.Float(string='Price')
	book_publication=fields.Char(string='Published By')
	book_image=fields.Image()
	book_genre_id=fields.Many2one('book.genre', string='Book Genre')
	book_location_id=fields.Many2one('stock.location', string='Book Location')
	book_department_id=fields.Many2one('book.department', string='Book Department')
	book_writer_id=fields.Many2many('book.writer', string='Book Writers')
	book_isbn=fields.Char(string='ISBN', default='00000')
	book_barcode=fields.Integer(string='Barcode')
	