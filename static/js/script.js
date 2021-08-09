var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    var nav = document.querySelector('nav')
    if(window.pageYOffset > 300){
        nav.classList.add('bg-light')
    }
    else{
        nav.classList.remove('bg-light')
    }
}
console.log('work');