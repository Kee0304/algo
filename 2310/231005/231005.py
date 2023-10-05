import sys
input = sys.stdin.readline

N = int(input())
timeList = [None]*N

for i in range(N):
    start, end = map(int,input().split())
    timeList[i] = [start, end]

sList = sorted(timeList, key = lambda x: (x[1],x[0]))
ans = 1
start = sList[0][0]
end = sList[0][1]
for i in range(N):
    if i == 0:
        continue
    else:
        if sList[i][0] >= end:
            start = sList[i][0]
            end = sList[i][1]
            ans+=1

print(ans)