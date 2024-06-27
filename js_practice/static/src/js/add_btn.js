/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ExpenseListController } from '@hr_expense/views/list';


patch(ExpenseListController.prototype, {

        add_btn() {
//                const now = new Date().getTime();
//                 console.log(now)
//                console.log(now.toLocaleString())
// create a new Date object with the current date and time

        var date = new Date().add;

// use the toLocaleString() method to display the date in different timezones
        const easternTime = date.toLocaleString("en-US", {timeZone: "America/New_York"});
        const londonTime = date.toLocaleString("en-GB", {timeZone: "Europe/London"});
        console.log(easternTime)
        console.log(londonTime)

            alert("Hi")

            },

});


