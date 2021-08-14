
window.onscroll = function() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20){
        scroll_up.style.display = 'block';
    }
    else{
        scroll_up.style.display = 'none';
    }
}
console.log('work');

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}