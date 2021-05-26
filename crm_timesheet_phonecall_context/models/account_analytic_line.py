# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, May 2021

from odoo import api, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    @api.onchange('project_id')
    def onchange_project_id(self):
        res = super().onchange_project_id()
        if 'domain' in res:
            filter = []
            if self.project_id:
                filter = [('project_id', '=', self.project_id.id)]
            res['domain']['phonecall_id'] = filter
        return res
