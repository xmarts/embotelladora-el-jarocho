# -*- coding: utf-8 -*-
from odoo import http

# class ReporteJarochito(http.Controller):
#     @http.route('/reporte_jarochito/reporte_jarochito/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reporte_jarochito/reporte_jarochito/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reporte_jarochito.listing', {
#             'root': '/reporte_jarochito/reporte_jarochito',
#             'objects': http.request.env['reporte_jarochito.reporte_jarochito'].search([]),
#         })

#     @http.route('/reporte_jarochito/reporte_jarochito/objects/<model("reporte_jarochito.reporte_jarochito"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reporte_jarochito.object', {
#             'object': obj
#         })