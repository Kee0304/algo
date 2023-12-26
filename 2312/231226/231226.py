import sys
input = sys.stdin.readline

N = int(input())
# dp[i][0]: i번째 줄에 사자가 없다
# dp[i][1]: i번째 줄에 왼쪽 우리에 사자가 있다
# dp[i][2]: i번째 줄에 오른쪽 우리에 사자가 있다.
dp = [[0,0,0] for _ in range(N+1)]

dp[1][0] = 1
dp[1][1] = 1 
dp[1][2] = 1

for i in range(2,N+1):
    # 이 줄에 사자가 없으면 그냥 그 전 줄에서 가능한 경우의 수를 그대로 가져오고
    dp[i][0] = sum(dp[i-1])
    # 사자가 있다면 전 줄과 사자 위치가 중복되면 안 된다.
    dp[i][1] = dp[i-1][0]+dp[i-1][2]
    dp[i][2] = dp[i-1][0]+dp[i-1][1]

print(sum(dp[-1])%9901)