import sys
input = sys.stdin.readline

N = int(input())

dp = [0]*(31)

# dp[6] = 3*dp[4] + 2*dp[2] + 2

# dp[8] = 3*dp[6] + 2*dp[4](특수한 4를 맨 앞에 배치하고 나머지 4칸 채우기) + 2*dp[2](특수한 6을 맨 앞에 배치하고 나머지 2칸 채우기) + 2
# 즉 dp[N] = 3*dp[N-2] + 2*dp[N-4] + 2*dp[N-6] + ... + 2

dp[2] = 3
dp[4] = 11
if N >= 5:
    for i in range(5,N+1):
        if i%2 == 0:
            for j in range(2,i-2,2):
                dp[i] += 2*dp[j]
            dp[i] += 3*dp[i-2] + 2

print(dp[N])