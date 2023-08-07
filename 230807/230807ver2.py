import sys
from math import sqrt, floor, ceil
inp = sys.stdin.readline

minnum, maxnum = map(int,inp().split())
visited = set()
ans = maxnum - minnum +1

for k in range(2, floor(sqrt(maxnum))+1):
    # min보다 작거나 같은 수 중 k의 제곱으로 나누어 떨어지는 수 중 가장 큰 수를 k의 제곱으로 나눈 몫
    squreNum = k**2
    # 탐색 시작 수를 찾는다
    start = ceil(minnum/squreNum)*squreNum
    for num in range(start, maxnum+1, squreNum):
        if num in visited:
            continue
        visited.add(num)
        ans -= 1

print(ans)