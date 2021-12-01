#!/usr/bin/node
// a function that prints the number of arguments already printed and the new argument value. 
let argument = 0;
exports.logMe = function (item) {
  console.log(argument + ': ' + item);
  argument += 1;
};
