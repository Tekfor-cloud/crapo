"""
See README for details
"""
from odoo import models, api, fields


class IrActionsServer(models.Model):
    """
    Crapo specific version of ir.actions.server
    """

    _inherit = "ir.actions.server"

    usage = fields.Selection(
        selection_add=[("crapo_automaton_action", "Crapo automaton action")],
        ondelete={"crapo_automaton_action": "set default"},
    )


class CrapoAutomatonAction(models.Model):
    """
    Crapo Action is a specialisation of Server Actions in order to be
    able to use them in actions/activities and run them asynchronously
    """

    _name = "crapo.automaton.action"
    _description = "Crapo Automaton Action"
    _inherits = {"ir.actions.server": "action_server_id"}
    _description = "A specialization of server actions for Crapo Automata"

    action_server_id = fields.Many2one(
        "ir.actions.server", required=True, ondelete="restrict"
    )

    def run(self):
        """
        Execute action
        """
        self.action_server_id.run()

    def run_async(self):
        """
        run action asynchronously
        """
        self.action_server_id.run()

    # ==============================
    # Write/Create
    # ==============================

    @api.model
    def create(self, values):
        """
        Override default creation : fixes value for 'usage'
        """
        values["usage"] = "crapo_automaton_action"
        return super(CrapoAutomatonAction, self).create(values)
