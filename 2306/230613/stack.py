# 가위바위보
def RSP(a, b):
    if a[0] == 1:
        if b[0] == 2:
            return b
        else:
            return a
    
    elif a[0] == 2:
        if b[0] == 3:
            return b
        else:
            return a
    
    else:
        if b[0] == 1:
            return b
        else:
            return a

# 그룹을 나눈다
def divideGroup(lst, group):
    if len(lst) >= 3:
        # 짝수면 큰 문제 없다
        # [1,2,3,4] 이면 len(lst)//2 = 2 로 lst[0,2] = [1,2]
        if len(lst)%2 == 0 :
            divideGroup(lst[:len(lst)//2], group)
            divideGroup(lst[len(lst)//2:], group)
        # 길이가 홀수면 번호와 인덱스로 나눈 것에 차이가 존재한다.
        # [1,2,3] 인 그룹이라면 len(lst)//2 = 1로 lst[0:1] = [1]이 되어버린다.
        # 하지만 (1+3)//2 = 2 로 2까지 들어가야 하므로 인덱스 범위에 1을 더해줄 필요가 있다.
        else:
            divideGroup(lst[:len(lst)//2+1], group)
            divideGroup(lst[len(lst)//2+1:], group)
        
    
    elif len(lst) == 2:
        group.append(RSP(lst[0], lst[1]))
        return
    
    elif len(lst) == 1:
        group.append(lst[0])
        return


T = int(input())

for t in range(1, T+1):
    N = int(input())
    inputlst = list(map(int,input().split()))
    group = []
    for index, value in enumerate(inputlst):
        group.append([value,index+1])

    # 승자가 한 명 나올 때까지 계속 그룹을 나누고 가위바위보를 시킨다.
    while len(group) >= 2:
        roopgroup = []
        divideGroup(group, roopgroup)
        group = roopgroup

    print(f'#{t} {group[0][1]}')
