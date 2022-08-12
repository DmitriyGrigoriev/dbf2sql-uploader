jQuery(document).ready(function ($) {
    (function ($) {
        $(function () {
            var selectField = $('#id_engine'),
                verified = $('.security_fieldset');

            function toggleVerified(value) {
                if (value === 'mssql') {
                    verified.show();
                } else {
                    verified.hide();
                }
            }

            // show/hide on load based on existing value of selectField
            toggleVerified(selectField.val());

            // show/hide on change
            selectField.change(function() {
                toggleVerified($(this).val());
            });
        });
    })(django.jQuery);
});
