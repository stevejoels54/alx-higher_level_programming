#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi.dev/api/films/';
request(url, (error, response, body) => {
  if (!error) {
    const filmsData = JSON.parse(body);
    const movie = filmsData.results.find((film) => film.episode_id === id);

    if (movie) {
      const characterUrls = movie.characters;

      characterUrls.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        });
      });
    }
  }
});
