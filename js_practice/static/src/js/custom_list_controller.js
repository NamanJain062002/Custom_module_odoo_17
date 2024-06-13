/** @odoo-module */

import {ListController} from "@web/views/list/list_controller";
import {listView} from "@web/views/list/list_view";
import { registry } from "@web/core/registry";

class CustomListController extends ListController{
   demo_method(){
     const selected = this.model.root.selection;
     console.log(selected)
     const ordID = selected.map((i)=>i.resId);
     console.log(ordID)
   }
}

CustomListController.template = "js_practice.list_btn";

export const CustomList = {
    ...listView,
    Controller: CustomListController,
};
registry.category("views").add("demo_btn", CustomList);