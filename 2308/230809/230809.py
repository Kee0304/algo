from math import gcd
from fractions import Fraction
from collections import deque
import sys
inp = sys.stdin.readline

N = int(inp())

def lcm(x,y):
    return x*y//gcd(x,y)

# 관계 저장
relations = [[] for _ in range(N)]
for _ in range(N-1):
    a,b,p,q = map(int,inp().split())
    # 최대 공약수로 나누어서 저장
    g = gcd(p,q)
    p, q = p//g, q//g
    # 방향성이 없으므로 양쪽으로 저장
    relations[a].append((b,p,q))
    relations[b].append((a,q,p))

visited = [False]*N
dq = deque()
dq.append((0, 1))
visited[0] = True
relDict = dict()
relDict[0] = Fraction(1, 1)

while dq:
    cur = dq.popleft()
    curNode = cur[0]
    curValue = cur[1]
    relation = relations[cur[0]]
    for nextI in range(len(relation)):
        nextNode = relation[nextI][0]
        if visited[nextNode] == False:
            visited[nextNode] = True
            nextValue = curValue * Fraction(relation[nextI][2], relation[nextI][1])
            dq.append((nextNode, nextValue))
            relDict[nextNode] = nextValue

nums = []
for key, value in relDict.items():
    if type(value) == Fraction:
        nums.append(value.denominator)

numslcm = 1
while len(nums)>=2:
    a = nums.pop()
    b = nums.pop()
    numslcm = lcm(a,b)
    nums.append(numslcm)

anslst = [None]*N
for key, value in relDict.items():
    anslst[key] = value*numslcm

ans = ""
for an in anslst:
    ans += f'{int(an)} '

print(ans)