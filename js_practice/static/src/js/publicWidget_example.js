/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.customWidget = publicWidget.Widget.extend({
    selector: '.s_website_form_submit',
    events: {
        'click .s_website_form_send': '_onClickMethod',
    },

    /**
     * @override
     */
    start: function () {
      console.log('My Public Widget is started');
      return this._super.apply(this, arguments);
    },

    _onClickMethod: function () {
         event.preventDefault();
         alert('Button clicked!');
    },
});



