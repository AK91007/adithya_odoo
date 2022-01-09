from odoo import fields,models,api

class CreateSoldInvoice(models.TransientModel):
	_name='create.sold.invoice'
	_description='Create Sold Invoice'

	partner_id=fields.Many2one('res.partner')
	charge=fields.Integer('Charge for Name Change',default=500)

	def make_invoice(self):
		print("\n\n Make Invoice Method Called")
		print("\n\n", self.partner_id.name)
		print(self._context.get('active_ids',[]))
		property=self.env['estate.property'].browse(self._context.get('active_ids',[]))
		if property:
			property.state='sold'

			journal=self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
			vals['partner_id'] = self.partner_id #record.buyer_id.id
			vals['move_type'] = 'out_invoice'
			vals['journal_id'] = journal.id
			vals['invoice_line_ids'] = [(0,0,{'name':property.name,'quantity':1,'price_unit':property.selling_price}),
										(0,0,{'name':'Extra Fees','quantity':1,'price_unit':0.06*property.selling_price}),
										(0,0,{'name':'Administrative Fees','quantity':1,'price_unit':1000}),
										(0,0,{'name':'Name Change Charges','quantity':1,'price_unit':self.charge})
										]
			
			self.env['account.move'].create(vals)