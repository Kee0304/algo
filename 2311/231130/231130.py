import math
import sys
input = sys.stdin.readline

N = int(input())

# dp[i][j] = i자리 계단수 중 j로 시작하는 계단수의 개수 
dp = [[0]*10 for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(0, 10):
        if i == 1:
            # 0으로 시작하는 수는 없다
            if j == 0:
                continue
            dp[i][j] = 1
        else:
            # j가 0이면 1에서 올 수 밖에 없다
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            # j가 9이면 8에서 올 수 밖에 없다
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            # i자리 계단수 중 j로 시작하는 계단수의 개수 = i-1자리 계단수 중 j-1로 시작하는 계단수의 개수 + i-1자리 계단수 중 j+1로 시작하는 계단수의 개수
            # 즉 앞에 숫자를 하나식 appendright한다고 생각하자
            else:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
        
print(sum(dp[-1])%1000000000)