# -*- coding: utf-8 -*-
from odoo import api, models, fields

class pos_shop(models.Model):
    _name = "pos.shop"

    name = fields.Char('Name', required=1)
    image = fields.Binary('Image')