from collections import deque
import sys
inp = sys.stdin.readline

V = int(inp().rstrip())

adjdict = dict()

for _ in range(V):
    inpList = list(map(int,inp().split()))
    pNode=inpList[0]
    adjdict[pNode] = []
    for i in range(1, len(inpList)-1, 2):
        adjdict[pNode].append((inpList[i],inpList[i+1]))


def bfs(node):
    ans = 0
    dq = deque()
    visited = set()
    dq.append((node,0))
    visited.add(node)

    while dq:
        curNode = dq.popleft()
        curChildNodes = adjdict[curNode[0]]
        for ci in range(len(curChildNodes)):
            if curChildNodes[ci][0] not in visited:
                dq.append((curChildNodes[ci][0],curNode[1]+curChildNodes[ci][1]))
                visited.add(curChildNodes[ci][0])
                if curNode[1]+curChildNodes[ci][1] > ans:
                    ans = curNode[1]+curChildNodes[ci][1]
                    farNode = curChildNodes[ci][0]

    return farNode, ans

first, rad = bfs(1)
final, rad = bfs(first)

print(rad)