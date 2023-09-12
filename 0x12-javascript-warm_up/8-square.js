#!/usr/bin/node
const arg = process.argv[2];
if (!isNaN(parseInt(arg))) {
  const square = parseInt(arg);
  for (let i = 0; i < square; i++) {
    let row = '';
    for (let i = 0; i < square; i++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
