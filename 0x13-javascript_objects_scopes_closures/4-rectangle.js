#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let r = 0; r < this.height; r++) console.log('X'.repeat(this.width));
  }

  rotate () {
    const r1 = this.height;
    this.height = this.width;
    this.width = r1;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
