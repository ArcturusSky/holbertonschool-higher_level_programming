// Script  that fetches and lists the title for all movies from the specified URL
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    // Check if the response was successful
    if (response.ok) {

      // The response.json() method parses the response body as JSON and returns a promise
      return response.json();
    }})
  .then(data => { // JSON data received and treated now
    let MovieArray = data.results // Selecting the array "results" in the JSON data received
    
    // Going through the array and for each element in the array, adding a node and title to the list
    MovieArray.forEach(element => {
        let ulBalises = document.querySelector('ul');
        let MovieList = document.createElement('li');
        MovieList.textContent = element.title;
        ulBalises.appendChild(MovieList)
    });
  });
