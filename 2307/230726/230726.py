import sys
inp = sys.stdin.readline

N = int(inp())
buildings = list(map(int,inp().split()))

sIndex = 0
mIndex = 1
eIndex = 0
ans = 0
# 기울기
smgradient = buildings[1]-buildings[0]
megradient = 0

if len(buildings)<=1:
    pass
elif len(buildings) == 2:
    ans = 1
else:
    while eIndex < N-1:
        # 큰 빌딩에 가려 안 보이는 빌딩 수
        invisible = 0
        print(sIndex, mIndex, eIndex)
        # 기울기가 커지는 동안 중간 빌딩 갱신
        for bIndex in range(sIndex+2, N):
            if (buildings[bIndex]-buildings[sIndex])/(bIndex-sIndex) > smgradient:
                if (mIndex != bIndex):
                    mIndex = bIndex
                    smgradient = buildings[bIndex]-buildings[0]
            else:
                break

        # 만약 끝 점까지 도달해버렸으면 끝내고
        if mIndex == N-1:
            eIndex == N-1
            break

        # 아니면
        else:
            # 다시 기울기가 커지는 동안 끝 빌딩 갱신
            # 단 기울기가 작아진다고 바로 끝내지 않고 뒤에 것도 판별
            eIndex = mIndex+1
            megradient = buildings[mIndex+1]-buildings[mIndex]
            for bIndex in range(mIndex+2,N):
                print(f'기울기는 {(buildings[bIndex]-buildings[mIndex])/(bIndex-mIndex)}')
                if (buildings[bIndex]-buildings[mIndex])/(bIndex-mIndex) > megradient:
                    eIndex = bIndex
                    megradient = buildings[bIndex]-buildings[mIndex]
                else:
                    invisible +=1
                
        
        print(buildings[sIndex:eIndex+1])
        if eIndex - sIndex > ans:
            ans = eIndex-sIndex-invisible
        
        sIndex = mIndex
        mIndex = eIndex

print(ans)