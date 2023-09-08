from collections import deque
import sys

inp = sys.stdin.readline

N, M = map(int,inp().split())

mat = []

for _ in range(N):
    mat.append(list(inp().rstrip()))

drow = [-1,0,1,0]
dcol = [0,1,0,-1]

dq = deque()
dq.append((0,0,0,0))
visited = set()
visited.add((0,0,0))
lenList = []

while dq:
    curRow, curCol, cnt, isBroken = dq.popleft()
    for d in range(4):
        nextRow = curRow + drow[d]
        nextCol = curCol + dcol[d]
        if 0<=nextRow<=N-1 and 0<=nextCol<=M-1:
            if nextRow == N-1 and nextCol == M-1:
                lenList.append(cnt+1)
                break
        
            else:
                if (nextRow,nextCol,isBroken) not in visited:
                    if mat[nextRow][nextCol] == "1":
                        if isBroken == 0:
                            dq.append((nextRow,nextCol,cnt+1,1))
                            visited.add((nextRow,nextCol,1))

                    else:
                        dq.append((nextRow,nextCol,cnt+1,isBroken))
                        visited.add((nextRow,nextCol,isBroken))


if N == 1 and M == 1:
    print(1)
else:
    if len(lenList) == 0:
        print(-1)
    else:
        print(min(lenList)+1)