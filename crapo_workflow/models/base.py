"""
see README for details
"""

from odoo import models


class Base(models.AbstractModel):
    """
    The base model, which is implicitly inherited by all models.

    A new :meth:`wf_event` method is added on all Odoo Models, allowing to
    notify an event to crapo_workflow
    """

    _inherit = "base"

    def _job_prepare_context_before_enqueue_keys(self):
        default_context_keys = (
            super()._job_prepare_context_before_enqueue_keys()
        )
        lst_default_context_keys = list(default_context_keys)
        for key in self.env.context.keys():
            if key not in lst_default_context_keys:
                lst_default_context_keys.append(key)
        default_context_keys = tuple(lst_default_context_keys)
        return default_context_keys

    def wf_event(self, name, values=None):
        """
        Notify event to workflow broker
        """
        broker = self.env["crapo.workflow.broker"]
        for rec in self:
            if values is None:
                values = {}
            values["record"] = rec
            broker = self.copy_context(rec, broker)
            broker.with_delay().notify(name, values)

    def copy_context(self, from_model, to_model):
        for key in from_model.env.context.keys():
            if key not in to_model.env.context.keys():
                to_model[key] = from_model.env.context[key]
        return to_model
