# -*- coding: utf-8 -*-
from odoo import http

# class AmountText(http.Controller):
#     @http.route('/amount_text/amount_text/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/amount_text/amount_text/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('amount_text.listing', {
#             'root': '/amount_text/amount_text',
#             'objects': http.request.env['amount_text.amount_text'].search([]),
#         })

#     @http.route('/amount_text/amount_text/objects/<model("amount_text.amount_text"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('amount_text.object', {
#             'object': obj
#         })