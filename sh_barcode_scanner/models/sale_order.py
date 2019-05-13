# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, api 
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.one
    def sh_on_barcode_scanned(self, barcode):
        
        order_id =self.id
        sale_order = self.env['sale.order'].search([('id', '=', order_id)],limit=1)
       
        if sale_order:
            product_id = self.env['product.product'].search([('barcode', '=', barcode)],limit=1)        
             
            if product_id: 
                if not sale_order.order_line:    
                    order_line_val = {
                       'name': product_id.name,
                       'product_id': product_id.id,
                       'product_qty': 1,    
                       'product_uom': product_id.product_tmpl_id.uom_id.id,
                       'price_unit': product_id.product_tmpl_id.list_price,
                       'order_id': sale_order.id
                    }
                    sale_order.update({'order_line': [(0, 0, order_line_val)]})
         
                else:
                    sale_order_line = sale_order.order_line.search([('product_id', '=', product_id.id),('order_id','=',order_id)], limit=1)                
                     
                    if sale_order_line:
                        sale_order_line.product_uom_qty = sale_order_line.product_uom_qty + 1
        
                    else:
                        order_line_val = {
                            'name': product_id.name,
                            'product_id': product_id.id,
                            'product_qty': 1,
                            'product_uom': product_id.product_tmpl_id.uom_id.id,
                            'price_unit': product_id.product_tmpl_id.list_price,
                            'order_id': sale_order.id
                        }
                        sale_order.update({'order_line': [(0, 0, order_line_val)]})
    
            else :
                raise UserError('Product does not exist')
