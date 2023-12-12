import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = [0]*(n)
# dp[i] = i를 만들 수 있는 최소 동전의 개수
dp = [float("inf")]*(k+1)
for i in range(n):
    inputNum = int(input())
    if inputNum <= k:
        coins[i] = int(inputNum)
        dp[inputNum] = 1

dp[0] = 1

for i in range(1,k+1):
    backIndex = [dp[i]]
    for coin in coins:
        if i-coin >=0:
            backIndex.append(dp[i-coin])
    
    if backIndex:
        # dp[i] = i-coin들에 대해서 가장 작은 값+1 과 dp[i] 중에 작은 값
        dp[i] = min(min(backIndex)+1,dp[i])
        

ans = None
if dp[-1] == float("inf"):
    ans = -1
else:
    ans = dp[-1]
print(ans)