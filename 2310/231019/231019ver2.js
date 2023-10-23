const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

class Queue {
    constructor() {
        this.storage = {};
        this.front = 0;
        this.rear = 0;
    };

    size() {
        if (this.storage[this.rear] === undefined) {
            return 0;
        } else {
            return this.rear - this.front +1;
        }
    };

    push(value) {
        if (this.size()===0) {
            this.storage['0'] = value;
        } else {
            this.rear +=1;
            this.storage[this.rear] = value;
        }
    }

    popleft() {
        let temp;

        if (this.front === this.rear) {
            temp = this.storage[this.front];
            delete this.storage[this.front];

            this. front = 0;
            this. rear = 0;
        } else {
            temp = this.storage[this.front];
            delete this.storage[this.front];
            this.front +=1;
        }
        return temp;
    }
}

let input = [];
rl.on('line', (line) => {
    input = line.split(' ').map(Number);
    rl.close();
}).on('close', () => {
    const N = input[0];
    const K = input[1];
    const visited = new Set();

    const dq = new Queue();
    dq.push([N,0]);

    while (dq.size()) {
        const cur = dq.popleft();

        let walkfront = [cur[0]+1,cur[1]+1];
        let walkback = [cur[0]-1,cur[1]+1];
        let teleport = [cur[0]*2,cur[1]];

        if (teleport[0] === K) {
            ans = teleport[1];
            break;
        } else {
            if (visited.has(teleport[0]) == false)  {    
                dq.push(teleport);
                visited.add(teleport[0]);
            };
        }

        if (walkfront[0] === K) {
            ans = walkfront[1];
            break;
        } else {
            if (visited.has(walkfront[0]) == false) {
                dq.push(walkfront);
                visited.add(walkfront[0])
            };
        }

        if (walkback[0] === K) {
            ans = walkback[1];
            break;
        } else {
            if (visited.has(walkback[0]) == false) {
                dq.push(walkback);
                visited.add(walkback[0])
            };
        }
    };
    console.log(ans);
    process.exit();
});