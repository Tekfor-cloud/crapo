/** @odoo-module **/

import { StatusBarField } from "@web/views/fields/statusbar/statusbar_field";
import { patch } from "@web/core/utils/patch";

patch(StatusBarField.prototype, "statusbar_patch", {
  selectItem(item) {
    switch (this.props.type) {
      case "many2one":
        const self = this;
        const value = this.props.value;
        this.props
          .update([item.id, item.name], { save: true })
          .then(function (res) {
            if (!res) {
              self.props.update(value);
            }
          });
        break;
      case "selection":
        this.props.update(item.id, { save: true });
        break;
    }
  },
});
