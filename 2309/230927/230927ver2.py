import sys
input = sys.stdin.readline

N = int(input())
start = 0
if N%2 == 0:
    end = N//2
    start = end
else:
    end = N//2+1
    start = end-1
dp = [0] + [0]*(N//2) + [num-1 for num in range(end, 0,-1)]

for i in range(start,0,-1):
    if i*3 <= N and i*2 <= N:
        dp[i] = min(dp[i*3]+1, dp[i*2]+1, dp[i+1]+1)
    elif i*3 > N and i*2 <= N:
        dp[i] = min(dp[i*2]+1, dp[i+1]+1)
        
print(dp[1])