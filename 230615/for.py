T = int(input())

for t in range(1, T+1):
    N,Q = map(int,input().split())
    nlist = [0]*N
    for q in range(1,Q+1):
        L,R = map(int, input().split())
        for index in range(L-1, R):
            nlist[index]=q
    

    ans = " ".join(list(map(str, nlist)))
    print(f'#{t} {ans}')
