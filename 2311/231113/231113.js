let fs = require("fs");
//let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let input = fs.readFileSync("input.txt").toString().split('\n');

// 힙
class Heap {
    constructor() {
      this.items = [];
    }
    swap(index1, index2) {
      let temp = this.items[index1];
      this.items[index1] = this.items[index2];
      this.items[index2] = temp;
    }
    parentIndex(index) {
      return Math.floor((index - 1) / 2);
    }
    leftChildIndex(index) {
      return index * 2 + 1;
    }
    rightChildIndex(index) {
      return index * 2 + 2;
    }
    parent(index) {
      return this.items[this.parentIndex(index)];
    }
    leftChild(index) {
      return this.items[this.leftChildIndex(index)];
    }
    rightChild(index) {
      return this.items[this.rightChildIndex(index)];
    }
    peek() {
      return this.items[0];
    }
    size() {
      return this.items.length;
    }
  }


class MinHeap extends Heap {
    // 노드가 삽입 되었을 때 다시 최소힙으로 만들기 위해 노드들을 교환하면서 작은 값을 위로 올림
    bubbleUp() {
        let index = this.items.length-1;
        // 부모보다 작을 때 까지 계속 올림
        // 이 문제의 경우 거리(가중치)
        while (
            this.parent(index) !== undefined &&
            this.parent(index)[1] > this.items[index][1]
          ) {
            this.swap(index, this.parentIndex(index));
            // 인덱스 갱신
            index = this.parentIndex(index);
        }
    }

    // 노드를 삭제할 때 루트 노드를 삭제하고 맨 마지막에 삽입했던 노드를 위로 올린 후 다시 최소힙이 되도록 교환
    bubbleDown() {
        let index = 0
        // 노드가 좌우 자식들보다 크면 교환
        while (
            this.leftChild(index) !== undefined
          ) {
            // 일단 임시로 왼쪽 자식 노드라고 하고
            let smallerIndex = this.leftChildIndex(index);
            // 최소힙은 왼쪽자식 노드 < 오른쪽 자식 노드이다.
            if (this.rightChild(index) !== undefined) {
                if (this.rightChild(index)[1] < this.items[smallerIndex][1]) {
                    smallerIndex = this.rightChildIndex(index);
                }
                }
            if (this.items[index][1] > this.items[smallerIndex][1] )   
              this.swap(index, smallerIndex);
              index = smallerIndex;
        }
    }

    // 아이템 추가
    push(item) {
        this.items[this.items.length] = item;
        this.bubbleUp();
      }

    // 아이템 삭제
    pop() {
            let item = this.items[0];
            // 맨 마지막 노드에 있는 아이템을 루트로 복사
            this.items[0] = this.items[this.items.length - 1];
            // 맨 마지막 노드 삭제
            this.items.pop();
            this.bubbleDown();
    
            return item;
        
    }
    
    sort() {
        let sort = [];
        const count = this.items.length;
        for (let i=0; i<count; i++) {
            sort.push(this.poll());
        }
        return sort;
    }
}


const VandE = input[0].split(" ");
const V = Number(VandE[0]);
const E = Number(VandE[1]);
const K = Number(input[1]);
const obj = new Object();


for (let i = 2; i < 2+E; i++) {
    let adj = input[i].split(" ");
    const start = Number(adj[0]);
    const end = Number(adj[1]);
    const weight = Number(adj[2]);

    if (obj.hasOwnProperty(start) == true) {
        obj[start].push([end, weight]);
    } else {
        obj[start] = [[end, weight]];
    }
}

mh = new MinHeap();
const distance = new Array(V+1).fill(Number.POSITIVE_INFINITY);
distance[K] = 0;
mh.push([K, 0]);
const visited = new Set();

while (mh.size()) {
    // 최소 힙을 사용하였으므로
    const [curNode, dist] = mh.pop();
    
    if (visited.has(curNode)) {
        continue;
    }

    if (obj[curNode] === undefined) {
        continue;
    }

    visited.add(curNode);
    // 현재 노드에서 도달할 수 있는 노드들에 대해
    for (let [nextNode, nextDist] of obj[curNode]) {
        // 여태까지 최단 거리와 지금 노드에서 갈 때의 거리를 비교하여
        // 지금 노드에서 갈 때가 더 거리가 짧으면 이동
        if (distance[nextNode] > distance[curNode] + nextDist) {
            distance[nextNode] = distance[curNode] + nextDist;
            mh.push([nextNode, distance[nextNode]])
        }
    }
}

ans = "";

for (let i=0; i<V; i ++) {
    let d = distance[i+1]
    if (d === Infinity) {
        ans += `INF\n`
    } else {
        ans += `${distance[i+1]}\n`
    }
}

console.log(ans)