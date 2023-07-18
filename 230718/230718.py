T = int(input())

for t in range(1,T+1):
    N, M = map(int,input().split())
    mat = []
    for _ in range(N):
        mat.append(list(map(int,input().split())))
    
    allhome = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                allhome +=1
    
    maxsales = allhome*M

    maxhomes = 0
    K = 1

    # 운영 비용이 최고 매출을 벗어나면 손해
    while ((K*K)+((K-1)*(K-1))) <= maxsales:
        for row in range(N):
            for col in range(N):
                homes = 0
                # 마름모 탐색
                # row 범위
                for r in range(-K+1, K):
                    # row에 따른col 길이
                    for c in range(-K+1 + abs(r), K- abs(r)):
                        if 0 <= row + r < N and 0<= col + c < N:
                            if mat[row+r][col+c] == 1:
                                homes +=1
                
                if (homes*M) >= ((K*K)+((K-1)*(K-1))):
                    if maxhomes < homes:
                        maxhomes = homes

        K += 1
    
    print(f'#{t} {maxhomes}')