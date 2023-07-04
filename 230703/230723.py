import itertools

# 
def honey(row, col,C):
    global ans
    
    # 작업자 1의 꿀통
    worker1=mat[row][col:col+M]
    comb1 = []
    
    # 가능한 꿀통 조합을 만들고 가능한 큰 꿀 채취량 구하기
    for length in range(1, M+1):
        comb1.extend(list(itertools.combinations(worker1,length)))
        worker1max = searchPart(comb1, C)

    # 작업자 2의 꿀통 탐색
    for subRow in range(row, N):
        # 같은 줄에 있는 경우
        if subRow == row:
            # 범위 제한
            if N-(col+M) >= M:
                for subCol in range(N-(col+M),N-M+1):
                    worker2 = mat[subRow][subCol:subCol+M]
                    comb2 = []
                    for length in range(1,M+1):
                        comb2.extend(list(itertools.combinations(worker2,length)))
                    worker2max = searchPart(comb2, C)

                    if worker1max + worker2max > ans:
                        ans = worker1max + worker2max

        # 다른 줄에 있는 경우
        else:
            for subCol in range(N-M+1):
                worker2 = mat[subRow][subCol:subCol+M]
                comb2 = []
                for length in range(1,M+1):
                    comb2.extend(list(itertools.combinations(worker2,length)))
                worker2max = searchPart(comb2, C)


                if worker1max + worker2max > ans:
                    ans = worker1max + worker2max

# 조합 중에서 가능한 가장 큰 채취량을 가지는 경우의 수 찾기
def searchPart(comb,C):
    max = 0
    for part in comb:
        if sum(part)<=C:
            acc = 0
            for p in part:
                acc += p**2
            if max < acc:
                max = acc
    
    return max


T = int(input())

for t in range(1, T+1):
    N, M, C = map(int,input().split())
    mat = []

    for _ in range(N):
        mat.append(list(map(int,input().split())))

    ans = 0

    # 작업자 1의 꿀통 시작 위치
    for row in range(N):
        for col in range(N-M+1):
            # 가능한 경우의 수 탐색
            honey(row, col, C)

    print(f'#{t} {ans}')