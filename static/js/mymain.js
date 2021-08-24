let footer_contains = $('.footer_items>p');
if (parseInt($('footer').css('width')) < 530) {
    $('.col').css('width', '90%');
    Array.from(footer_contains).forEach(element => {
        $(element).css('display', 'none');
    });
    $('.footer_items').css({
        'display' : 'flex',
        'justify-content' : 'center',
        'align-items' : 'center',
        'flex-direction' : 'column'
    });
    $('.footer_items').after(
        `
        <p class="mt-3 text-white text-center 
        footer_main_text" style="font-size: 15px;">
        ТОО "ДАНИЛА МАСТЕР.КЗ"</p>
        `)
}