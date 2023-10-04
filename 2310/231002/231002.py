import sys
input = sys.stdin.readline

K, N= map(int,input().split())

lineList = [0]*K

for i in range(K):
    lineList[i] = int(input())

minLen = min(lineList)

ans = 0

for divisor in range(minLen, 0, -1):
    sum = 0

    for i in range(K):
        sum += lineList[i]//divisor
    
    if sum >= N:
        ans = divisor
        break

print(ans)
