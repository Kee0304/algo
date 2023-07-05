from pprint import pprint

#def nQueen():



T = int(input())

for t in range(1, T+1):
    N = int(input())
    mat = []
    for _ in range(N):
        mat.append([0]*N)
    
    ans = 0
    #nQueen()

    print(f'#{t} {ans}')