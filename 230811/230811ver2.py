from itertools import combinations
import sys
inp = sys.stdin.readline

N, K = inp().split()
numberTuple = tuple(N)
K = int(K)

possilbeList = []
possilbeList.append(numberTuple)
for _ in range(K):
    T = set()
    comb = list(combinations(range(len(numberTuple)), 2))
    for t in possilbeList:
        for a, b in comb:
            newList = list(t)
            newList[a], newList[b] = newList[b], newList[a]
            T.add(tuple(newList))
    
    possilbeList = sorted(list(T))

print(''.join(possilbeList[-1]))