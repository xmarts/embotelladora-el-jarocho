# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openerp.exceptions import UserError, RedirectWarning, ValidationError

class AddClaseProduct(models.Model):

	_name = 'class.product'

	clase = fields.Char( string = 'Clase' )

	_rec_name = 'clase'

class AddPresentationProduct(models.Model):

	_name = 'presentation.product'

	presentation = fields.Char( string = 'Presentación' )

	_rec_name = 'presentation'

class AddCodeTypeContainerProduct(models.Model):

	_name = 'typecontainer.product'

	code = fields.Char( string = 'Cod. Tipo de envase' )
	
	_rec_name = 'code'

class AddTasteProduct(models.Model):

	_name = 'taste.product'

	taste = fields.Char( string = 'Sabor' )

	_rec_name = 'taste'

class AddCodeBrandProduct(models.Model):

	_name = 'brand.product'

	brand = fields.Char( string = 'Código de marca' )

	_rec_name = 'brand'

class AddCampsProductPage(models.Model):

	_inherit = 'product.template'

	#-- Relación para agregar clases al producto
	clase_prod = fields.Many2one( 'class.product' , string = 'Clase' )
	
	#-- Relación para agregar una presentación al producto
	presentation_prod = fields.Many2one( 'presentation.product' , string = 'Presentación' )

	#-- Relación para gregar un código al envase del producto 
	code_container_prod = fields.Many2one( 'typecontainer.product' , string = 'Cod. Tipo de envase' )

	# -- Relación para agregar un sabor al producto 
	taste_product = fields.Many2one( 'taste.product' , string = 'Sabor' )

	# -- Relación para gregar un código a la marca del producto
	brand_product = fields.Many2one( 'brand.product' , string = 'Código de marca' )

class AddRateAddressDelivery(models.Model):

	_inherit = 'res.partner'

	rate_address = fields.Many2one( 'product.pricelist', string = 'Tarifa' )

	most_ieps = fields.Boolean( string = 'Mostrar IEPS' )

class OnchangeDirectionFacture(models.Model):

	_inherit = 'sale.order'

	@api.onchange('partner_shipping_id')
	def changeDirFac(self):
		if self.partner_shipping_id:
			self.pricelist_id = self.partner_shipping_id.rate_address.id

'''class ChangeFunctionAmount(models.Model):

	_inherit = 'account.invoice'				

	@api.one
	@api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'tax_line_ids.amount_rounding',
		'currency_id', 'company_id', 'date_invoice', 'type')

	def _compute_amount(self):

		round_curr = self.currency_id.round
		self.amount_untaxed = sum(line.price_subtotal for line in self.invoice_line_ids)

		if self.partner_id.most_ieps == True:
			self.amount_tax = sum(round_curr(line.amount_total) for line in self.tax_line_ids)
		else:
			for l in self.tax_line_ids:
				for n in l.tax_id:	
					for f in n.tag_ids:
						if f.name == 'IEPS':
							rest = round_curr(l.amount)
							self.amount_tax = sum(round_curr(line.amount_total) for line in self.tax_line_ids) - rest
						else:
							rest = 2
							self.amount_tax = l.amount_total

		self.amount_total = self.amount_untaxed + self.amount_tax
		amount_total_company_signed = self.amount_total
		amount_untaxed_signed = self.amount_untaxed
		if self.currency_id and self.company_id and self.currency_id != self.company_id.currency_id:
			currency_id = self.currency_id
			amount_total_company_signed = currency_id._convert(self.amount_total, self.company_id.currency_id, self.company_id, self.date_invoice or fields.Date.today())
			amount_untaxed_signed = currency_id._convert(self.amount_untaxed, self.company_id.currency_id, self.company_id, self.date_invoice or fields.Date.today())
		sign = self.type in ['in_refund', 'out_refund'] and -1 or 1
		self.amount_total_company_signed = amount_total_company_signed * sign
		self.amount_total_signed = self.amount_total * sign
		self.amount_untaxed_signed = amount_untaxed_signed * sign

class IepsInvoiceLine(models.Model):

	_inherit = 'account.invoice.line'

	@api.onchange('invoice_line_tax_ids')
	def ChangeTax(self):
		if self.invoice_id.partner_id.most_ieps == False:
			for lines in self.invoice_id.invoice_line_ids:
				for tag in self.invoice_line_tax_ids:
					if tag.tag_ids.name == 'IEPS':
						value_prod = lines.product_id.lst_price
						percentaje = tag.amount
						operation = ( value_prod * percentaje ) / 100
						self.price_unit = value_prod + operation
					else:
						self.price_unit = lines.product_id.lst_price'''


class IepsOrderLine(models.Model):

	_inherit = 'sale.order.line'

	@api.onchange('tax_id')
	def ChangeTax(self):
		if self.order_id.partner_id.most_ieps == False:
			for line in self.order_id.order_line:
				for tax in line.tax_id:
					for tag in tax.tag_ids:
						if tag.name == 'IEPS':
							line.price_unit = line.product_id.lst_price + tax.amount

	@api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
	def _compute_amount(self):
		"""
		Compute the amounts of the SO line.
		"""	

		for line in self:
			price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
			taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
			amount_env = 0
			for tax in line.tax_id:
				for tag in tax.tag_ids:
					if tag.name == 'IEPS':
						amount_env = tax.amount
			'''line.update({
				'price_tax': amount_env,
				'price_total': taxes['total_included'],
				'price_subtotal': taxes['total_excluded'],
			})'''

			line.update({
				'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])) - amount_env,
				'price_total': taxes['total_included'],
				'price_subtotal': taxes['total_excluded'],
			})

			'''price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
			taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
			line.update({
				'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
				'price_total': taxes['total_included'],
				'price_subtotal': taxes['total_excluded'],
			})'''

'''class IepsSales(models.Model):

	_inherit = 'sale.order'

	@api.depends('order_line.price_total')
	def _amount_all(self):
		"""
		Compute the total amounts of the SO.
		"""
		for order in self:
			amount_untaxed = amount_tax = 0.0
			for line in order.order_line:
				amount_untaxed += line.price_subtotal
				amount_tax += line.price_tax

			order.update({
				'amount_untaxed': order.pricelist_id.currency_id.round(amount_untaxed),
				'amount_tax': order.pricelist_id.currency_id.round(amount_tax),
				'amount_total': amount_untaxed + amount_tax,
			})
'''
