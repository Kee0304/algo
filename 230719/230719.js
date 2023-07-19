const fs = require('fs');
// 리눅스 환경에선 "/dev/stdin"으로 콘솔입력과 같이 입력을 받을 수 있다.
const stdin = (process.platform === 'linux'
    ? fs.readFileSync("/dev/stdin").toString()
    : fs.readFileSync("./input.txt").toString()
    ).split('\n');

const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();

// 첫 input() 실행 시 테스트 케이스 반환
let t = input();

// 다음부터는 input() 실행 시 각 테스트 케이스 반환
while (t--) {
    const [a,b] = input().split(' ').map(Number);
    console.log(a + b);
};