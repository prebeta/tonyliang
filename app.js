var express = require('express');
var favicon = require('serve-favicon');
var app = express();

app.use(favicon(__dirname + '/public/images/favicon.ico'));
app.use('/', express.static(__dirname + '/public'));

app.listen(3000, function () {
  console.log('Personal website listening on port 3000!');
});