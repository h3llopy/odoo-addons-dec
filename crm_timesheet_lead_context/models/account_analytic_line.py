# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2021

from odoo import api, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    @api.onchange("lead_id")
    def onchange_lead_id(self):
        if not self.lead_id:
            return
        if not self.project_id and self.lead_id.project_id:
            self.project_id = self.lead_id.project_id

    @api.onchange('project_id')
    def onchange_project_id(self):
        res = super().onchange_project_id()
        if 'domain' in res:
            filter = []
            if self.project_id:
                filter = [('project_id', '=', self.project_id.id)]
            res['domain']['lead_id'] = filter
        return res
