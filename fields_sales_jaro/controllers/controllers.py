# -*- coding: utf-8 -*-
from odoo import http

# class FieldsSalesJaro(http.Controller):
#     @http.route('/fields_sales_jaro/fields_sales_jaro/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fields_sales_jaro/fields_sales_jaro/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fields_sales_jaro.listing', {
#             'root': '/fields_sales_jaro/fields_sales_jaro',
#             'objects': http.request.env['fields_sales_jaro.fields_sales_jaro'].search([]),
#         })

#     @http.route('/fields_sales_jaro/fields_sales_jaro/objects/<model("fields_sales_jaro.fields_sales_jaro"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fields_sales_jaro.object', {
#             'object': obj
#         })