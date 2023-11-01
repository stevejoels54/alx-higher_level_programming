$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (payload) {
    $('DIV#hello').text(payload.hello);
  });
});
