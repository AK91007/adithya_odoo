{
	'name': 'Real Estate',
	'version': '14.0.1',
	'application': True,
	'depends':['base','stock'],
	'author': "Adithya",
	'category': "Sales",
	'data': [
		'security/ir.model.access.csv',
		'views/estate_menus.xml',
		'wizard/create_sold_invoice_view.xml',
		'views/estate_property_views.xml'
	]
	

}