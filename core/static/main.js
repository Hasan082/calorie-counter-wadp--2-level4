$(document).ready(function () {

    // Handle menu arrow clicks
    $('.arrow').on('click', function () {
        $(this).closest('.menu-item').toggleClass('showMenu');
        // OR if parentElement.parentElement is needed:
        $(this).parent().parent().toggleClass('showMenu');
    });

    // Handle sidebar toggle
    $('.bx-menu').on('click', function () {
        $('.sidebar').toggleClass('close');
    });

});

