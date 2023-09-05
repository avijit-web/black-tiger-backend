/* // Index Page
var typed = new Typed('#elementHome', {
    strings: ['tiger'],
    typeSpeed: 200,
    loop: true,
    backSpeed: 200,
    showCursor: false,
}); */



$('.brandSlider').owlCarousel({
    loop: true,
    margin: 10,
    nav: false,
    dots: false,
    autoplay: true,
    slideTransition: 'linear',
    autoplayTimeout: 2500,
    autoplaySpeed: 2500,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 2
        },
        600: {
            items: 3
        },
        1000: {
            items: 4
        }
    }
})


