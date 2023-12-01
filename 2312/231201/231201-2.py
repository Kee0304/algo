import sys
input = sys.stdin.readline


n, k = map(int,input().split())
coins = [0]*(n)
for i in range(n):
    coins[i] = int(input())

coins.sort()

dp = [0]*(k+1)

min_coin = coins[0]
dp[0] = 1

# i를 만들 수 있는 동전의 경우의 수에 대해 동전 a를 더하면 이는 i+a를 만들 수 있는 경우의 수이다.  
# 즉 동전들에 대해
# dp[i] = dp[i] + dp[i-동전1]
# dp[i] = dp[i] + dp[i-동전2]
# ...
# 를 하자
for coin in coins:
    for i in range(coin,k+1):
        dp[i] += dp[i-coin]

print(dp[-1])