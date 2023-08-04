# 저번 풀이는 원점에서 시작해서 소용돌이를 돌며 탐색했다
# 최악의 경우 소용돌이 맨 끝에 있는 점을 출력해야하면 1억 번을 전부 돌아야할 수도 있다.
# 아예 주어진 범위 내에서, 좌표에 따른 값을 수학적으로 계산하여 출력하도록 해보자
r1,c1,r2,c2 = map(int,input().split())

mat = []
maxNum = 0

for row in range(r1, r2+1,1):
    # 하나의 행
    rowList = []
    for col in range(c1, c2+1,1):
        # 소용돌이 진행방향이 횡방향
        if abs(row)>=abs(col):
            # 오른쪽으로 진행
            if row >= 0:
                # 왼쪽 시작점 abs(row) == abs(col)
                n = abs(row)
                # row == col일 때 시작점
                start = 4*((n)**2)+2*(n)+1
                rowList.append(start+n+col)
            
            # 왼쪽으로 진행
            elif row < 0:
                # row == col일 때 시작
                n = abs(row)
                start = 4*((n)**2)-2*(n)+1
                rowList.append(start+n-col)


        # 소용돌이 진행이 종방향
        if abs(row) < abs(col):
            # 아래로 진행
            if col < 0:
                n = abs(col)
                start = 4*((n)**2)+1
                rowList.append(start+n+row)
            
            elif col > 0:
                n = abs(col)
                start = ((2*(n-1)+1)**2)
                rowList.append(start+n-row)
    
    maxOfList = max(rowList)
    if maxNum < maxOfList:
        maxNum = maxOfList
    mat.append(rowList)

maxlen=len(str(maxNum))
ans = ""
for row in range(r2-r1+1):
    for col in range(c2-c1+1):
        ans += str(mat[row][col]).rjust(maxlen)
        ans += " "
    ans += '\n'

print(ans)