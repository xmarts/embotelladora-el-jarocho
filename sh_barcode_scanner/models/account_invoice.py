# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, api
from odoo.exceptions import UserError

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    
    @api.one
    def sh_on_barcode_scanned(self, barcode):
        
        invoice_id = self.id    

        if self.type=="out_invoice":  # Sales Invoice

            sale_invoice = self.env['account.invoice'].search([('id', '=', invoice_id),('type','=','out_invoice')],limit=1)
                
            if sale_invoice:                
                product_id = self.env['product.product'].search([('barcode', '=', barcode)],limit=1)    
                
                ir_property_obj = self.env['ir.property']
        
                account_id = False
                if product_id and product_id.id:
                    account_id = product_id.property_account_income_id.id or product_id.categ_id.property_account_income_categ_id.id
                if not account_id:
                    inc_acc = ir_property_obj.get('property_account_income_categ_id', 'product.category')
                    account_id = self.fiscal_position_id.map_account(inc_acc).id if inc_acc else False
                if not account_id:
                    raise UserError(
                        _('There is no income account defined for this product: "%s". You may have to install a chart of account from Accounting app, settings menu.') %
                        (product_id.name,))                    
                  
                if product_id:     
                    if not sale_invoice.invoice_line_ids:    

                        invoice_line_val = {
                            'name': product_id.name,
                            'product_id': product_id.id,
                            'account_id':account_id,   
                            'quantity': 1,
                            'product_uom': product_id.product_tmpl_id.uom_id.id,
                            'price_unit': product_id.product_tmpl_id.list_price,
                            'invoice_id': sale_invoice.id
                        }
                        sale_invoice.update({'invoice_line_ids': [(0, 0, invoice_line_val)]})
                 
                    else:
                        sale_invoice_line = sale_invoice.invoice_line_ids.search([('product_id', '=', product_id.id),('invoice_id','=',invoice_id)], limit=1)                
                             
                        if sale_invoice_line:
                            sale_invoice_line.quantity = sale_invoice_line.quantity + 1
                        
                        else:
                            invoice_line_val = {
                                'name': product_id.name,
                                'product_id': product_id.id,
                                'account_id':account_id,   
                                'quantity': 1,
                                'product_uom': product_id.product_tmpl_id.uom_id.id,
                                'price_unit': product_id.product_tmpl_id.list_price,
                                'invoice_id': sale_invoice.id
                            }
                            sale_invoice.update({'invoice_line_ids': [(0, 0, invoice_line_val)]})
                else :
                    raise UserError('Product does not exist')


        elif self.type=="in_invoice":  # Purchase  Invoice
   
            
            purchase_invoice = self.env['account.invoice'].search([('id', '=', invoice_id),('type','=','in_invoice')],limit=1)       
                
            if purchase_invoice:      
                product_id = self.env['product.product'].search([('barcode', '=', barcode)],limit=1)        
                      
                ir_property_obj = self.env['ir.property']
        
                account_id = False
                if product_id and product_id.id:
                    account_id = product_id.property_account_expense_id.id or product_id.categ_id.property_account_expense_categ_id.id
                if not account_id:
                    inc_acc = ir_property_obj.get('property_account_expense_categ_id', 'product.category')
                    account_id = self.fiscal_position_id.map_account(inc_acc).id if inc_acc else False
                if not account_id:
                    raise UserError(
                        _('There is no income account defined for this product: "%s". You may have to install a chart of account from Accounting app, settings menu.') %
                        (product_id.name,))                   
                

                
                if product_id:      
                    if not purchase_invoice.invoice_line_ids:    
                        invoice_line_val = {
                            'name': product_id.name,
                            'product_id': product_id.id,
                            'account_id':account_id,   
                            'quantity': 1,
                            'product_uom': product_id.product_tmpl_id.uom_id.id,
                            'price_unit': product_id.product_tmpl_id.list_price,
                            'invoice_id': purchase_invoice.id
                        }
                        purchase_invoice.update({'invoice_line_ids': [(0, 0, invoice_line_val)]})
                  
                    else:
                        sale_invoice_line = purchase_invoice.invoice_line_ids.search([('product_id', '=', product_id.id),('invoice_id','=',invoice_id)], limit=1)                
                              
                        if sale_invoice_line:
                            sale_invoice_line.quantity = sale_invoice_line.quantity + 1
                        else:
                            invoice_line_val = {
                                'name': product_id.name,
                                'product_id': product_id.id,
                                'account_id':account_id,   
                                'quantity': 1,
                                'product_uom': product_id.product_tmpl_id.uom_id.id,
                                'price_unit': product_id.product_tmpl_id.list_price,
                                'invoice_id': purchase_invoice.id
                            }
                            purchase_invoice.update({'invoice_line_ids': [(0, 0, invoice_line_val)]})
                else :
                    raise UserError('Product does not exist')
                 
            
                        