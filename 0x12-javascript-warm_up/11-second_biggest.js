#!/usr/bin/env node
const args = process.argv;
if (args.length <= 2) {
  console.log(0);
} else {
  const sorted = args.slice(2).map(Number).sort((a, b) => b - a);
  console.log(sorted[1]);
}
