# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modelo288w(models.Model):
    _name = 'odoo288w.modelo288w'
    _description = 'model modelo288w'

    name = fields.Char('id',required=True)
    tipo = fields.Char(String='Tipo',required=True)
    altura = fields.Char(String='altura',required=True)
    ancho = fields.Char(String='ancho',required=True)
    profundidad = fields.Char(String='profundidad',required=True)

# modelo 2 para ejercicio segundo trimestre
class proveedores(models.Model):
    _name = 'odoo288w.proveedores'
    _description = 'model proveedores'

    name = fields.Char('identificador',required=True)
    nombre_proveedor = fields.Char(String='nombre_proveedor', required=True)
    tipo_producto = fields.Char(String='tipo_producto',required=True)
    unidades_repartidas = fields.Char(String='unidades_repartidas',required=True)
    mes = fields.Char(String='mes',required=True)

# modelo 3 para ejercicio segundo trimestre
class tiendas(models.Model):
    _name = 'odoo288w.tiendas'
    _description = 'model tiendas'

    name = fields.Char('identificador', required=True)
    nombre_tienda = fields.Char(String='nombre_tienda', required=True)
    tipo_producto = fields.Char(String='tipo_producto', required=True)
    unidades_facilitadas = fields.Char(String='unidades_facilitadas', required=True)
    id_proveedor = fields.Char(String='id_proveedor',required=True)
    mes = fields.Char(String='mes', required=True)
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
