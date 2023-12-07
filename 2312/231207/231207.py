import sys
input = sys.stdin.readline

N, K = map(int,input().split())

dp = None
if K > N//2:
    dp = [0]*(N-K+1)
else:
    dp = [0]*(K+1)

dp[0] = 1

for i in range(1,len(dp)):
    if i == 1:
        dp[i] = N
    else:
        dp[i] = (dp[i-1]*(N+1-i))//(i)

print(dp[-1]%10007)