# 저번 풀이는 k가 커지면 아무래도 N*N의 우려가 있다
# 로직은 맞아도 시간 초과가 남

import sys
inp = sys.stdin.readline

# 이번에는 N**N 내에 구하고자 하는 수보다 작은 수가 몇 개인지 구해보자
# 6**6 에서 10보다 작거나 같은 수
# 1 ~ 6 = 6 // 1
# 2*1 ~ 2*3 = 6 // 2
# 3*1 ~ 3*2 = 6 // 3
# 4*1 = 6 // 4
# 5*1 = 6 // 5
# 6*1 = 6 // 6
# 즉 구하고자 하는 값을 행으로 나눈 몫 만큼 두 수의 곱으로 이루어진 수가 존재

N = int(inp())
k = int(inp())
left, right = 1, k
ans = 0
while left <= right:
    mid = (left + right) // 2

    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N)

    # 이분 탐색
    # mid보다 작은 수들의 합이 k보다 크면 왼쪽 탐색, 작으면 오른쪽 탐색
    if temp >= k:
        ans = mid
        right = mid -1
    else:
        left = mid + 1

print(ans)

