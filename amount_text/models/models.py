# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from . import amount_to_text

class AddFieldAmountText(models.Model):
	_inherit = "account.invoice"

	amount_to_text = fields.Char(compute='_get_amount_to_text', string='Monto en Texto', readonly=True, help='Amount of the invoice in letter')

	@api.one
	@api.depends('amount_total')
	def _get_amount_to_text(self):
		self.amount_to_text = amount_to_text.get_amount_to_text(self, self.amount_total)