/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.customWidget = publicWidget.Widget.extend({
    selector: '.container',

    /**
     * @override
     */
    start: function () {
        console.log('Custom Web page render using controller');
        this._super.apply(this, arguments);
        this._bindEvents();
    },

    _bindEvents: function () {
        this.$('.widget-trigger').on('click', this.trigger_method.bind(this));
        this.$('.submit-btn').on('click', this.chk_email.bind(this));

    },

    chk_email: function(){
       let email = document.getElementById('email').value
       let mobile = document.getElementById('mobile').value

       if (mobile.length != 10){
          alert("Mobile Number Must Be Of 10 Digit");
          return false;
        }

       let flag = 0;
       let ans = true;
       for(let i=0; i<email.length; i++){
          if (email[i] == '@'){
            flag = flag + 1;
            if (i+1 >= email.length){
              ans = false;
            }
          }
       }

       if (flag != 1 || ans==false){
         alert("Please enter valid email")
         return false;
       }
       else if(flag == 1 && ans==false){
         alert("Please enter valid email");
         return false;
       }
      return true;
    },

    trigger_method: function () {
//        alert('Public Widget Call!');
         this.change_form_bg_color();
    },

     change_form_bg_color: function () {
      const randomColor = this.getRandomColor();
        this.$('.submit-form').css('background-color', randomColor);
    },

      getRandomColor: function () {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }
});
