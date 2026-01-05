"""
See README for details
"""

from lxml.builder import E  # pylint: disable=no-name-in-module
from odoo import models


class ReadonlyViewMixin(models.AbstractModel):
    """
    Mixin class that can be used to set a whole view readonly with domains
    """

    _name = "crapo.readonly.view.mixin"
    _description = "Crapo Readonly View Mixin"

    _readonly_expression = "False"
    _readonly_fields_to_add = []

    def _valid_field_parameter(self, field, name):
        # I can't even
        return (
            name == "skip_readonly_domain"
            or super()._valid_field_parameter(field, name)
        )

    def _get_view(self, view_id=None, view_type="form", **options):
        arch, view = super()._get_view(view_id, view_type, **options)
        if view_type in ("form", "list"):
            skip_fields = [
                name
                for name, field in self._fields.items()
                if (
                    hasattr(field, "skip_readonly_domain")
                    and field.skip_readonly_domain
                )
                or field.readonly
            ]

            for field in self._readonly_fields_to_add:
                arch.append(
                    E.field(
                        name=field,
                        invisible="True",
                        column_invisible="True",
                    )
                )

            self._process_field(arch, skip_fields)
        return arch, view

    def _process_field(self, node, skip_fields):
        """
        Add readnoly attrs if needed
        """

        if node.tag == "field":
            field_name = node.get("name")

            if field_name in skip_fields:
                return
            readonly = node.get("readonly") or "False"
            readonly += " or " + self._readonly_expression.format(field_name)
            node.set("readonly", str(readonly))

        else:
            for child_node in node:
                self._process_field(child_node, skip_fields)
