#!/usr/bin/node
const fs = require('fs');
const source1 = fs.readFileSync(process.argv[2], 'utf8');
const source2 = fs.readFileSync(process.argv[3], 'utf8');
const destination = process.argv[4];
fs.writeFileSync(destination, source1 + source2);
