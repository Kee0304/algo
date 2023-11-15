//const fs = require('fs');
//const path = './input.txt'

const readline = require("readline");
const rl = readline.createInterface({
    //input:fs.createReadStream(path),
    input: process.stdin,
    output: process.stdout
})
const input = [];

rl.on("line", function (line) {
    input.push(line)
}).on("close", function() {
    const T = Number(input[0]);
    let ans = "";
    for (let t=1; t<T+1; t++) {
        const n = Number(input[3*t-2]);
        const stickers = [];
        const stickers1 = input[3*t-1].split(" ").map(Number);
        const stickers2 = input[3*t].split(" ").map(Number);
        stickers.push(stickers1);
        stickers.push(stickers2);
        const dp = Array.from(Array(2), () => Array(n).fill(0));
        for (let col=0; col<=n-1; col++) {
            for (let row=0; row<2; row++) {
                if (col === 0 ) {
                    dp[row][col] = stickers[row][col];
                } else if (col == 1) {
                    if (row === 0) {
                        dp[row][col] = dp[row+1][col-1]+stickers[row][col];
                    } else {
                        dp[row][col] = dp[row-1][col-1]+stickers[row][col];
                    }
                } else {
                    if (row === 0) {
                        dp[row][col] = Math.max(
                            dp[row+1][col-1] + stickers[row][col],
                            dp[row][col-2] + stickers[row][col],
                            dp[row+1][col-2] + stickers[row][col]
                            );
                    } else {
                        dp[row][col] = Math.max(
                            dp[row-1][col-1] + stickers[row][col],
                            dp[row][col-2] + stickers[row][col],
                            dp[row-1][col-2] + stickers[row][col]
                        );
                    }
                }
            }
        }
        ans += `${Math.max(dp[0][n-1],dp[1][n-1])}\n`;
    }
    console.log(ans);
    process.exit();
})