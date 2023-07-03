import itertools

def honey(row, col,C):
    global ans

    for subRow in range(row, N):
        if subRow == row:
            if N-(col+M) >= M:
                worker1 = mat[subRow][col:col+M]
                comb1 = []
                for length in range(1, M+1):
                    comb1.extend(list(itertools.combinations(worker1,length)))
                worker1max = searchPart(comb1, C)

                for subCol in range(N-(col+M),N-M):
                    worker2 = mat[subRow][subCol:subCol+M]
                    comb2 = []
                    for length in range(1,M+1):
                        comb2.extend(list(itertools.combinations(worker2,length)))
                    worker2max = searchPart(comb2, C)

                    if worker1max + worker2max > ans:
                        ans = worker1max + worker2max
                
        else:
            worker1 = mat[subRow][col:col+M]
            comb1 = []
            for length in range(1, M+1):
                comb1.extend(list(itertools.combinations(worker1,length)))
            worker1max = searchPart(comb1, C)

            for subCol in range(N-M):
                worker2 = mat[subRow][subCol:subCol+M]
                comb2 = []
                for length in range(1,M+1):
                    comb2.extend(list(itertools.combinations(worker2,length)))
                worker2max = searchPart(comb2, C)


                print(comb1, comb2)
                if worker1max + worker2max > ans:
                    ans = worker1max + worker2max



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

    for row in range(N):
        for col in range(N-M+1):
            honey(row, col, C)

    print(f'#{t} {ans}')