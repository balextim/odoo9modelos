# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo288w(http.Controller):
#     @http.route('/odoo288w/odoo288w/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo288w/odoo288w/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo288w.listing', {
#             'root': '/odoo288w/odoo288w',
#             'objects': http.request.env['odoo288w.odoo288w'].search([]),
#         })

#     @http.route('/odoo288w/odoo288w/objects/<model("odoo288w.odoo288w"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo288w.object', {
#             'object': obj
#         })
