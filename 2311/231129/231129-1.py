import sys
input = sys.stdin.readline

n = int(input())
mat = []

for _ in range(n):
    mat.append(list(map(int,input().split())))

dp = [[0]*i for i in range(1,n+1)]
dp[0][0] = mat[0][0]

for i in range(n):
    if i == 0:
        pass
    else:
        width = len(mat[i])
        for j in range(width):
            if j == 0:
                dp[i][j] = dp[i-1][j] + mat[i][j]
            elif 1<=j<=width-2:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + mat[i][j]
            else:
                dp[i][j] = dp[i-1][j-1] + mat[i][j]


print(max(dp[-1]))