// Script  that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML element with id hello.
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  
    .then(response => {
    // Check if the response was successful
    if (response.ok) {

      // The response.json() method parses the response body as JSON and returns a promise
      return response.json();
    }})
  .then(data => { // JSON data received and treated now
    let content = document.getElementById('hello');
    content.innerHTML= data.hello
    });
