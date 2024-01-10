#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  try {
    const title = JSON.parse(body).title;
    console.log(title);
  } catch (parseError) {
    console.error('Error parsing response:', parseError);
    process.exit(1);
  }
});
