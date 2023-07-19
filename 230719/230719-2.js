const fs = require('fs');
const stdin = (process.platform === "linux"
    ? fs.readFileSync('/dev/stdin').toString()
    : fs.readFileSync('./input2.txt').toString()
).split('\n');

const input = (() => {
    let line = 0;
    return () => stdin[line++]
})();

const [N, M] = input().split(" ").map(Number);
const numlst = input().split(" ").map(Number);
const sumlst = []

for (let i = 0; i < N; i++) {
    if (i === 0) {
        sumlst[i] = numlst[i];
    } else {
        sumlst[i] = sumlst[i-1]+numlst[i];
    }
};

let answer = '';

for (let m = 1; m <= M; m++) {
    let [st, en] = input().split(" ").map(Number);
    if (st === 1) {
        answer += sumlst[en-1].toString() + "\n";
    } else {
        answer += (sumlst[en-1] - sumlst[st-2]).toString() + "\n";
    }
};

console.log(answer)