/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { TextAreaPopup } from "@point_of_sale/app/utils/input_popups/textarea_popup";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import {Order} from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

export class CustomNotePOPUP extends Component {
    static template = "point_of_sale.CustomPOPbtn";
//    static template = "point_of_sale.customNote";

    setup() {
        this.pos = usePos();
        this.popup = useService("popup");
    }
    async onClick() {
        const order = this.pos.get_order();
        const selectedOrderline = this.pos.get_order().get_selected_orderline();
        // FIXME POSREF can this happen? Shouldn't the orderline just be a prop?
        if (!selectedOrderline) {
            return;
        }
        const { confirmed, payload: inputNote } = await this.popup.add(TextAreaPopup, {
            startingValue: selectedOrderline.get_customer_note(),
            title: _t("Add Customer Note"),
        });

        if (confirmed) {
           let notes = document.getElementsByClassName("custom_note");

           console.log(notes);
            if (notes.length > 0){
            var note = notes[0];
            // Step 3: Set the innerText or textContent property
            note.innerText = inputNote; // or element.textContent = 'New Text';

          }

          order.setNotes(inputNote);
        }

    }
}

ProductScreen.addControlButton({
    component: CustomNotePOPUP,
});

patch(Order.prototype,{

     export_as_JSON(){
       const res = super.export_as_JSON(...arguments);
       res.notes = this.get_notes();
           res.location_pos = this.location_value;
       return res;
     },

     get_notes(){
       return this.inputNote
     },

     setNotes(inputNote){
       this.inputNote = inputNote
     },

     export_for_printing(){
       const rec = super.export_for_printing(...arguments);
       rec.note = this.inputNote
        rec.location_recept = this.location_value
       return rec;
     },






//     export_as_JSON(){
//       const res = super.export_as_JSON(...arguments);
//       res.location_pos = this.get_location();
//       return res;
//     },

//     get_location(){
//       return this.location_value
//     },

     set_location(selection){
       this.location_value = selection
     },


//     export_for_printing(){
//       const rec = super.export_for_printing(...arguments);
//       rec.location_recept = this.location_value
//       return rec;
//     }


})
