from copy import deepcopy
import sys
inp = sys.stdin.readline

# 집합 S의 크기
L = int(inp())
# 집합 S
sList = list(map(int,inp().split()))

# 좋은 수 출력 개수
n = int(inp())

area = []
minLuckyArea = []
if sList[0] > 1:
    area.append([1,sList[0]-1])
    minLuckyArea.append(sList[0]-2)
for i in range(len(sList)-1):
    if sList[i]+1 != sList[i+1]:
        area.append([sList[i]+1,sList[i+1]-1])
        minLuckyArea.append(sList[i+1]-sList[i]-2)
if sList[-1] < 1000000000:
    area.append([sList[-1]+1,1000000000])
    minLuckyArea.append(1000000000-sList[-1]-1)
curArea = deepcopy(area)

ansList = []

# minLuckyArea를 탐색하며 가장 작은 값을 가지는 인덱스에 대한 구간의 처음, 끝을 추가
# minLuckyArea갱신, 구간 갱신


curLuckyArea = 1000000000

# 다음 구간을 구하는 함수
def nextArea():
    global curLuckyArea
    minLuckyIndex = 0
    for i in range(len(minLuckyArea)):
        if curArea[i][0] <= curArea[i][1]:
            if minLuckyArea[i] < curLuckyArea:
                minLuckyIndex = i
                curLuckyArea = minLuckyArea[i]
    
    curLuckyArea = 1000000000
    return minLuckyIndex

# 반복회수가 n에 도달할 때 까지 반복
loopcnt = 0
ansList += sList
loopcnt += len(sList)

while loopcnt < n:
    # minLuckyArea 탐색
    minIndex = nextArea()
    if loopcnt +2 <= n:
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
    curArea[minIndex][1] -= 1
    minLuckyArea[minIndex] = minLuckyArea[minIndex] + curArea[minIndex][1]-curArea[minIndex][0]

print(" ".join((map(str,ansList))))