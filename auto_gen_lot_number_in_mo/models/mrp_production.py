from odoo import fields,models,api,_
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError
from odoo.tools import float_is_zero
import math
from datetime import datetime

class mrp_production_al(models.Model):
    _inherit="mrp.production"
    
    lot_id=fields.Many2one('stock.production.lot', string='Lot',copy=False)
    
    @api.multi
    def open_produce_product(self):
        #if self.product_id.tracking == 'lot':
        auto_gen_lot_number = self.env['ir.config_parameter'].sudo().get_param('auto_gen_lot_number_in_mo.auto_generate_mo_lot_based_on')
        if auto_gen_lot_number == 'production_date':
            production_date = datetime.strptime(self.date_planned_start,"%Y-%m-%d %H:%M:%S")
            date = datetime.strftime(production_date,'%Y%m%d')
        else:
            date = datetime.now().strftime('%Y%m%d')
        
        if self.lot_id:
            res= super(mrp_production_al,self).open_produce_product()
        else:
            counter=1
            lot_id_name = date
            lot_ids=self.env['stock.production.lot'].search([('product_id','=',self.product_id.id),('name',"ilike",date)])
            if lot_ids:
                for lot in lot_ids:
                    counter+=1
                lot_id_name=date+str(counter)
            else:
                lot_id_name=date
            vals={
                    "product_id":self.product_id.id,
                    "name":lot_id_name
                    }
            self.lot_id = self.env['stock.production.lot'].create(vals)
        return super(mrp_production_al,self).open_produce_product()