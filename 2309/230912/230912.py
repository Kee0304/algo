import sys
inp = sys.stdin.readline

def minSegmentTree(node, start, end):
    if start == end:
        sTree[node] = leaf[start]
        return sTree[node]

    mid = (start+end)//2
    sTree[node] = min(minSegmentTree(node*2,start,mid), minSegmentTree(node*2+1, mid+1, end))

    return sTree[node]


def minSTree(node, start, end, left, right):
    if left > end or right < start:
        return 10**9
    
    if left <= start and end <= right:
        return sTree[node]

    mid = (start + end) // 2
    return min(minSTree(node*2, start, mid, left, right), minSTree(node*2+1, mid+1, end, left, right))
    


def update(node, start, end, index, data):
    if index < start or index > end:
        return
    if start == end:
        leaf[index] = data
        sTree[node] = data
        return sTree[node]

    mid = (start+end)//2
    update(node*2, start, mid, index, data)
    update(node*2+1, mid+1, end, index, data)
    sTree[node] = min(sTree[node*2],sTree[node*2+1])


    

N = int(inp().rstrip())
leaf = list(map(int,inp().split()))
sTree = [0]*(N*4)

minSegmentTree(1,0,N-1)

M = int(inp())

for _ in range(M):
    inpQuery = list(map(int,inp().split()))

    if inpQuery[0] == 2:
        i = inpQuery[1]-1
        j = inpQuery[2]-1
        print(minSTree(1, 0, N-1, i, j))
    
    elif inpQuery[0] == 1:
        i = inpQuery[1]-1
        value = inpQuery[2]
        update(1, 0, N-1, i, value)
