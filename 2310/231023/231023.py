import sys
input = sys.stdin.readline

N, M = map(int,input().split())
treeList = list(map(int,input().split()))
start = 1
end = max(treeList)
ans = 0
while start<=end:
    mid = (start+end)//2
    lenSum = 0

    for tree in treeList:
        if (tree-mid) > 0:
            lenSum+=tree-mid
    
    if lenSum >= M:
        start = mid+1
    elif lenSum < M:
        end = mid-1

else:
    ans = (start+end)//2

print(ans)
