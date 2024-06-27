/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { TextAreaPopup } from "@point_of_sale/app/utils/input_popups/textarea_popup";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";

export class discountBtn extends Component {
    static template = "point_of_sale.discountBtn";

    setup() {
        this.pos = usePos();
        this.popup = useService("popup");
    }
    async onClick() {
        const selectedOrderline = this.pos.get_order().get_orderlines();
        // FIXME POSREF can this happen? Shouldn't the orderline just be a prop?
        if (!selectedOrderline) {
            return;
        }
        const { confirmed, payload: inputNote } = await this.popup.add(TextAreaPopup, {
//            startingValue: selectedOrderline.get_customer_note(),
            title: _t("Add Discount %"),
        });



        if (confirmed) {
         if ((inputNote > 100) || (inputNote <= 0)){
           this.popup.add(ErrorPopup, {
                    title: _t("You cant add invalid discount"),
                    body: _t(
                        "Invalid discount percentage. Please enter a value between 0% and 100%.",
                    ),
                    cancelKey: true,
                });
        }
        else{
         for(let order of selectedOrderline){
            order.set_discount(inputNote);
        }
        }
    }
}
}

ProductScreen.addControlButton({
    component: discountBtn,
});
