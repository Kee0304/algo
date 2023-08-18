const fs = require('fs');

const stdin = (process.platform === 'linux'
    ? fs.readFileSync("/dev/stdin").toString()
    : fs.readFileSync("./input.txt").toString()
    ).split('\n');


const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();

// N: 정점의 수 M: 간선의 수 R: 시작 정점
const [N, M, R] = input().split(" ").map(Number);

const adjList = new Array(N+1);
const orderList = new Array(N+1);
const visited = new Set();
let answer = '';

// 인덱스와 정점 번호를 맞춘 리스트에 저장
for (let i = 0; i < M; i++) {
    let [s,e] = input().split(" ").map(Number);
    if (adjList[s] === undefined) {
        adjList[s] = [e];
        if (adjList[e] === undefined) {
            adjList[e] = [s];
        } else {
            if (adjList[e].includes(s) === false) {
                adjList[e].push(s);
            }
        }
    } else {
        if (adjList[s].includes(e) === false) {
            adjList[s].push(e);
        }
        if (adjList[e] === undefined) {
            adjList[e] = [s];
        } else {
            if (adjList[e].includes(s) === false) {
                adjList[e].push(s);
            }
        }
    }
};

// 각 리스트 오름차순 배열
for (let i = 1; i < N+1; i++) {
    if (adjList[i] != undefined) {
        adjList[i].sort((a,b) => {
            return a-b;
        });
    }
};

let cnt = 1;

// 탐색 함수
const dfs = ((point) => {
    orderList[point] = cnt
    // 더 이상 방문할 수 없는 점이 없으면
    if ((adjList[point] === undefined) || (adjList[point].length === 0)) {
        return;
    } else {
        // 가장 큰 점이 방문한 적 있는지 확인하고 아니면 그보다 작은 점 체크
        while (adjList[point].length >= 1) {
            // 인접한 점 중 가장 큰 점으로 간다
            let nextpoint = adjList[point].pop();
            // 방문한 적없는 점이냐?
            if (visited.has(nextpoint) === false) {
                visited.add(nextpoint);
                cnt += 1;
                dfs(nextpoint);
            }
        }

        return;
    };
});

// 처음 점을 set에 추가해주고 탐색 시작
visited.add(R);
dfs(R);

// 각 점들의 방문 순서 및 0 표시
for (let i=1; i<N+1; i++) {
    if (orderList[i] === undefined) {
        answer += '0\n'
    } else { 
        answer += `${orderList[i]}\n`
    }
}

console.log(answer);