#!/usr/bin/node
const request = require('request');
const link = process.argv[2];
const output = {};
request(link, function (error, response, body) {
  if (error) throw error;
  const data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    if (data[i].output === true) {
      if (output[data[i].userId]) {
        output[data[i].userId] += 1;
      } else {
        output[data[i].userId] = 1;
      }
    }
  }
  console.log(output);
});
