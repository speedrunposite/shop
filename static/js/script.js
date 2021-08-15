
<<<<<<< HEAD
=======
window.onscroll = function() {
    if (document.body.scrollTop >= 20 || document.documentElement.scrollTop >= 20){
        scroll_up.style.display = 'block';
    }
    else{
        scroll_up.style.display = 'none';
    }
}
>>>>>>> 1fcd61ebd6c577ec5c6f52fffe7fd9a371ee3200

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}