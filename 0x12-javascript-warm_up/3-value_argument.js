#!/usr/bin/node
const numArgs = process.argv.length;
if (numArgs < 3) {
  console.log('No Arguement');
} else {
  console.log(process.argv[2]);
}
