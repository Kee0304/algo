def beat(binNum, N):
    for rIndex in range(-1, -1-N, -1):
        if binNum[rIndex] == "0":
            return "OFF"
    
    return "ON"

T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())

    # N이 2진수 표현보다 크면 N개의 비트가 다 켜지는 것은 불가능하다
    if N > len(bin(M)[2:]):
        print(f'#{t} OFF')
    # 아니면
    else:
        print(f'#{t} {beat(bin(M),N)}')