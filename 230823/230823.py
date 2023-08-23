import sys
inp = sys.stdin.readline

# 집합 S의 크기
L = int(inp())
# 집합 S
sList = list(map(int,inp().split()))

# 좋은 수 출력 개수
n = int(inp())

구간 = []
if sList[0] > 1:
    구간.append(f'1:{sList[0]-1}')
for i in range(len(sList)-1):
    if sList[i]+1 != sList[i+1]:
        구간.append(f'{sList[i]+1}:{sList[i+1]-1}')
if sList[-1] < 1000000000:
    구간.append(f'{sList[-1]+1}:1000000000')

def goodNum(num):
    secForNum = []
    for partS in sList:
        start, end = map(int,partS.split(":"))
        if start <= num <= end:
            secForNum.append(start)
            secForNum.append(end)


    return [num, (num-secForNum[0])*(secForNum[1]-num)]

print(구간)
            
