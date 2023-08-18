r1,c1,r2,c2 = map(int,input().split())

# 2차월 배열 형태로 저장
mat = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]

# 채워야할 칸 수
total = (r2-r1+1)*(c2-c1+1)
# 시작 지점
row = 0
col = 0
# 좌표에 적힐 수
cnt = 1
# 직진 거리
length = 1

# 진행방향
drow = [-1,0,1,0]
dcol = [0,1,0,-1]
# 첫 진행방향은 오른쪽
d = 1

# 최대 수를 기억하자
maxNum = 1

# 2차원 배열을 모두 0이 아닌 수로 채울 때까지 반복
while total >0:
    # 소용돌이를 그릴 때 같은 길이만큼 두 번씩 직진하는 성질이 있다
    for _ in range(2):
        # 직진 거리 만큼 직진
        for _ in range(length):
            # 만약 좌표가 그려야하는 범위 내에 있다면
            if r1 <= row <= r2 and c1 <= col <= c2:
                # 좌표를 보정하고 값을 저장하고 0인 칸의 수 -1
                mat[row-r1][col-c1] = cnt
                maxNum = cnt
                total -= 1
            # 다음 좌표로 이동
            row += drow[d]
            col += dcol[d]
            # 값 +1
            cnt+=1
        
        # 방향 전환
        if d == 1:
            d = 0
        elif d == 0:
            d = 3
        elif d == 3:
            d = 2
        elif d == 2:
            d = 1
    
    # 두 번 직진 후 길이가 늘어남
    length += 1

maxNumlength = len(str(maxNum))

# 예쁘게 출력하기 위해서 공백을 맞춰주는 함수
def toStr(num):
    strNum = str(num)
    strNumlength = len(strNum)    
    if strNumlength < maxNumlength:
        strNum = " "*(maxNumlength-strNumlength) + strNum
    return strNum

# 문자열 출력
ans = ""
for i in range(r2-r1+1):
    ans += " ".join(list(map(toStr, mat[i])))
    ans += '\n'

print(ans)