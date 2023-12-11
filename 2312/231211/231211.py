from collections import deque
import sys
input = sys.stdin.readline

row, col = map(int,input().split())
mat = []
dp = [[0]*col for _ in range(row)]
for _ in range(row):
    mat.append(list(map(int,input().split())))

visited = [[[0,0,0,0] for _ in range(col) ]for _ in range(row)]
dp[0][0] = 1
dq = deque([(0,0)])
drow = [-1,0,1,0]
dcol = [0,1,0,-1]
cnt = 0
while dq:
    for _ in range(len(dq)):
        cur = dq.popleft()
        cRow = cur[0]
        cCol = cur[1]
        for d in range(4):
            nRow = cRow+drow[d]
            nCol = cCol+dcol[d]
            if 0<=nRow<row and 0<=nCol<col:
                # 내리막일 때
                if mat[nRow][nCol] < mat[cRow][cCol]:
                    # 다른 방향에서 진입했을 때
                    if visited[nRow][nCol][d] == 0:
                        dp[nRow][nCol] += dp[cRow][cCol]
                        visited[nRow][nCol][d] = dp[cRow][cCol]
                        dq.append((nRow,nCol))
                    # 같은 방향에서 진입한 적이 있을 때
                    else:
                        if visited[nRow][nCol][d] < dp[cRow][cCol]:
                            dp[nRow][nCol] -= visited[nRow][nCol][d]
                            dp[nRow][nCol] += dp[cRow][cCol]
                            visited[nRow][nCol][d] = dp[cRow][cCol]
                            dq.append((nRow,nCol))

print(dp[-1][-1])