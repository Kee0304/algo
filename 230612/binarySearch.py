# 중위 순회를 하면서
def inorder(node):
    global nodeNum
    # 왼쪽 자식 노드가 존재하면 왼쪽 자식노드로 이동
    if 2*node <= N:
        inorder(2*node)
    
    # 현재 노드 번호를 저장하고 노드 번호를 1 늘려줌
    tree[node] = nodeNum
    nodeNum+=1

    # 오른쪽 자식 노드가 존재하면 오른쪽 자식 노드로 이동
    if 2*node +1 <= N:
        inorder(2*node+1)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    nodeNum = 1
    inorder(1)
    print(tree)
