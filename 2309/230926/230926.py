import sys
input = sys.stdin.readline

N = int(input())

ans = N
for _ in range(N):
    strList = list(input().rstrip())
    alpSet = set()
    for i in range(len(strList)):
        if strList[i] not in alpSet:
            alpSet.add(strList[i])
        else:
            if strList[i-1] != strList[i]:
                ans -=1
                break

print(ans)