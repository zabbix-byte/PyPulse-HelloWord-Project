$('document').ready(() => {
    $('body').css('height', window.innerHeight);
    $('nav li').on("click", function () {
        let right = 0;
        let left = 0;
        switch ($(this).attr('id')) {
            case 'logout':
                left = 0;
                right = 1;
                break;
            case 'favourites':
                left = 1;
                right = 2;
                break;
            case 'cart':
                left = 2;
                right = 1;
                break;
            case 'account':
                left = 1;
                right = 0;
                break;
        }
        $('.nav-left-part').css('flex-grow', left);
        $('.nav-right-part').css('flex-grow', right);
        $('nav li').removeClass('active-item');
        $(this).addClass('active-item');
    })

})