const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let ans = 0;
let input = [];
rl.on('line', (line) => {
    input = line.split(' ').map(Number);
    rl.close();
}).on('close', () => {
    const N = input[0];
    const K = input[1];
    const lst = [[N,0]];
    const visited = new Set();

    while (lst.length) {
        let cur = lst.shift();
        
        let walkfront = [cur[0]+1,cur[1]+1];
        let walkback = [cur[0]-1,cur[1]+1];
        let teleport = [cur[0]*2,cur[1]];

        if (teleport[0] === K) {
            ans = teleport[1];
            break;
        } else {
            if (visited.has(teleport[0]) == false)  {    
                lst.unshift(teleport);
                visited.add(teleport[0]);
            };
        }

        if (walkfront[0] === K) {
            ans = walkfront[1];
            break;
        } else {
            if (visited.has(walkfront[0]) == false) {
                lst.push(walkfront);
                visited.add(walkfront[0])
            };
        }

        if (walkback[0] === K) {
            ans = walkback[1];
            break;
        } else {
            if (visited.has(walkback[0]) == false) {
                lst.push(walkback);
                visited.add(walkback[0])
            };
        }
    };
    console.log(ans);
    process.exit();
});