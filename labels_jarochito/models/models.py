# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class LabelsPallets(models.Model):

	_name = 'labels.pallets'

	def _name_default(self):
		cr = self.env.cr
		cr.execute('select "id" from "labels_pallets" order by "id" desc limit 1')
		id_returned = cr.fetchone()
		if id_returned == None:
			id_returned = (0,)
		text = ''
		pref = 'Etiq-'
		if((max(id_returned) + 1) < 100):
			text = pref + '00' + str(max(id_returned) + 1)
		else:
			text = pref + str(max(id_returned) + 1)
		return text

	name = fields.Char( string = 'Nombre' , readonly = True, default = _name_default )

	turn = fields.Selection( [('mat','Matutino'),('ves','Vespertino'),('noc','Nocturno')] , string = 'Turno' )

	pallet = fields.Many2one( 'pallets' , string = 'Tarima' )

	date = fields.Date( string = 'Fecha' )

class Pallets(models.Model):

	_name = 'pallets'

	pallet_name = fields.Char( string = 'Tarima' )

	_rec_name = 'pallet_name'