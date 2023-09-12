#!/usr/bin/node
const argument1 = process.argv[2] || 'undefined';
const argument2 = process.argv[3] || 'undefined';

function add (a, b) {
  const sum = parseInt(a) + parseInt(b);
  console.log(sum);
}

add(argument1, argument2);
