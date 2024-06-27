/**@odoo-module **/
//import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
//import { CustomAlertPopup } from "@pos_buttons/js/PopUp/pos_pop_up";
export class CreateButton extends Component {

static template = "point_of_sale.CreateButton";

/**
* Setup function to initialize the component.

*/

setup() {
  this._loading();
this.pos = usePos();
//
this.popup = useService("popup");

}

/**
* Click event handler for the create button.

*/
_loading(){
  console.log("Setup loaded.........")
}




async onClick() {
        console.log(this.pos.get_order())
        console.log(this.pos.get_order().get_orderlines())
        console.log(this.pos.get_order().get_orderlines().length)
        const selectedOrderline = this.pos.get_order().get_selected_orderline();
        console.log(selectedOrderline)
        const orderLine = this.pos.get_order();
        if (!orderLine) {
            return;
          }
        const currentOrder = orderLine.get_orderlines().slice();
        for(let i=0;i<currentOrder.length;i++){
             orderLine.removeOrderline(currentOrder[i]);
    //         console.log(currentOrder[i])
        }
        console.log(selectedOrderline)

}
}
/**
 * Add the OrderlineProductCreateButton component to the control buttons in
   the ProductScreen.
 */
ProductScreen.addControlButton({
component: CreateButton,
});