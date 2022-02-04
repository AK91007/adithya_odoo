from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class EstateProperty(models.Model):
	_inherit = 'estate.property'

	def action_sold(self):
		super(EstateProperty,self).action_sold()
		print("\n \n Sold button clicked")

		for record in self:
			vals={}
			journal=self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
			vals['partner_id'] = record.buyer_id.id
			vals['move_type'] = 'out_invoice'
			vals['journal_id'] = journal.id
			vals['invoice_line_ids'] = [(0,0,{'name':record.name,'quantity':1,'price_unit':record.selling_price}),
										(0,0,{'name':'Extra Fees','quantity':1,'price_unit':0.06*record.selling_price}),
										(0,0,{'name':'Administrative Fees','quantity':1,'price_unit':1000})
										]
			
			self.env['account.move'].create(vals)