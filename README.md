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