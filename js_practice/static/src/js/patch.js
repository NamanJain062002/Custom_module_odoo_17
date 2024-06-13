/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import {PlanningGanttController} from '@planning/views/planning_gantt/planning_gantt_controller';


patch(PlanningGanttController.prototype, {
  setup(){
   super.setup();
  },

   async hi_method(){
//   This the date and time zone in javascript
    try{ // try block
        var date = new Date();
        const easternTime = date.toLocaleString("en-US", {timeZone: "America/New_York"});
        const londonTime = date.toLocaleString("en-GB", {timeZone: "Europe/London"});
        console.log(easternTime)
        console.log(londonTime)
          console.log(date)
        alert("Date & Time in INDIA "+date)
        }
        catch(error){ // catch block to handle any error
          console.log("Try & Catch error>>>>>>>", error)
        }
   },

});