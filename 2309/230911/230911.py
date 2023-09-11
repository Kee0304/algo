import sys
inp = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = leaf[start]
        return tree[node]
    
    mid = (start+end)//2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
            
    return tree[node]


def subSum(node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left<=start and end<=right:
        return tree[node]

    mid = (start + end) // 2
    return subSum(node*2, start, mid, left, right) + subSum(node*2+1, mid+1, end, left, right)

def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff
    
    mid = (start+end)//2

    if start != end:
        update(node*2, start, mid, index, diff)
        update(node*2+1, mid+1, end, index, diff)


N, M, K = map(int,inp().split())

leaf = []
tree = [0] * (N*4)

for _ in range(N):
    leaf.append(int(inp()))

init(1,0,N-1)

for _ in range(M+K):
    a, b, c = map(int,inp().split())

    if a == 1:
        b=b-1
        diff = c - leaf[b]
        leaf[b] = c
        update(1, 0, N-1, b, diff)
    
    elif a == 2:
        print(subSum(1, 0, N-1, b-1, c-1))
