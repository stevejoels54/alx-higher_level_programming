#!/usr/bin/node
const arg = process.argv[2];

function factorial (num) {
  num = parseInt(num);

  if (isNaN(num) || num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(arg));
