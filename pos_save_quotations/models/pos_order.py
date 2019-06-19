# -*- coding: utf-8 -*-
from odoo import api, models, fields

class pos_order(models.Model):
    _inherit = "pos.order"

    quotation_id = fields.Many2one('pos.quotation', 'Quotation', readonly=1)

    @api.model
    def _order_fields(self, ui_order):
        res = super(pos_order, self)._order_fields(ui_order)
        if ui_order.get('quotation_name', ''):
            quotations = self.env['pos.quotation'].search([('name', '=', ui_order.get('quotation_name'))])
            if quotations:
                res.update({
                    'quotation_id': quotations[0].id
                })
                quotations.write({'state': 'delivery_success'})
        if ui_order.get('note', ''):
            res.update({
                'note': ui_order.get('note'),
            })
        return res