import sys
input = sys.stdin.readline

N = int(input())


dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1

for num in range(2,N+1):
    dp[num] = num
    sq = (num)**(1/2)
    if sq.is_integer():
        dp[num] = 1
    else:
        for sub_num in range(1, num):
            sub_double = sub_num**2
             
            if sub_double > num:
                break

            if dp[num] > dp[num-sub_double]+1:
                dp[num] = dp[num-sub_double]+1

print(dp)