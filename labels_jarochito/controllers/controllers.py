# -*- coding: utf-8 -*-
from odoo import http

# class LabelsJarochito(http.Controller):
#     @http.route('/labels_jarochito/labels_jarochito/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/labels_jarochito/labels_jarochito/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('labels_jarochito.listing', {
#             'root': '/labels_jarochito/labels_jarochito',
#             'objects': http.request.env['labels_jarochito.labels_jarochito'].search([]),
#         })

#     @http.route('/labels_jarochito/labels_jarochito/objects/<model("labels_jarochito.labels_jarochito"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('labels_jarochito.object', {
#             'object': obj
#         })