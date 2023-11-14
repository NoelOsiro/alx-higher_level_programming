#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // Use the filter method to count occurrences
  const occurrences = list.filter(element => element === searchElement);
  return occurrences.length;
};
