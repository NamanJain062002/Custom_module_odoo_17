/* @odoo-module */
import {A} from './class_a'

A.include({
  include_method(){
    console.log("This is Include method!")
  }
});

