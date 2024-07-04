/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { PartnerListScreen } from "@point_of_sale/app/screens/partner_list/partner_list";

patch(PartnerListScreen.prototype, {

   async set_sundry_customer(){
     var data = this.pos.partners
     console.log(data)
        for (let i of data){
            if (i.id == 63){
            this.state.selectedPartner = i;
            this.props.resolve({ confirmed: true, payload: this.state.selectedPartner });
            this.pos.closeTempScreen();
            }
//   const res = await this.orm.call('pos.order', 'get_Partner',['true']);
//    const obj = {
//      name: res,
//
//    }
//
//
//      console.log(res);
////      this.state.selectedPartner = 'NAMAN';
//      this.clickPartner(obj);
   }
   }

})



//patch(PosStore.prototype, {
//
//
//})