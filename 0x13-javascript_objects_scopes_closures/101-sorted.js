#!/usr/bin/node
const { dict } = require('./101-data.js');

const sortedDict = Object.entries(dict).reduce((acc, [key, value]) => {
  acc[value] = acc[value] || [];
  acc[value].push(key);
  return acc;
}, {});

console.log(sortedDict);
