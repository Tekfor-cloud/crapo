"""
See README for details
"""

from odoo import models, api


class ResPartner(models.Model):
    """
    Add crapo.automaton.mixin to res.partner and emit wf_event
    on event and create
    """

    _inherit = ["res.partner", "crapo.automaton.mixin"]
    _name = "res.partner"

    @api.model_create_multi
    def create(self, vals_list):
        """
        Emit wf_event on create
        """
        recs = super(ResPartner, self).create(vals_list)
        for rec in recs:
            rec.wf_event("record_create")
        return recs

    def write(self, values):
        """
        Emit wf_event on write
        """
        res = super(ResPartner, self).write(values)
        self.wf_event("record_write")
        return res
