#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const filmsData = JSON.parse(body);
    const movies = filmsData.results.filter((film) => {
      return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
    });
    console.log(movies.length || 0);
  }
});
