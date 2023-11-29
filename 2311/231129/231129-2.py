import sys
input = sys.stdin.readline

n = int(input())
wine_list = []


for _ in range(n):
    wine_list.append(int(input()))

wines = len(wine_list)

dp = [0]*wines

for i in range(n):
    if i == 0:
        dp[i] = wine_list[i]
    elif i == 1:
        dp[i] = dp[i-1]+wine_list[i]
    elif i == 2:
        dp[i] = max(
            dp[i-1],
            dp[i-2]+wine_list[i],
            wine_list[i-1]+wine_list[i]
            )

    else:
        dp[i] = max(
            # i번째 잔을 마시지 않을 때
            dp[i-1],
            # i번째 잔을 마신다고 했을 때
            # i-2번째 잔을 마시지 않은 경우
            dp[i-3] + wine_list[i-1] + wine_list[i],
            # i-1번째 잔을 마시지 않은 경우
            dp[i-2] + wine_list[i]
        )

print(dp[-1])