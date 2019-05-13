# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models,api,_
from odoo.exceptions import Warning,UserError

class StockPicking(models.Model):
    _inherit='stock.picking'
 
    @api.one
    def sh_on_barcode_scanned(self, barcode):
#         self.ensure_one()
        picking_id =self.id
        stock_picking = self.env['stock.picking'].search([('id', '=', picking_id)],limit=1)       
            
        if stock_picking:
            product_id = self.env['product.product'].search([('barcode', '=', barcode)],limit=1)
    
            if product_id:
                stock_picking_line = stock_picking.move_lines.search([('product_id', '=', product_id.id),('picking_id','=',picking_id)], limit=1)
                     
                if stock_picking_line:         
                    stock_picking_line.quantity_done += 1
                    self._cr.commit()
                    
                    if stock_picking_line.quantity_done == stock_picking_line.product_uom_qty + 1:
                        raise Warning('Becareful! Quantity exceed than initial demand!')   
    
            else:
                raise UserError('Product does not exist')


    @api.multi
    def show_success_msg(self,counter,skipped_line_no):
        
        #to close the current active wizard        
        action = self.env.ref('sh_import_inventory.sh_import_inventory_action').read()[0]
        action = {'type': 'ir.actions.act_window_close'} 
        
        #open the new success message box    
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False                                   
        context = dict(self._context or {})
        dic_msg = str(counter) + " Records imported successfully"
        if skipped_line_no:
            dic_msg = dic_msg + "\nNote:"
        for k,v in skipped_line_no.items():
            dic_msg = dic_msg + "\nRow No " + k + " " + v + " "
        context['message'] = dic_msg            
        
        return {
            'name': 'Success',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
            }  