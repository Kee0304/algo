adjList = [
    [2,5],
    [2,3,4],
    [1,5],
    [1,2,5],
    [2]
]

# 오른쪽 노드 기준으로 자신을 선택한 왼쪽 노드를 저장
selected = [-1]*(5+1)

def bimatch(node):

    if visited[node]:
        return False
    visited[node] = True
    # 왼쪽 노드에서 연결된 오른쪽 노드들을 탐색
    for num in adjList[node]:
        # 해당 오른쪽 노드를 선택한 왼쪽 노드가 없거나
        # 그 왼쪽 노드가 다른 놈을 선택할 수 있으면
        # num을 선택하고 끝
        # 어떤 왼쪽 노드가 해당 오른쪽 노드를 선택했으면 selected[num]이 -1이 아니게 되니까 if 에 걸리지 않음
        if selected[num] == -1 or bimatch(selected[num]):
            selected[num] = node
            print(f'왼쪽 노드 {node}가 오른쪽 노드 {num} 선택')
            print(f'현재 선택한 왼쪽 노드들 {selected}')
            return True
    
    # 아무것도 선택할 수 없었다.
    return False

for i in range(5): 
    # 왼쪽 노드 방문 여부 표시
    visited = [False]*(5)
    bimatch(i)

ans = 0
for i in range(1, 5+1):
    if selected[i] >= 0:
        ans +=1

print(selected)
print(ans)