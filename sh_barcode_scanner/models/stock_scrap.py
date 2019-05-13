# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models,fields,api

class StockScrap(models.Model):
    _inherit='stock.scrap'
 
    barcode = fields.Char("Barcode")
    
    @api.onchange('barcode')
    def barcode_scanned(self):

        if self and self.barcode:
            
            product_obj = self.env['product.product'].search([('barcode', '=', self.barcode)],limit=1)
            if product_obj:
                
                if self.product_id:
                    if self.product_id.barcode == self.barcode:
                        self.scrap_qty += 1
                    else:
                        self.barcode = ''
                        self._cr.commit()
                        warning_mess = {
                            'message' : ('Scrap Product changed, please save current product scrap order and continue with next order.'),
                            'title': "Warning" 
                        }
                        return {'warning': warning_mess}         
                        
                else:
                    self.product_id = product_obj.id
            
                self.barcode = ''
            else :
                self.barcode = ''
                self._cr.commit()
                warning_mess = {
                    'message' : ('Product with this barcode does not exist.'),
                    'title': "Warning" 
                }
                return {'warning': warning_mess}         
                    
 
#     @api.one
#     def sh_on_barcode_scanned(mdl,barcode):
#  
#         print ('\n\n self',mdl)
#         print ('\n\n self',barcode)
        
        
#        picking_id =self.id
#         stock_picking = self.env['stock.picking'].search([('id', '=', picking_id)],limit=1)       
#             
#         if stock_picking:
#             product_id = self.env['product.product'].search([('barcode', '=', barcode)],limit=1)
#     
#             if product_id:
#                 stock_picking_line = stock_picking.move_lines.search([('product_id', '=', product_id.id),('picking_id','=',picking_id)], limit=1)
#                      
#                 if stock_picking_line:         
#                     stock_picking_line.quantity_done += 1
#                     self._cr.commit()
#                     
#                     if stock_picking_line.quantity_done  == stock_picking_line.product_qty :
#                         raise Warning('Done quantity exceed required quantity')       
#     
#             else :
#                 raise UserError('Product does not exist')
#              