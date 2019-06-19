# -*- coding: utf-8 -*-
from odoo import api, models, fields

class pos_config(models.Model):
    _inherit = 'pos.config'

    allow_save_quotation = fields.Boolean('Allow save quotations')
    allow_load_data = fields.Boolean('Allow load quotations')
    delete_after_save = fields.Boolean('Delete order after save quotation')
    send_mail_after_save = fields.Boolean('Send email after save quotation')
    hide_shop_selection = fields.Boolean('Hide shop selection')
    shop_id = fields.Many2one('pos.shop', 'Shop')
