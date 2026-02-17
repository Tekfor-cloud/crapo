/** @odoo-module **/

import { StatusBarField } from "@web/views/fields/statusbar/statusbar_field";
import { patch } from "@web/core/utils/patch";

patch(StatusBarField.prototype, {
  async selectItem(item) {
    const { name, record } = this.props;
    const value =
      this.field.type === "many2one" ? [item.value, item.label] : item.value;
    await record.update({ [name]: value });
    const onError = this.onSaveError.bind(this);
    await record.save({ onError });
  },

  async onSaveError(error, { discard }) {
    const { name, record } = this.props;
    record.update({ [name]: record._values[name] });
    throw error;
  },
});
