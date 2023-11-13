#!/usr/bin/node
const numArgs = process.argv.length;
console.log(numArgs < 3 ? 'No argument' : process.argv[2]);
