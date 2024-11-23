// Script that updates the text of the "header" element to "New Header!!!"" when the user clicks on the element with id "update_header"

let button = document.getElementById('update_header');
button.addEventListener('click', function() {

    //Select the header and changed the content of it
    let header = document.querySelector('header');
    header.textContent = "New Header! ! !"
});
