from odoo import models, fields


class HolaMundo(models.Model):
    _name = 'hola.mundo'

    name = fields.Char(string="Nombre", required=True, default="Mundo")