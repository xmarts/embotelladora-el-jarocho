from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare

class AddBranchJournal(models.Model):
	_inherit = 'account.journal'

	@api.multi
	def _default_branch_id(self):
		print ("sssssssssssssssssssssssssssssssssssssssssssss",self._context.get('branch_id'))
		if not self._context.get('branch_id'):
			branch_id = self.env['res.users'].browse(self._uid).branch_id.id
		else:
			branch_id =  self._context.get('branch_id')
		return branch_id
		
	branch_id = fields.Many2one('res.branch', default=_default_branch_id)