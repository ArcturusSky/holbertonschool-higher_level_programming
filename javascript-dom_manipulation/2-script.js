// script that adds the class red to the header element when the user clicks on the tag with id red_header

let button = document.getElementById('red_header');
button.addEventListener('click', function() {
    let section = document.querySelector("header");
    section.classList.add('red')
});

