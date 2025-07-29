from odoo import models, api

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['public'] = True  # Force attachment to be public
        return super(IrAttachment, self).create(vals_list)

    def write(self, vals):
        # Only set public if it's not already part of the update
        if 'public' not in vals:
            vals['public'] = True
        return super(IrAttachment, self).write(vals)
