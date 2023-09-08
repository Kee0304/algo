from collections import deque
import sys

inp = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int,inp().split())

mat = []

for _ in range(N):
    mat.append(list(inp().rstrip()))

drow = [-1,0,1,0]
dcol = [0,1,0,-1]

breakWall = False
visited = set()
dq = deque()
dq.append((0,0))
visited.add((0,0))
lenList = []

def bfs(isBroken, cnt):
    if len(dq) == 0:
        return

    curRow, curCol = dq.popleft()
    for d in range(4):
        nextRow = curRow + drow[d]
        nextCol = curCol + dcol[d]
        if 0<=nextRow<=N-1 and 0<=nextCol<=M-1:
            if nextRow == N-1 and nextCol == M-1:
                lenList.append(cnt+1)
                return
        
            else:
                if (nextRow,nextCol) not in visited:
                    if mat[nextRow][nextCol] == "1":
                        if isBroken == False:
                            mat[nextRow][nextCol] = "0"
                            dq.append((nextRow,nextCol))
                            visited.add((nextRow,nextCol))
                            bfs(True, cnt+1)
                            mat[nextRow][nextCol] = "1"

                    else:
                        dq.append((nextRow,nextCol))
                        visited.add((nextRow,nextCol))
                        bfs(isBroken, cnt+1)


bfs(False, 0)

if N == 1 and M == 1:
    print(1)
else:
    if len(lenList) == 0:
        print(-1)
    else:
        print(min(lenList)+1)