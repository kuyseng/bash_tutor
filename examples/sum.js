#!/usr/local/opt/node@12/bin/node

console.log("argv", process.argv)

const args = process.argv.slice(2).map(i=> parseInt(i));

const sum = args.reduce((a,b) => a+b)

console.log(`${args.join('+')} = ${sum}`)
