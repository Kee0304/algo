from copy import deepcopy
from math import inf
import sys
inp = sys.stdin.readline

# 집합 S의 크기
L = int(inp().rstrip())
# 집합 S
sList = list(map(int,inp().split()))

# 좋은 수 출력 개수
n = int(inp())

area = []
minLuckyArea = []

if sList[0] > 2:
    area.append([1,sList[0]-1])
    minLuckyArea.append(sList[0]-1-1)
elif sList[0] == 2:
    area.append([1,1])
    minLuckyArea.append(1)

if len(sList) >= 2:
    for i in range(len(sList)):    
        # 딱 나 추가
        area.append([sList[i],sList[i]])
        minLuckyArea.append(1)

        # 내 뒷구간 추가
        if i != len(sList)-1:
            if sList[i+1] > sList[i]+1:
                area.append([sList[i]+1,sList[i+1]-1])
                if sList[i]+1 == sList[i+1]-1:
                    minLuckyArea.append(1)
                else:
                    minLuckyArea.append(sList[i+1]-1-sList[i]-1)

        else:
            area.append([sList[-1]+1,inf])
            minLuckyArea.append(inf)

else:
    area.append([sList[0],sList[0]])
    minLuckyArea.append(1)
    area.append([sList[0]+1,inf])
    minLuckyArea.append(inf)

curArea = deepcopy(area)

ansList = []

print(area)
print(minLuckyArea)

# minLuckyArea를 탐색하며 가장 작은 값을 가지는 인덱스에 대한 구간의 처음, 끝을 추가
# minLuckyArea갱신, 구간 갱신

curLuckyArea = inf

# 다음 구간을 구하는 함수
def nextArea():
    global curLuckyArea
    minLuckyIndex = 0
    for i in range(len(minLuckyArea)):
        if curArea[i][0] <= curArea[i][1]:
            if minLuckyArea[i] < curLuckyArea:
                minLuckyIndex = i
                curLuckyArea = minLuckyArea[i]
            else:
                if curLuckyArea == inf and minLuckyArea[i] == curLuckyArea:
                    minLuckyIndex = i

    curLuckyArea = inf
    return minLuckyIndex

# 반복회수가 n에 도달할 때 까지 반복
loopcnt = 0

while loopcnt < n:
    # minLuckyArea 탐색
    minIndex = nextArea()
    if loopcnt +2 <= n:
        # 무한인 오른쪽 끝 구간이면
        if minLuckyArea[minIndex] == inf:
            ansList.append(curArea[minIndex][0])
            loopcnt +=1
        else: 
            # 만약 구간의 길이가 1이면 하나만 더해줌
            if curArea[minIndex][0] == curArea[minIndex][1]:
                ansList.append(curArea[minIndex][0])
                loopcnt += 1
            else:
                ansList.append(curArea[minIndex][0])
                ansList.append(curArea[minIndex][1])    
                loopcnt +=2
    # 하나만 들어가면 끝이면 하나 넣고 끝
    else:
        ansList.append(curArea[minIndex][0])
        break
    
    # 갱신
    curArea[minIndex][0] += 1
    if curArea[minIndex][1] != inf:
        curArea[minIndex][1] -= 1
    # 구간에서 어떤 수를 포함하는 범위의 개수
    # = 자신을 포함 왼쪽에서 선택할 수 있는 수의 개수(시작) * 자신을 포함 오른쪽에서 선택할 수 있는 수의 개수(끝) - 1(자신을 두 번 선택)
    minLuckyArea[minIndex] = (curArea[minIndex][0] - area[minIndex][0]+1)*(area[minIndex][1] - curArea[minIndex][0]+1) -1

print(" ".join((map(str,ansList))))