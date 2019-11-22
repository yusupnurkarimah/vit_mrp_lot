# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    
    @api.model
    def create(self, vals):
        res = super(MrpProduction, self).create(vals)
        lot_data = {
            'name': res.name,
            'product_id': res.product_id.id}
        self.env['stock.production.lot'].create(lot_data)
        
        
        return res