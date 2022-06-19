{
	'name':'Library Management',
	'description':'This module is built to manage the library operations',
	'category':'all',
	'version': '14.0.1',
	'application': True,
	'depends':['base','contacts'],
	'author': "Adithya",
	'data':[
	'security/ir.model.access.csv',
	'views/contact_fields_menus.xml',
	'views/contact_fields_view.xml',
	'views/lbms_menus.xml',
	'views/lbms_views.xml'
	]

}