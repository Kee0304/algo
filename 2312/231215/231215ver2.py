import sys
input = sys.stdin.readline

# 시간 초과
dp = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(51) ]
while 1:
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break

    if a>0 and b>0 and c>0:
        for i in range(a+1):
            for j in range(b+1):
                for k in range(c+1):
                    if i <= 0 or j <= 0 or k <= 0:
                        dp[i][j][k] = 1
                    elif i > 20 or j > 20 or k > 20:
                        if a > 20 and b> 20 and c > 20:
                            dp[i][j][k] = dp[20][20][20]
                        elif a > 20 and b > 20 and c <= 20:
                            dp[i][j][k] = dp[20][20][c]
                        elif a > 20 and b <= 20 and c > 20:
                            dp[i][j][k] = dp[20][b][20]
                        elif a <= 20 and b > 20 and c < 20:
                            dp[i][j][k] = dp[a][20][20]
                        elif a > 20 and b <= 20 and c <= 20:
                            dp[i][j][k] = dp[20][b][c]
                        elif a <= 20 and b > 20 and c <= 20:
                            dp[i][j][k] = dp[a][20][c]
                        elif a <= 20 and b <= 20 and c > 20:
                            dp[i][j][k] = dp[a][b][20]

                    elif i < j and j < k:
                        dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
                    else:
                        dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
        
        answer = dp[a][b][c]

    else:
        answer = 1

    print(f'w({a}, {b}, {c}) = {answer}')