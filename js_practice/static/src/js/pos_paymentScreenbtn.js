/**@odoo-module **/
import { Component } from "@odoo/owl";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";
import { useState } from "@odoo/owl";

patch(PaymentScreen.prototype,{

setup(){
  super.setup();
      this.state = useState({
            count: 0
        });
},

payment_method(){
   console.log("Payment>>>>>>>>")
   // alert(this.state.count)
   this.state.count++;
},

});



