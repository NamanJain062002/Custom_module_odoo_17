/**@odoo-module **/
//import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
//import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
//import { usePos } from "@point_of_sale/app/store/pos_hook";
//import { CustomAlertPopup } from "@pos_buttons/js/PopUp/pos_pop_up";
export class CreateButton extends Component {

static template = "point_of_sale.CreateButton";

/**
* Setup function to initialize the component.

*/

setup() {
//this.pos = usePos();
//
//this.popup = useService("popup");

}

/**
* Click event handler for the create button.

*/

async onClick() {

  alert("POP UP Button")

}
}
/**
 * Add the OrderlineProductCreateButton component to the control buttons in
   the ProductScreen.
 */
ProductScreen.addControlButton({
component: CreateButton,
});