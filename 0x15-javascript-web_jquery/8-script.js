$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (payload) {
  $('UL#list_movies').append(...payload.results.map(movie => `<li>${movie.title}</li>`));
});
