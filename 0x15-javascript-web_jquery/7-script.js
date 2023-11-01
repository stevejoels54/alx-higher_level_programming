$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (payload) {
  $('DIV#character').text(payload.name);
});
