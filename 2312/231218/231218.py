import sys
input = sys.stdin.readline

# 시작점에 대해서 뒷 번호의 도착점이 항상 커야 한다.
# 증가하는 가장 긴 부분 수열을 찾고 전체 길이에서 빼주자
# 즉 실제 어떤 줄들을 잘라야 하는지는 우리 관심사가 아니다.


def findIndex(targetNum):
    start = 0
    end = len(part)-1
    while start<end:
        mid = (start+end)//2
        if targetNum < part[mid]:
            end = mid
        elif targetNum > part[mid]:
            start = mid+1
        else:
            start = mid
            end = mid
        
    return start
    

N = int(input())

lines = []
for _ in range(N):
    lines.append(list(map(int,input().split())))

lines.sort(key= lambda x: x[0])

part = [lines[0][1]]
for i in range(N):
    goal = lines[i][1]
    if goal > part[-1]:
        part.append(goal)
    else:
        part[findIndex(goal)] = goal

print(N-len(part))
