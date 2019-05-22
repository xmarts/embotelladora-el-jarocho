# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class AddFIeldsSalesJaro(models.Model):

	_inherit = 'sale.order'

	number_order = fields.Char( string = "Numero de orden" )
	number_appoi = fields.Char( string = "Numero de cita" )
	date_of_deli = fields.Date( string = "Fecha de entrega" )
