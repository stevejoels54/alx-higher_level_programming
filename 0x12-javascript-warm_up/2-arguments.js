#!/usr/bin/node
const argLength = process.argv.length;
console.log(argLength === 3 ? 'Argument found' : argLength >= 4 ? 'Arguments found' : 'No argument');
