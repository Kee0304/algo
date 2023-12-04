import sys
input = sys.stdin.readline
print = sys.stdout.write

N,M = map(int,input().split())
mat = []
dp = [[0]*(N+1) for _ in range(N+1)]

for _ in range(N):
    mat.append(list(map(int,input().split())))

for row in range(1,N+1):
    for col in range(1,N+1):
        dp[row][col] = dp[row][col-1]+dp[row-1][col]-dp[row-1][col-1]+mat[row-1][col-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    print(f'{dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]}\n')