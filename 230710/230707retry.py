def movingAtom(atom):
    if atom[2] == 0:
        atom[1]+=1
    elif atom[2] == 1:
        atom[1]-=1
    elif atom[2] == 2:
        atom[0]-=1
    else:
        atom[0]+=1  

def crush():
    global ans
    idx = 0
    while idx <= len(atoms)-2:
        crushes=[]
        for other in atoms:
            if atoms[idx][0] == other[0] and atoms[idx][1] == other[1] and atoms[idx] != other:
                crushes.append(other)

        if len(crushes) >= 1:
            print(atoms)
            print(f'충돌하는 놈들 {crushes}')
            ans += atoms[idx][3]
            atoms.remove(atoms[idx])
            for other in crushes:
                ans += other[3]
                atoms.remove(other)
            print(f'남은 원자들{atoms}')

        else:
            idx +=1

T = int(input())

for t in range(1, T+1):
    N = int(input())
    atoms = []
    for _ in range(N):
        atoms.append(list(map(int,input().split())))

    ans = 0
    step = 0
    while step <= 2001:
        # 원자들 이동
        for atom in atoms:
            movingAtom(atom)

        # 충돌 판정
        crush()
        step +=1

    print(f'#{t} {ans}')


# 1. 시간초과
# 2. 반대편에서 오는 놈들 끼리 충돌할 경우, 반드시 정수 좌표에서 충돌하는 것이 아닌 0.5 좌표에서도 충돌 할 수 있다.