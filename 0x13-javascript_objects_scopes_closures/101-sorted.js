// File: 101-sorted.js
const { dict } = require('./101-data');

const sortedDict = Object.entries(dict).reduce((acc, [key, value]) => {
  acc[value] = acc[value] || [];
  acc[value].push(key);
  return acc;
}, {});

console.log(sortedDict);
