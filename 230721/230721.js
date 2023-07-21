const fs = require('fs');

const stdin = (process.platform === 'linux'
    ? fs.readFileSync("/dev/stdin").toString()
    : fs.readFileSync("./input.txt").toString()
    ).split('\n');


const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();

const [N, M, T] = input().split(" ").map(Number);
let mat = new Array();

// 원판
for (let i = 0; i < N; i++) {
    mat.push(input().split(" ").map(Number));
};

const drow = [-1,0,1,0]
const dcol = [0,1,0,-1]

const rotate = ((numbers, d) => {
    if (d === 0) {
        const lastNum = numbers.pop();
        numbers.unshift(lastNum);
        return;
    } else {
        const firstNum = numbers.shift();
        numbers.push(firstNum);
        return;
    }
});

let allSum = 0;

// 회전
for (let t = 0; t < T; t++) {
    let [x, d, k] = input().split(" ").map(Number);
    // 배수 원판 회전
    for (let i = 1; x*i-1 < N; i++) {
        for (let _ = 0; _<k; _++) {
            rotate(mat[x*i-1], d)
        }
    }
    let middleSum = 0;
    let toDelete = new Set();
    let visited = new Set();
    let numNum = 0;
    for (let row = 0; row < N; row++) {
        for (let col = 0; col <M; col++) {
            if (mat[row][col] !== 0) {
                middleSum += mat[row][col];
                numNum+=1;
                // 방문한 적 없는 점이면 인접한 점을 탐색
                if (!visited.has(`${row},${col}`)) {
                    stack = [[row,col]];
                    visited.add(`${row},${col}`)
                    while (stack.length >= 1) {
                        for (let _ = 0; _<stack.length; _++) {
                            const point = stack.pop();
                            for (let d = 0; d<4; d++) {
                                // 다음 점을 보는데
                                let [newRow, newCol] = [point[0]+drow[d], point[1]+dcol[d]];
                                // row는 항상 범위 안에 존재해야하지만
                                if (0<=newRow && newRow<N) {
                                    //col은 원형이므로 범위 벗어낫으면 인덱스 수정
                                    if (newCol == M) {
                                        newCol = 0;
                                    }
                                    if (newCol == -1) {
                                        newCol = M-1;
                                    }
                                    let forSize = toDelete.size;
                                    // 인적한 점이 방문한 적 없는데 같으면 삭제할 리스트에 추가, 스택에 추가, 방문 표시
                                    if (!visited.has(`${newRow},${newCol}`) && (mat[point[0]][point[1]] == mat[newRow][newCol])) {
                                        toDelete.add(`${newRow},${newCol}`);
                                        stack.push([newRow,newCol]);
                                        visited.add(`${newRow},${newCol}`);
                                    }
                                    if (forSize < toDelete.size) {
                                        toDelete.add(`${point[0]},${point[1]}`);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    if (toDelete.size != 0) {
        for (let del of toDelete) {
            lstdel = del.split(",").map(Number);
            middleSum -= mat[lstdel[0]][lstdel[1]];
            mat[lstdel[0]][lstdel[1]] = 0;
        }
    } else {
        const avg = middleSum / numNum;
        for (let row = 0; row < N; row++) {
            for (let col = 0; col < M; col++) {
                if (mat[row][col] !== 0) {
                    if (mat[row][col] < avg) {
                        mat[row][col] +=1;
                        middleSum+=1;
                    } else if (mat[row][col] > avg) {
                        mat[row][col] -=1;
                        middleSum-=1;
                    }
                }
            }
        } 
    }

    allSum = middleSum;
    
};



console.log(allSum);