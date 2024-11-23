// Script that toggles the class of the header element when the user clicks on the tag id toggle_header

let button = document.getElementById('toggle_header');
button.addEventListener('click', function() {
    // Select <header> element
    let header = document.querySelector('header');

    // Check the header's class and change it
    if (header.classList.contains('green')) {
        header.classList.remove('green');
        header.classList.add('red');
    } else {
        header.classList.remove('red');
        header.classList.add('green');
    }
});
