// script that updates the text color of the header element to red (#FF0000)
// when the user clicks on the tag with id red_header:

let button = document.getElementById('red_header');
button.addEventListener('click', function() {
    ColorThingInColor('header', 'FF0000');
});

export default function ColorThingInColor(Tag, ColorCode) {
    document.querySelector(${Tag}).style.color = `#${ColorCode}`;
};