const fs = require('fs');
const stdin = (process.platform === 'linux'
    ? fs.readFileSync("/dev/stdin").toString()
    : fs.readFileSync("./input3.txt").toString()
    ).split('\n');

const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();

let t = input();

let answer = '';

while (t--) {
    const [a,b] = input().split(' ').map(Number);
    answer += (a+b).toString() + "\n"
};

console.log(answer);