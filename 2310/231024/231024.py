from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
adjDict = dict()
visited = set()
for _ in range(M):
    s, e = map(int,input().split())
    if s in adjDict:
        adjDict[s].append(e)
    else:
        adjDict[s] = [e]
    
    if e in adjDict:
        adjDict[e].append(s)
    else:
        adjDict[e] = [s]
ans = 0
for key in adjDict:
    if key not in visited:
        dq = deque([key])
        visited.add(key)
        while dq:
            cur = dq.popleft()
            for nextNode in adjDict[cur]:
                if nextNode not in visited:
                    dq.append(nextNode)
                    visited.add(nextNode)
        else:
            ans +=1

# 독립된 노드 처리
size = len(adjDict)
if N > size:
    ans += N-size

print(ans)