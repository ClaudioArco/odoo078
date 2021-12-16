# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo078(http.Controller):
#     @http.route('/odoo078/odoo078/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo078/odoo078/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo078.listing', {
#             'root': '/odoo078/odoo078',
#             'objects': http.request.env['odoo078.odoo078'].search([]),
#         })

#     @http.route('/odoo078/odoo078/objects/<model("odoo078.odoo078"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo078.object', {
#             'object': obj
#         })
