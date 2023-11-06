import sys
input = sys.stdin.readline

N, M, R = map(int,input().split())
malList = list(map(int,input().split()))
flagList = list(map(int,input().split()))

ans = -1

# 삼각형의 넓이 = (밑변 * 높이) / 2
# 이 경우 밑변은 두 말뚝 사이의 거리
# 높이는 깃대의 길이

# 먼저 순서대로 정렬
flagList.sort()

# 가장 낮은 깃대의 길이
minMal = flagList[0]

# 먼저 최대 밑변 탐색
front = 0
end = len(malList)-1

while ((malList[end]-malList[front])*minMal)/2 > R:
    if (malList[front+1]-malList[front]) > (malList[end]-malList[end-1]):
        end -=1
    else:
        front+=1

    if front>=end:
        break

# 최대 밑변을 구했다.



# 밑변이 최대 넓이를 만들 수 있는 길이보다 길 때
if front >= end:
    print(ans)

# 아니면 높이를 순회하며 밑변을 줄이거나 높이를 줄이거나 하자
else:
    flagIndex = 0
    while 0<=flagIndex<=M-1:
        bottom = malList[end]-malList[front]
        height = flagList[flagIndex]
        width = height*bottom/2
        #print(f'현재 front = {malList[front]}, end = {malList[end]}, height = {flagList[flagIndex]}')
        #print(f'즉 넓이는 {width}')
        # 만약 넓이가 최대 넓이보다 같거나 낮으면
        if width <= R:
            # 넓이 갱신
            if ans < width:
                ans = width
            # 깃발 큰 거
            flagIndex +=1

        # 만약 넓이가 최대 넓이보다 크면
        else:
            heightChangeRatio = 50000
            # 깃대 줄이거나
            if flagIndex>=1:
                heightChangeRatio = (flagList[flagIndex]-flagList[flagIndex-1])/height
            # 밑변 왼쪽에서 줄이거나
            bottomChangeRatio1 = (malList[end]-malList[front+1])/bottom
            # 밑변 오른쪽에서 줄이거나
            bottomChangeRatio2 = (malList[end-1]-malList[front])/bottom

            toChange = min(heightChangeRatio, bottomChangeRatio1, bottomChangeRatio2)
            
            if toChange == heightChangeRatio:
                #print('깃대를 줄인다')
                flagIndex-=1
                break

            elif toChange == bottomChangeRatio1:
                #print('왼쪽에서 줄인다')
                front+=1
            else:
                #print('오른쪽에서 줄인다')
                end-=1
        
        if front >= end:
            break
    
    print(ans)