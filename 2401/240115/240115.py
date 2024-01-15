from collections import deque
import sys
input = sys.stdin.readline

computer = int(input())
N = int(input())
adj = dict()
visited = set()

for _ in range(N):
    start, end = map(int,input().split())
    
    if start in adj:
        adj[start].append(end)
    else:
        adj[start] = [end]
    
    if end in adj:
        adj[end].append(start)
    else:
        adj[end] = [start]

dq = deque([1])
visited.add(1)

while dq:
    cur = dq.popleft()
    
    if cur not in adj:
        break
    
    for next in adj[cur]:
        if next not in visited:
            dq.append(next)
            visited.add(next)

print(len(visited)-1)