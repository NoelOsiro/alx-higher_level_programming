// File: 102-concat.js
const fs = require('fs');

const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

const fileContent1 = fs.readFileSync(sourceFile1, 'utf-8');
const fileContent2 = fs.readFileSync(sourceFile2, 'utf-8');
const concatenatedContent = fileContent1 + fileContent2;

fs.writeFileSync(destinationFile, concatenatedContent);
