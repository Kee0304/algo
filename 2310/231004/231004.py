from collections import deque
import sys
input = sys.stdin.readline

drow = [-1,0,1,0]
dcol = [0,1,0,-1]

T = int(input().rstrip())

for _ in range(T):
    M, N, K = map(int,input().split())
    mat = [[0]*M for _ in range(N)]
    visited = set()
    ans = 0
    for _ in range(K):
        col, row = map(int,input().split())
        mat[row][col] = 1
    
    for row in range(N):
        for col in range(M):
            if mat[row][col] == 1:
                if (row,col) not in visited:
                    ans+=1
                    visited.add((row,col))
                    dq = deque([(row, col)])
                    while dq:
                        cRow, cCol = dq.popleft()
                        for d in range(4):
                            nRow = cRow + drow[d]
                            nCol = cCol + dcol[d]
                            if 0<=nRow<N and 0<=nCol<M:
                                if mat[nRow][nCol] == 1 and (nRow,nCol) not in visited:
                                    dq.append((nRow,nCol))
                                    visited.add((nRow,nCol))
    
    print(ans)