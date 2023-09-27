import sys
input = sys.stdin.readline

N = int(input())

if N >= 3:
    dp = [0,0,1,1]+[0]*(N-3)
    for i in range(3, N+1):
        if i % 6 == 0:
            dp[i] = min(dp[i//3],dp[i//2])+1
        elif i % 3 == 0:
            dp[i] = min(dp[i//3], dp[i-1])+1
        elif i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1])+1
        else:
            dp[i] = dp[i-1]+1
    print(dp[N])
elif N == 2:
    print(1)
elif N == 1:
    print(0)