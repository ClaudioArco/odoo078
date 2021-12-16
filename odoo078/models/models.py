# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo078(models.Model):
#     _name = 'odoo078.odoo078'
#     _description = 'odoo078.odoo078'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class moviles078(models.Model):
	_name = 'odoo078.moviles078'
	_description = 'model moviles078'

	name = fields.Char('Num',required=True)
	modelo = fields.Char(string='Modelo',required=True)
	marca = fields.Char(string='Marca',required=True)

