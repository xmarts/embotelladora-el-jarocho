# -*- coding: utf-8 -*-
from odoo import api, models, fields

class pos_quotation(models.Model):
    _name = "pos.quotation"
    _inherit = ['mail.thread']
    _order = 'create_date DESC'

    name = fields.Char('Name')
    uid = fields.Char('Order ID', readonly=1)
    session_id = fields.Many2one('pos.session', 'Session')
    datas = fields.Text('Datas')
    shop_ids = fields.Many2many('pos.shop', 'pos_quotation_pos_shop_rel', 'quotation_id', 'shop_id','Shop', required=1)
    user_id = fields.Many2one('res.users', 'Create by', required=1)
    create_date = fields.Datetime('Create at', readonly=1)
    partner_id = fields.Many2one('res.partner', 'Customer')
    state = fields.Selection([
        ('waiting_transfer', 'Waiting Transfer'),
        ('delivery_success', 'Delivery Success'),
        ('removed', 'Removed')
    ], default='waiting_transfer', string='State')
    amount_paid = fields.Float('Amount paid')
    amount_total = fields.Float('Amount Total')
    note = fields.Text('Note')
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.user.company_id)
    line_ids = fields.One2many("pos.quotation.line", 'quotation_id', 'Lines')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('pos.quotation')
        return super(pos_quotation, self).create(vals)

    @api.model
    def remove_pos_quotation(self, quotation_id=None):
        if quotation_id:
            self.browse(quotation_id).write({'state': 'removed'})
        else:
            return self.write({'state': 'removed'})

    @api.model
    def get_quotations(self, shop_id):
        values = []
        records = self.search([('state', '=', 'waiting_transfer')])
        for record in records:
            shop_ids = []
            for shop in record.shop_ids:
                shop_ids.append(shop.id)
            if shop_id in shop_ids:
                val = record.read()[0]
                if val.get('partner_id', None):
                    val['partner_id'] = self.env['res.partner'].browse(val['partner_id'][0]).read()[0]
                val['datas'] = eval(val['datas'])
                values.append(val)
        return values

    @api.model
    def save_quotation(self, json_order):
        quotations = self.search([('uid', '=', json_order['uid']), ('state', '=', 'waiting_transfer')])
        value = {
            'user_id': json_order['user_id'],
            'uid': json_order['uid'],
            'session_id': json_order['pos_session_id'],
            'partner_id': json_order['partner_id'],
            'amount_paid': json_order['amount_paid'],
            'shop_ids': [(6, 0, json_order['shop_ids_selected'])],
            'amount_total': json_order['amount_total'],
            'datas': json_order,
            'note': json_order.get('note', '')
        }
        if quotations:
            quotations.write(value)
            quotations.line_ids.unlink()
            send_mail_after_save = json_order['send_mail_after_save']
            for line in json_order['lines']:
                tax_ids = line[2]['tax_ids'][0][2]
                self.env['pos.quotation.line'].create({
                    'quotation_id': quotations[0].id,
                    'product_id': line[2]['product_id'],
                    'discount': line[2]['discount'],
                    'price_unit': line[2]['price_unit'],
                    'qty': line[2]['qty'],
                    'tax_ids': [(6, 0, tax_ids)],
                })
            if send_mail_after_save:
                mail_template = self.env.ref('pos_save_quotations.email_pos_quotation')
                mail_template.send_mail(quotations[0].id)
            return True
        else:
            pos_quotation = self.create(value)
            send_mail_after_save = json_order['send_mail_after_save']
            for line in json_order['lines']:
                tax_ids = line[2]['tax_ids'][0][2]
                self.env['pos.quotation.line'].create({
                    'quotation_id': pos_quotation.id,
                    'product_id': line[2]['product_id'],
                    'discount': line[2]['discount'],
                    'price_unit': line[2]['price_unit'],
                    'qty': line[2]['qty'],
                    'tax_ids': [(6, 0, tax_ids)],
                })
            if send_mail_after_save:
                mail_template = self.env.ref('pos_save_quotations.email_pos_quotation')
                mail_template.send_mail(pos_quotation.id)
        return True

    class pos_quotation(models.Model):
        _name = "pos.quotation.line"

        quotation_id = fields.Many2one("pos.quotation", "Quotation", required=1, readonly=1)
        product_id = fields.Many2one('product.product', 'Product', readonly=1)
        discount = fields.Float('Discount %', readonly=1)
        price_unit = fields.Float('Price unit', readonly=1)
        qty = fields.Float('Quantity', readonly=1)
        tax_ids = fields.Many2many('account.tax', 'pos_quotation_line_account_tax_rel', 'quotation_line_id', 'tax_id', 'Tax', readonly=1)
