#!/usr/bin/node
import Square from './5-square.js';

module.exports = class NewSquare extends Square {
  charPrint (c) {
    // If c is undefined, use the character 'X'
    const charToPrint = c || 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(charToPrint.repeat(this.width));
    }
  }
};
