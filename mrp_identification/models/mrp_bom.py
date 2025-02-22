# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jul 2021

from odoo import models, fields, api


class MrpBom(models.Model):
    _inherit = "mrp.bom"

    @api.multi
    @api.depends('name', 'product_id')
    def name_get(self):
        """ Custom naming to remove bom name / product name duplication
        """
        res = []
        for rec in self:
            if rec.product_id.code in rec.code:
                name = '[%s] %s' % (rec.code, rec.product_id.name)
            else:
                name = '[%s] %s' % (rec.code, rec.product_id.display_name)
            res.append((rec.id, name))
        return res