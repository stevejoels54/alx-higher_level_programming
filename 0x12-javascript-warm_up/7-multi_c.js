#!/usr/bin/node
const arg = process.argv[2];
if (!isNaN(parseInt(arg))) {
  const times = parseInt(arg);
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
