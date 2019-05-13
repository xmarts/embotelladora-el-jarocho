# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, api 
from odoo.exceptions import UserError

class MrpBom(models.Model):
    _inherit = 'mrp.bom'
    
    @api.one
    def sh_on_barcode_scanned(self, barcode):
        
        bom_id = self.id
        mrp_bom = self.env['mrp.bom'].search([('id', '=', bom_id)],limit=1)
       
        if mrp_bom:
            product_id = self.env['product.product'].search([('barcode', '=', barcode)],limit=1)        
             
            if product_id: 
                if not mrp_bom.bom_line_ids:    
                    bom_line_val = {
                       'product_id': product_id.id,
                       'product_qty': 1,    
                       'product_uom_id': product_id.product_tmpl_id.uom_id.id,
                       'bom_id': mrp_bom.id
                    }
                    mrp_bom.update({'bom_line_ids': [(0, 0, bom_line_val)]})
         
                else:
                    mrp_bom_line = mrp_bom.bom_line_ids.search([('product_id', '=', product_id.id),('bom_id','=',bom_id)], limit=1)                
                     
                    if mrp_bom_line:
                        mrp_bom_line.product_qty = mrp_bom_line.product_qty + 1
        
                    else:
                        bom_line_val = {
                            'product_id': product_id.id,
                            'product_qty': 1,
                            'product_uom_id': product_id.product_tmpl_id.uom_id.id,
                            'bom_id': mrp_bom.id
                        }
                        mrp_bom.update({'bom_line_ids': [(0, 0, bom_line_val)]})
    
            else :
                raise UserError('Product does not exist')
