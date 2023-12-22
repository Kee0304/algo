import sys
input = sys.stdin.readline

N,M = map(int,input().split())
mat = []
dp = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    mat.append(list(map(int,input().split())))

drow = [-1,0]
dcol = [0,-1]

for r in range(N):
    for c in range(M):
        if r == 0 and c == 0:
            dp[r][c] = mat[r][c]
            continue
        
        if r == 0:
            dp[r][c] = dp[r][c-1]+mat[r][c]
            continue

        if c == 0:
            dp[r][c] = dp[r-1][c]+mat[r][c]
            continue

        dp[r][c] = max(dp[r-1][c],dp[r][c-1]) + mat[r][c]

print(dp[-1][-1])