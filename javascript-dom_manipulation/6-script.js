// Script that fetches the character name from the specified URL
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    // Check if the response was successful
    if (response.ok) {

      // The response.json() method parses the response body as JSON and returns a promise
      return response.json();
    }})
  .then(data => { // JSON data received and treated now

    let header = document.getElementById('character');
    // Update the text content of the element with the ID 'character' to the character's name
    header.textContent = `${data.name}`;
  });