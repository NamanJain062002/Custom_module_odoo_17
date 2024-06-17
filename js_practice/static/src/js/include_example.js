/* @odoo-module */
import {WebsiteSale} from "@website_sale/js/website_sale";
import {customWidget} from "@js_practice/js/publicWidget_example";

customWidget.include({
    events: Object.assign({}, customWidget.prototype.events, {
       "click .s_website_form_send": '_onClickMethod2',
    }),

    start: function(){
       console.log("Include is done in custom widget");
       return this._super.apply(this, arguments);
    },

    _onClickMethod2: function(){
       alert("Include Functionality");
    },
});


//In review order ---> shipping when the state you change it will add value in Apartment
//
//WebsiteSale.include({
//    events: Object.assign({}, WebsiteSale.prototype.events, {
//        "change select[name='state_id']": "_onChangeState",
//        "change select[name='city_id']": "_onChangeCity",
//    }),
//    start: function () {
////      Selected a .div_street2 and store in autoStreetTwo
//
//        this.autoStreetTwo = document.querySelector(".div_street2");
//
//        return this._super.apply(this, arguments);
//    },
//
////    Overriding the functionality of _onChangeState function
//
//    _onChangeState: function () {
//        console.log("ABC")
//        this.autoStreetTwo.querySelectorAll("input").forEach((input) => {
//                                input.value = "Include Example";
//                            });
//      },
//    }
//});
