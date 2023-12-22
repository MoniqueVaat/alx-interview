#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, (err, res) => {
  if (err) {
    console.error(err);
    return;
  }

  const { characters } = JSON.parse(res.body);

  const printCharacterNames = async () => {
    for (const character of characters) {
      // eslint-disable-next-line no-await-in-loop
      await new Promise((resolve, reject) => {
        request(character, (err, res) => {
          if (err) {
            reject(err);
          }

          const characterNames = JSON.parse(res.body).name;
          console.log(characterNames);
          resolve();
        });
      });
    }
  };
  printCharacterNames();
});
