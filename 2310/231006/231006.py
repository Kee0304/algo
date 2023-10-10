from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
mat = []

for _ in range(N):
    mat.append(list(map(int,list(input().rstrip()))))

visited = set()
dq = deque()
drow = [-1,0,1,0]
dcol = [0,1,0,-1]
sizeList = []

for row in range(N):
    for col in range(N):
        if mat[row][col] == 1:
            if (row,col) not in visited:
                size = 1
                dq.append((row,col))
                visited.add((row,col))
                while dq:
                    cRow, cCol = dq.popleft()
                    for d in range(4):
                        nRow = cRow + drow[d]
                        nCol = cCol + dcol[d]
                        if 0<=nRow<N and 0<=nCol<N:
                            if mat[nRow][nCol] == 1:
                                if (nRow, nCol) not in visited:
                                    dq.append((nRow,nCol))
                                    visited.add((nRow,nCol))
                                    size+=1
        

                sizeList.append(size)

sSizeList = list(map(str,sorted(sizeList)))
ans = f'{len(sSizeList)}\n'+"\n".join(sSizeList)
print(ans)