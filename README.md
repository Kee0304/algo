<details>
<summary> 230612 </summary>

# 이진 탐색 트리
## 이진 탐색 트리의 조건
- 왼쪽 자식 노드 <= 부모 자식 노드 <= 오른쪽 자식 노드
  
&nbsp;

## 이진 탐색 트리의 특징
- 중위 순회하면 오름차순으로 정렬된 리스트를 얻을 수 있다.

&nbsp;

## 구현
- 먼저 노드와 이진 탐색 클래스 작성

```python
class Node:
    def __init__(self):
        self.value = value
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self):
        self.root = None
    def setRoot(self, value):
        self.root = Node(value)
```

### 검색
1. 루트에서 시작
2. 루트와 비교해서 찾고자 하는 값이 작으면 왼쪽 자식 노드로, 크면 오른쪽 자식 노드로 이동
3. 일치하는 값이 나올 때까지 반복

```python
class binarySearchTree:
    # 찾고자 하는 값이 트리에 존재하는지 여부
    def search(self, value):
        if (self._search(self.root, value) is False):
            return False
        else:
            return True
    # 탐색
    def _search(self, currentNode, value):
        # 더 이상 노드가 없으면 탐색 실패
        if (currentNode is None):
            return False
        # 일치하는 노드가 존재하면 반환
        elif (value == currentNode.value):
            return currentNode
        # 값이 현재 노드보다 작으면 왼쪽 자식으로 가서 계속 탐색
        elif(value < currentNode.value):
            return self._search(currentNode.left, value)
        # 값이 현재 노드보다 크면 오른쪽 자식으로 가서 계속 탐색
        elif (value > currentNode.value):
            return(self._search(currentNode.right, value))
```

### 삽입

```python
class binarySearchTree:
    def insert(self, value):
        if (self.root is None):
            self.setRoot(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, currentNode, value):
        # 값이 현재 노드값보다 작은데
        if (value <= currentNode.value):
            # 현재 노드에 왼쪽 자식이 있다면
            if(currentNode.left):
                # 왼쪽 자식 노드로 이동
                self._insert(currnetNode.left, value)
            # 왼쪽 자식이 없다면
            else:
                # 삽입
                currentNode.left = Node(value)

        # 값이 현재 노드값보다 큰데
        else:
            # 오른쪽 자식이 있다면
            if(currentNode.right):
                # 오른쪽 자식 노드로 이동
                self._insert(currentNode.right, value)
            # 오른쪽 자식 없다면
            else:
                # 삽입
                currentNode.right = Node(value)
```

### 삭제
1. 삭제할 노드에 자식 노드가 없으면 그냥 삭제
2. 자식 노드가 하나 있으면
   - 해당 노드를 지우고 해당 노드의 자식 노드와 부모 노드를 연결
3. 삭제할 노드에 자식 노드가 두 개 있으면
   - predecessor: 삭제할 노드의 왼쪽 서브트리 중 최대값
   - successor: 삭제할 노드의 오른쪽 서브트리 중 최소값
    1. 삭제할 노드의 오른쪽 서브트리에서 successor를 찾는다.
    2. successor을 삭제할 노드 위치에 복사한다.
    3. successor를 삭제한다.
```python
class binarySearchTree:
    def delete(self, value):
        if (currentNode is None):
            return False
        elif value < currentNode.value:
            currentNode.left = self._delete(currentNode.left, value)
        elif value > currentNode.value:
            currentNode.right = self._delete(currentNode.right, value)
    
    def _delete(self, currentNode, value):
        # 자식 노드가 없으면 그냥 지움
        if (currentNode.left == None and currentNode.right == None):
            currentNode = None
        # 자식 노드가 하나면 자기의 부모 노드와 자기의 자식 노드를 이어줌
        elif(currentNode.left == None):
            currentNode = currentNode.right
        elif(currentNode.right== None):
            currentNode = currentNode.left

        # 삭제할 노드가 자식 노드를 두 개 가지고 있으면
        else:
            # 삭제할 노드의 오른쪽 서브트리에서 가장 작은 수를 대체자로 선정
            successor = currentNode.right
            while successor:
                successor = successor.left
                currentNode.value, successor.value = successor.value, currentNode.value
                currentNode.left = self._delete(currentNode.left, successor.value)

        return currentNode

```

</details>


<details>
<summary> 230614 </summary>

# 파이썬 list 연산에 따른 시간 복잡도
## 시간 복잡도가 O(1)인 연산
- len(lst)
- lst[index]
- lst.append(el)
- lst.pop()

## 시간 복잡도가 O(k)인 연산
- lst[i:j]

## 시간 복잡도가 O(n)인 연산
- el in lst
- lst.count(el)
- lst.index(el)
- el.pop(0)
  - 맨 앞에 있는 값을 빼기 위해 전체 복사를 한 번 한다.
  - deque.popleft()는 시간 복잡도가 O(1)으로, 리스트의 맨 앞 요소를 뺄 일이 있으면 deque를 사용하는 것이 좋은 편이다.
- del lst[i]
- min, max
- lst.reverse()

## 시간 복잡도가 O(nlogn)인 연산
- lst.sort()

&nbsp;


# 앞에 걸 뺀다고 무조건 deque를 쓰는 게 좋을까?
- 앞서 맨 앞에 있는 것을 뺄 때에는 deque를 사용하는 것을 권장한다고 했는데, 무조건 그런 것은 아니다.
- 만약 양쪽에서 넣고 뺄 일이 있다면 deque를 사용하는 것이 더 효율적이지만, 만약 한 쪽에서만 계속 뺄 것이라면 차라리 리스트를 한 번뒤집고 pop()을 하는 것이 더 짧은 시간이 걸릴 수도 있다.

</details>

<details>
<summary> 230719</summary>

# js로 알고리즘 문제 풀기 기초
## 입력받기
- readline와 fs 중 기본적으로 fs를 쓴다
- 빠르고, 알고리즘 문제 풀이에는 정해진 입력값만 입력 받으면 되기 때문

## 코드
```javaScript
// fs모듈 import
const fs = require('fs');
const stdin = fs.readFileSync("test.txt").toString().split("\n");

// 실행될 때마다 stdin을 한 줄씩 반환하는 함수
const input = (() => {
    let line = 0;
    return () => stdin[line++];
})();
```

### 예제
1. 테스트 케이스 수가 주어지고, 각 테스트 케이스 별로 두 개의 문자열 숫자가 띄어쓰기로 구분되어 입력될 때, 각각 두 수의 합을 출력하는 코드
```javaScript
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
```

2. 테스트 케이스 수는 주어지지 않고, 숫자의 개수와 테스트 케이스 개수가 주어지고 숫자의 개수만큼 숫자를, 테스크 케이스 숫자만큼 두 개의 숫자가 띄어쓰기로 주어졌을 때 부분합을 구하는 문제
```javaScript
const fs = require('fs');
const stdin = (process.platform === "linux"
    ? fs.readFileSync('/dev/stdin').toString()
    : fs.readFileSync('./input2.txt').toString()
).split('\n');

const input = (() => {
    let line = 0;
    return () => stdin[line++]
})();

const [N, M] = input().split(" ").map(Number);
const numlst = input().split(" ").map(Number);
const sumlst = []

for (let i = 0; i < N; i++) {
    if (i === 0) {
        sumlst[i] = numlst[i];
    } else {
        sumlst[i] = sumlst[i-1]+numlst[i];
    }
};

let answer = '';

for (let m = 1; m <= M; m++) {
    let [st, en] = input().split(" ").map(Number);
    if (st === 1) {
        answer += sumlst[en-1].toString() + "\n";
    } else {
        answer += (sumlst[en-1] - sumlst[st-2]).toString() + "\n";
    }
};

console.log(answer)
```

## 출력할 때 주의사항
- 테스트 케이스마다 매번 답을 console.log로 출력하면 시간이 타이트하게 주어진 문제에선 시간 초과가 날 수도 있다.
- 위의 예제 처럼 answer이라는 빈 문자열에 답을 문자열로 하나씩 추가하고 마지막에 한 번에 출력하는 게 시간이 조금 덜 걸린다.

</details>

<details>
<summary> 230614 </summary>

# 파이썬 list 연산에 따른 시간 복잡도
## 시간 복잡도가 O(1)인 연산
- len(lst)
- lst[index]
- lst.append(el)
- lst.pop()

## 시간 복잡도가 O(k)인 연산
- lst[i:j]

## 시간 복잡도가 O(n)인 연산
- el in lst
- lst.count(el)
- lst.index(el)
- el.pop(0)
  - 맨 앞에 있는 값을 빼기 위해 전체 복사를 한 번 한다.
  - deque.popleft()는 시간 복잡도가 O(1)으로, 리스트의 맨 앞 요소를 뺄 일이 있으면 deque를 사용하는 것이 좋은 편이다.
- del lst[i]
- min, max
- lst.reverse()

## 시간 복잡도가 O(nlogn)인 연산
- lst.sort()

&nbsp;


# 앞에 걸 뺀다고 무조건 deque를 쓰는 게 좋을까?
- 앞서 맨 앞에 있는 것을 뺄 때에는 deque를 사용하는 것을 권장한다고 했는데, 무조건 그런 것은 아니다.
- 만약 양쪽에서 넣고 뺄 일이 있다면 deque를 사용하는 것이 더 효율적이지만, 만약 한 쪽에서만 계속 뺄 것이라면 차라리 리스트를 한 번뒤집고 pop()을 하는 것이 더 짧은 시간이 걸릴 수도 있다.

</details>

<details>
<summary> 230721</summary>

# js로 알고리즘 문제 풀기 기초
## 참조 문제
- 문제를 풀다가 Set 안에 Array를 넣고 싶었다. 그래서 생각 없이 그냥 넣어봤다.
```javaScript
for (let row = 0; row < maxRow; row++) {
    for (let col = 0; col < maxCol; col++) {
        let stack = [];
        let visited = new Set();
        if (mat[row][col] == 1 && visited.has([row,col]) === false) {
            visited.add([row,col]);
            stack.push([row,col]);
            while (true) {
                if (stack.length === 0) {
                    break;
                }
                let [curRow, curCol] = stack.pop();

                for (let d = 0; d < 4; d++) {
                    if (0<=curRow+drow[d] && curRow+drow[d] < maxRow && 0<=curCol+dcol[d] && curCol+dcol[d] < maxCol) {
                        if (mat[curRow+drow[d]][curCol+dcol[d]] == 1 && visited.has([curRow+drow[d],curCol+dcol[d]]) === false) {
                            stack.push([curRow+drow[d],curRow+drow[d]]);
                            visited.add([curRow+drow[d],curRow+drow[d]]);
                        }
                    }    
                }
            }
        }
        anset.add(visited.length);
    }
};
```
- 무한 루프를 돈다. 사실 생각해보면 python에서도 set 안에 list를 넣지 못하게 한다.
- 결국 내용물만 같지 실제로는 다른 메모리 상에 존재하는 두 리스트이기 때문에 Set에 같은 놈이 여러 개 들어가있는 것 처럼 보인다.
- 이러한 상황을 피하기 위해선 Set 안에 넣을 것은 immutable한 놈들로 제한하는 것이 좋다. 예를 들어 문자열로 변환해서 저장하자.
</details>

<details>
<summary> 230724</summary>

# 파이썬 입력
- 저번 js 알고리즘 문제 풀이때와 비슷하게, 이번엔 파이썬에서 입력 시간으로 인해 시간 초과가 뜨는 일이 발생하였다.
- 보통 input()으로 매번 입력을 받았는데, 이는 잘못된 선택이었다.
- `input = sys.stdin.readline`과 같이 sys.stdin.readline을 이용하는 것이 입력 시간을 단축하는 방법이다.
## 예제
```python
import sys
inp = sys.stdin.readline

T = int(input())
```
</details>

<details>
<summary> 230724</summary>

# 자체 지원 함수와 수동 계산
- 파이썬 뿐만이 아니라 언어에서 자체적으로 지원하는 문법들의 경우 수동으로 계산하는 것보다 최적화 되어있다.
- 230807의 두 코드는 기본적으로 같은 동작을 수행하지만 생각보다 큰 시간의 차이가 난다.  
</details>


<details>
<summary> 230904</summary>

# 트리의 지름 구하기
- 노드와 간선들의 정보가 주어졌을 때, 트리의 지름을 구해야할 때가 있다.
- 트리의 지름은 임의의 두 노드 사이의 거리 중 가장 먼 거리를 뜻한다.
- 임의의 점에서 시작하여 가장 먼 노드를 찾자. 해당 노드는 지름이 되는 두 노드 중 한 노드일 것이다.
- 따라서 해당 노드에서 다시 가장 먼 노드를 찾으면 지름을 구할 수 있다.
</details>