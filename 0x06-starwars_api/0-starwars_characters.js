#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

if (process.argv.length > 2) {
  // get characters' url
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const charactersUrl = JSON.parse(body).characters;

      // fetch characters' name by using Promise for each character's url
      const characterName = charactersUrl.map(url => new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          } else {
            reject(error);
          }
        });
      }));

      // get names in order by waiting for all the Promises to finish
      Promise.all(characterName)
        .then(names => console.log(names.join('\n')))
        .catch(allError => console.log(allError));
    } else {
      console.log(error);
    }
  });
}
