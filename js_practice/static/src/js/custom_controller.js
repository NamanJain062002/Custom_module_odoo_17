/* @odoo-module */
import { FormController } from "@web/views/form/form_controller";
import { formView } from "@web/views/form/form_view";
import { registry } from "@web/core/registry";

class CustomController extends FormController {
    ControllerMethod() {
                alert("HI")
    }
}
CustomController.template = "js_practice.controller_btn";

export const modelInfoStock = {
    ...formView,
    Controller: CustomController,
};
registry.category("views").add("stock_info", modelInfoStock);
