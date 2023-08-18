const fs = require('fs');

const stdin = (process.platform === 'linux'
    ? fs.readFileSync("/dev/stdin").toString()
    : fs.readFileSync("./input2.txt").toString()
    ).split('\n');


const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();

// N: 끊어진 기타줄의 개수 M: 브랜드 개수
const [N, M] = input().split(" ").map(Number);
let minsix = 6001;
let minone = 1001;
for (let i=0; i < M; i++) {
    // 6개 들이 가격과 1개 가격
    const [six, one] = input().split(" ").map(Number);
    
    if (minsix > six) {
        minsix = six;
    }

    if (minone > one) {
        minone = one;
    }
};

let money = 0;

// 6개 들이보다 단품이 더 싸면 다 단품으로 사면 된다
if (minsix > minone*6) {
    money += minone*N;

// 6개 들이가 더 싸면 6의 배수까지는 다 6개로 사고 나머지는 비교해서 산다
} else {
    pile = parseInt(N/6);
    money += pile*minsix;
    lest = N%6;
    if (minsix > minone*lest) {
        money += minone*lest;
    } else {
        money += minsix;
    }
}

console.log(money);