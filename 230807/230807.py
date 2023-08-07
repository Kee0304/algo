import sys
inp = sys.stdin.readline

minnum, maxnum = map(int,inp().split())
visited = set()
ans = maxnum - minnum +1

for k in range(2, int(maxnum**(1/2))+1):
    # min보다 작거나 같은 수 중 k의 제곱으로 나누어 떨어지는 수 중 가장 큰 수를 k의 제곱으로 나눈 몫
    loopNum = minnum//(k**2)
    while (k**2)*loopNum <= maxnum:
        if minnum<= (k**2)*loopNum <= maxnum and (k**2)*loopNum not in visited:
            visited.add((k**2)*loopNum)
            ans -=1
        loopNum +=1

print(ans)