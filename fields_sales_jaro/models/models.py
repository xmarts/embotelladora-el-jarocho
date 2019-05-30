# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class AddFIeldsSalesJaro(models.Model):

	_inherit = 'sale.order'

	number_order = fields.Char( string = "Numero de orden" )

	number_appoi = fields.Char( string = "Numero de cita" )

	date_of_deli = fields.Date( string = "Fecha de entrega" )

	folio_note_entry = fields.Char( string = "Folio de nota de entrada" )

	field_add_capture = fields.Char( string = "Campo addicional para capturar" )

class AddFieldManySales(models.Model):

	_inherit = 'account.invoice'

	field_sales = fields.Many2one( 'sale.order', string = "Campo ventas" , compute = "getValue", readonly = True )

	field_test = fields.Char( string = "Campo de prueba", readonly = True )

	def getValue(self):
		search = self.env['sale.order'].search([('name', '=', self.origin)], limit = 1)
		self.field_sales = search.id

class AddFIeldsContacts(models.Model):

	_inherit = 'res.partner'

	number_store = fields.Char( string = "Numero de tienda" )