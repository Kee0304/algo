let fs = require("fs");
//let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs.readFileSync("input.txt").toString().split('\n');

const [n, k] = input[0].split(" ").map(Number);
const dp = new Array(k+1).fill(0);
const coinList = new Array(n);
for (let i=1; i<n+1; i++) {
    coinList.push(Number(input[i]))
}
dp[0] = 1;

for (let coin of coinList) {
    // dp[2]는 dp[1]에서 1짜리 동전을 하나, dp[0]에서 2짜리 동전을 하나 더해서 구할 수 있다.
    // dp[7]은 dp[6]에서 1짜리 동전을 하나 dp[5]에서 2짜리 동전을 하나, dp[2]에서 5짜리 동전을 하나 더해서 만들 수 있다.
    // 즉 코인 1에 대해서 순회하면서 가능한 경우의 수를 더하고, 코인 2에 대해서 순회하면서 가능한 경우의 수를 더하고... 하면서 dp를 채운다.
    for (let j=coin; j<k+1;j++) {
        if (j-coin>=0) {
            dp[j] += dp[j-coin]
        }
    }
}

console.log(dp);