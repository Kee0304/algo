let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

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

// 중간값보다 큰 수들의 집합인 최소힙(루트가 가장 작은 수)
class MinHeap extends Heap {
    // 노드가 삽입 되었을 때 다시 최소힙으로 만들기 위해 노드들을 교환하면서 작은 값을 위로 올림
    bubbleUp() {
        let index = this.items.length-1;
        // 부모보다 작을 때 까지 계속 올림
        while (
            this.parent(index) !== undefined &&
            this.parent(index) > this.items[index]
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
            this.leftChild(index) !== undefined &&
            (this.leftChild(index) < this.items[index] ||
              this.rightChild(index) < this.items[index])
          ) {
            // 일단 임시로 왼쪽 자식 노드라고 하고
            let smallerIndex = this.leftChildIndex(index);
            // 최소힙은 왼쪽자식 노드 < 오른쪽 자식 노드이다.
            if (
                this.rightChild(index) !== undefined &&
                this.rightChild(index) < this.items[smallerIndex]
              ) {
                smallerIndex = this.rightChildIndex(index);
              }
              this.swap(index, smallerIndex);
              index = smallerIndex;
        }
    }

    // 아이템 추가
    add(item) {
        this.items[this.items.length] = item;
        this.bubbleUp();
      }

    // 아이템 삭제
    poll() {
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

// add poll sort를 재사용하기 위해 상속
// 나머지는 오버라이딩
class MaxHeap extends MinHeap{
    bubbleUp() {
        let index = this.items.length -1;
        // 최대 힙이므로 큰 값을 위로 올림
        while (
            this.parent(index) !== undefined &&
            this.parent(index) < this.items[index]
          ) {
            this.swap(index, this.parentIndex(index));
            index = this.parentIndex(index);
          }
    }


    // 삭제 했을 때 
    bubbleDown() {
        let index = 0;
        while (
          this.leftChild(index) !== undefined &&
          (this.leftChild(index) > this.items[index] ||
            this.rightChild(index) > this.items[index])
        ) {
          let largerIndex = this.leftChildIndex(index);
          if (
            this.rightChild(index) !== undefined &&
            this.rightChild(index) > this.items[largerIndex]
          ) {
            largerIndex = this.rightChildIndex(index);
          }
          this.swap(index, largerIndex);
          index = largerIndex;
        }
      }
}

class MedianHeap {
    constructor() {
      this.minheap = new MinHeap();
      this.maxheap = new MaxHeap();
    }
    add(value) {
      if (value > this.median()) {
        this.minheap.add(value);
      } else {
        this.maxheap.add(value);
      }
  
      if (this.minheap.size() - this.maxheap.size() > 1) {
        this.maxheap.add(this.minheap.poll());
      }
      if (this.maxheap.size() - this.minheap.size() > 1) {
        this.minheap.add(this.maxheap.poll());
      }
    }
    median() {
      if (this.minheap.size() === 0 && this.maxheap.size() === 0) {
        return Number.NEGATIVE_INFINITY;
      } else if (this.minheap.size() === this.maxheap.size()) {
        return Math.min(this.minheap.peek(), this.maxheap.peek());
      } else if (this.minheap.size() > this.maxheap.size()) {
        return this.minheap.peek();
      } else {
        return this.maxheap.peek();
      }
    }
  }

const answer = [];
const N = Number(input[0]);
input.shift();
const medianHeap = new MedianHeap();
for (let i = 0; i < N; i++) {
    medianHeap.add(Number(input[i]));
    answer.push(medianHeap.median());
  }
console.log(answer.join("\n"));