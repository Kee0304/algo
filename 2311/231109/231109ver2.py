import sys
input = sys.stdin.readline

n = int(input())
intList = list(map(int,input().split()))
dp = [0]*n
dp[0] = intList[0]

for i in range(1,n):
    dp[i] = max(intList[i], dp[i-1]+intList[i])

print(max(dp))