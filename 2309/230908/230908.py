import sys
inp = sys.stdin.readline

N, M, K = map(int,inp().split())
numList = [0]*N
pSum = [0]*N
for i in range(N):
    intinp = int(inp())
    if i == 0:
        pSum[i] = intinp
    else:
        pSum[i] = intinp + pSum[i-1]
    numList[i] = intinp



for _ in range(K):
    for _ in range(M):
        a, b, c = map(int,inp().split())
        if a == 1:
            origin = numList[b-1]
            for i in range(b-1,N):
                pSum[i]+=c-origin

        else:
            print(pSum[c-1]-pSum[b-2])