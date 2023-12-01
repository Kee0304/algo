import sys
input = sys.stdin.readline

N = int(input())
card_price = [0] + list(map(int,input().split()))

# dp[i] = i개를 살 수 있는 최대 금액
dp = [0]*(N+1)

for i in range(1,N+1):
    if i == 1:
        dp[i] = card_price[1]
    else:
        val = -1
        for j in range(1,i):
            if dp[i-j]+dp[j] > val:
                val = dp[i-j]+dp[j]
        dp[i] = max(val,card_price[i])

print(dp[-1])