from collections import deque

drow = [-1,0,1,0]
dcol = [0,1,0,-1]

def tunnel(R,C,type):
    if type == 1:
        for d in range(4):
            plus(R,C,d)
    
    elif type == 2:
        for d in range(0,4,2):
            plus(R,C,d)
    
    elif type == 3:
        for d in range(1,4,2):
            plus(R,C,d)
    elif type == 4:
        for d in range(0,2):
            plus(R,C,d)

    elif type == 5:
        for d in range(1,3):
            plus(R,C,d)

    elif type == 6:
        for d in range(2,4):
            plus(R,C,d)
    
    elif type == 7:
        for d in range(0,4,3):
            plus(R,C,d)


def plus(R,C,d):
    if 0<=R+drow[d]<=N-1 and 0<=C+dcol[d]<=M-1:
        # 진행하는 방향의 터널이 연결되어있어야 한다.
        if d == 0:
            if mat[R+drow[d]][C+dcol[d]] == 1 or mat[R+drow[d]][C+dcol[d]] == 2 or mat[R+drow[d]][C+dcol[d]] == 5 or mat[R+drow[d]][C+dcol[d]] == 6:
                if (R+drow[d],C+dcol[d]) not in tun:
                    cur.append((R+drow[d],C+dcol[d]))
                tun.add((R+drow[d],C+dcol[d]))
        
        elif d == 1:
            if mat[R+drow[d]][C+dcol[d]] == 1 or mat[R+drow[d]][C+dcol[d]] == 3 or mat[R+drow[d]][C+dcol[d]] == 6 or mat[R+drow[d]][C+dcol[d]] == 7:
                if (R+drow[d],C+dcol[d]) not in tun:
                    cur.append((R+drow[d],C+dcol[d]))
                tun.add((R+drow[d],C+dcol[d]))            

        elif d == 2:
            if mat[R+drow[d]][C+dcol[d]] == 1 or mat[R+drow[d]][C+dcol[d]] == 2 or mat[R+drow[d]][C+dcol[d]] == 4 or mat[R+drow[d]][C+dcol[d]] == 7:
                if (R+drow[d],C+dcol[d]) not in tun:
                    cur.append((R+drow[d],C+dcol[d]))
                tun.add((R+drow[d],C+dcol[d]))         

        elif d == 3:
            if mat[R+drow[d]][C+dcol[d]] == 1 or mat[R+drow[d]][C+dcol[d]] == 3 or mat[R+drow[d]][C+dcol[d]] == 4 or mat[R+drow[d]][C+dcol[d]] == 5:
                if (R+drow[d],C+dcol[d]) not in tun:
                    cur.append((R+drow[d],C+dcol[d]))
                tun.add((R+drow[d],C+dcol[d]))      

T = int(input())

for t in range(1, T+1):
    N, M, R, C, L = map(int,input().split())
    mat = []
    for _ in range(N):
        mat.append(list(map(int,input().split())))
    
    tun = set()
    tun.add((R,C))
    cur = deque()
    cur.append((R,C))
    forlen = 0

    # 시작 지점은 이미 추가한 상태이므로 한 시간 지난 상태에서 시작
    for _ in range(1,L):
        for _ in range(len(cur)):
            curtun = cur.popleft()
            tunnel(curtun[0],curtun[1],mat[curtun[0]][curtun[1]])
        
        if len(tun) == forlen:
            break
        else:
            forlen = len(tun)
    
    print(f'#{t} {len(tun)}')
    
