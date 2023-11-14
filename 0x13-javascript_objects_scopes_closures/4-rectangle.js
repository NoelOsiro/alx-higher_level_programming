#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If w or h is 0 or not a positive integer, create an empty object
      Object.create(null);
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // Exchange the width and height
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Multiply the width and height by 2
    this.width *= 2;
    this.height *= 2;
  }
};
