flectra.define('website_sale.payment', function (require) {
"use strict";

$(document).ready(function () {
    // If option is enable
    if ($("#checkbox_cgv").length) {
      var enabling_button = function() {
        $("button#o_payment_form_pay").prop("disabled", !this.checked);
      };
      $("#checkbox_cgv").click(enabling_button).each(enabling_button);
    }
});

});
