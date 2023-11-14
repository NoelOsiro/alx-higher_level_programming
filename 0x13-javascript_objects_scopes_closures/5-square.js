#!/usr/bin/node
import Rectangle from './4-rectangle';

module.exports = class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of the base class (Rectangle) using super()
    super(size, size);
  }
};
