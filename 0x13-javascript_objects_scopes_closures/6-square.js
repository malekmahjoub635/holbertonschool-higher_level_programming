#!/usr/bin/node
const sq = require('./5-square');
module.exports = class Square extends sq {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let s = 0; s < this.height; s++) console.log(c.repeat(this.width));
    }
  }
};
