/* @odoo-module */
import {WebsiteSale} from "@website_sale/js/website_sale";

//In review order ---> shipping when the state you change it will add value in Apartment

WebsiteSale.include({
    events: Object.assign({}, WebsiteSale.prototype.events, {
        "change select[name='state_id']": "_onChangeState",
        "change select[name='city_id']": "_onChangeCity",
    }),
    start: function () {
//      Selected a .div_street2 and store in autoStreetTwo

        this.autoStreetTwo = document.querySelector(".div_street2");

        return this._super.apply(this, arguments);
    },

//    Overriding the functionality of _onChangeState function

    _onChangeState: function () {
        console.log("ABC")
        this.autoStreetTwo.querySelectorAll("input").forEach((input) => {
                                input.value = "Include Example";
                            });
      },
    }
});
