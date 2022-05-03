# -*- coding: utf-8 -*-
# from odoo import http


# class BankingManagement(http.Controller):
#     @http.route('/banking_management/banking_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/banking_management/banking_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('banking_management.listing', {
#             'root': '/banking_management/banking_management',
#             'objects': http.request.env['banking_management.banking_management'].search([]),
#         })

#     @http.route('/banking_management/banking_management/objects/<model("banking_management.banking_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('banking_management.object', {
#             'object': obj
#         })
