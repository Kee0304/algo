T = int(input())

for t in range(1,T+1):
    N = int(input())
    busStop = [0]*5000
    for _ in range(N):
        A, B = map(int,input().split())
        for index in range(A-1,B):
            busStop[index]+=1
    
    anslst = []
    P = int(input())
    for _ in range(P):
        anslst.append(str(busStop[int(input())-1]))
    
    ans = " ".join(anslst)

    print(f'#{t} {ans}')