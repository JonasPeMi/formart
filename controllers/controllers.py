# -*- coding: utf-8 -*-
from odoo import http

# class Formarte(http.Controller):
#     @http.route('/formarte/formarte/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/formarte/formarte/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('formarte.listing', {
#             'root': '/formarte/formarte',
#             'objects': http.request.env['formarte.formarte'].search([]),
#         })

#     @http.route('/formarte/formarte/objects/<model("formarte.formarte"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('formarte.object', {
#             'object': obj
#         })