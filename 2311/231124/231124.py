import sys
input = sys.stdin.readline

N = int(input())
cost = []

for _ in range(N):
    cost.append(list(map(int, input().split())))

dp = []
dp.append(cost[0])

for i in range(1,N):
    min0 = cost[i][0]+min(dp[i-1][1],dp[i-1][2])
    min1 = cost[i][1]+min(dp[i-1][0],dp[i-1][2])
    min2 = cost[i][2]+min(dp[i-1][0],dp[i-1][1])
    dp.append([min0,min1,min2])

print(min(dp[-1]))