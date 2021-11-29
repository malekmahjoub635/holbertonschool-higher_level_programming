#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const sbi = process.argv.slice(2, process.argv.length);
  sbi.sort(function (a, b) { return a - b; });
  console.log(sbi[sbi.length - 2]);
}
