#!/usr/bin/node
const argument = process.argv[2];
console.log(typeof argument === 'undefined' ? 'No argument' : argument);
