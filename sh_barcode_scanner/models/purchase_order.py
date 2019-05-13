# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models,api
from datetime import datetime
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class PurchaseOrder(models.Model):
    _inherit='purchase.order'

    @api.one
    def sh_on_barcode_scanned(self, barcode):
        
        order_id =self.id
        purchase_order = self.env['purchase.order'].search([('id', '=', order_id)],limit=1)
         
        if purchase_order: 
            product_id = self.env['product.product'].search([('barcode', '=', barcode)],limit=1)
             
            if product_id: 
                if not purchase_order.order_line:    
                     
                    order_line_val = {
                        'name': product_id.name,
                        'product_id': product_id.id,
                        'product_qty': 1,
                        'product_uom': product_id.product_tmpl_id.uom_id.id,
                        'price_unit': product_id.product_tmpl_id.list_price,
                        'order_id': purchase_order.id,
                        'date_planned': datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT),
                    }
                    purchase_order.update({'order_line': [(0, 0, order_line_val)]})
                 
                else:              
                    purchase_order_line = purchase_order.order_line.search([('product_id', '=', product_id.id),('order_id','=',order_id)], limit=1)
        
                    if purchase_order_line:
                        purchase_order_line.product_qty +=  1
        
                    else:
                        order_line_val = {
                            'name': product_id.name,
                            'product_id': product_id.id,
                            'product_qty': 1,
                            'product_uom': product_id.product_tmpl_id.uom_id.id,
                            'price_unit': product_id.product_tmpl_id.list_price,
                            'order_id': purchase_order.id,
                            'date_planned': datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT),
                        }
                        purchase_order.update({'order_line': [(0, 0, order_line_val)]})
            else :
                raise UserError('Product does not exist')
