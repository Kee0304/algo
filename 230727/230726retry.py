import sys
inp = sys.stdin.readline

N = int(inp())
buildings = list(map(int,inp().split()))
ans = 0
# 빌딩을 다 순회해보자
for bIndex in range(N):
    # 해당 빌딩에서 보이는 빌딩 수
    cnt = 0
    # 앞의 빌딩을 순회하면서 기억할 기울기
    fGradient = 0
    # 뒤의 빌딩을 순회하면서 기억할 기울기
    bGradient = 0

    # 앞 빌딩 순회
    for fbIndex in range(bIndex-1,-1,-1):
        curGradient = (buildings[bIndex]-buildings[fbIndex])/(bIndex-fbIndex)
        if fbIndex == bIndex-1:
            fGradient = curGradient
            cnt +=1
        else:
            # 기울기가 저장된 기울기보다 작으면 기억하고 빌딩+1
            if fGradient > curGradient:
                cnt+=1
                fGradient = curGradient
            
    # 뒤 빌딩 순회
    for bbIndex in range(bIndex+1, N):
        curGradient = (buildings[bbIndex]-buildings[bIndex])/(bbIndex-bIndex)
        if bbIndex == bIndex+1:
            bGradient = curGradient
            cnt+=1
        else:
            # 기울기가 저장된 기울기보다 크면 기억하고 빌딩+1
            if bGradient < curGradient:
                cnt+=1
                bGradient = curGradient
    
    # 큰 값으로 갱신
    if cnt > ans:
        ans = cnt

print(ans)