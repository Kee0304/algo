import sys
input = sys.stdin.readline

N = int(input())
input_list = list(map(int,input().split()))
dp = [0]*N
for i in range(N):
    max_num = 0
    for j in range(i):
        if input_list[i] > input_list[j] and dp[j] > max_num:
            max_num = dp[j]

    dp[i] = max_num+1

print(max(dp))