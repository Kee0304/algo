from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int,input().split())
tomato = []

dq = deque()
visited = set()
total = N*M

for row in range(N):
    inputList = list(map(int,input().split()))
    tomato.append(inputList)
    for col in range(M):
        if inputList[col] == 1:
            dq.append((row,col))
            visited.add((row,col))
        elif inputList[col] == -1:
            total -= 1

drow = [-1,0,1,0]
dcol = [0,1,0,-1]

ans = 0

while dq:
    for _ in range(len(dq)):
        curTomato = dq.popleft()
        for d in range(4):
            nRow = curTomato[0]+drow[d]
            nCol = curTomato[1]+dcol[d]
            if 0<=nRow<N and 0<=nCol<M:
                if tomato[nRow][nCol] == 0 and (nRow,nCol) not in visited:
                    dq.append((nRow,nCol))
                    visited.add((nRow,nCol))
    
    if dq:
        ans += 1

if len(visited) != total:
    ans = -1

print(ans)