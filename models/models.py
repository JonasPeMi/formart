# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Curso(models.Model):
    _name = 'formarte.curso'
    _description = "Formarte Cursos"

    nombre = fields.Char(required=True)
    descripcion = fields.Text()
    empresa = fields.Char()
    precio = fields.Float()
    duracion = fields.Float()

class Sesion(models.Model):
    _name = 'formarte.sesion'
    _description = "Formarte Sesiones"

    descripcion = fields.Text()
    start_date = fields.Date()
    end_date = fields.Date()
    lugar = fields.Char()
    profesor = fields.Char()
    duration = fields.Float(digits=(6, 2), help="Duration in days")


# class formarte(models.Model):
#     _name = 'formarte.formarte'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100