import sys
input = sys.stdin.readline

def gradeFunc(num):
    return gradeDict[num]

N = int(input())
posList = list(map(int,input().split()))

sList = sorted(posList)

grade = 0
gradeDict = dict()
for i in range(N):
    gradeDict[sList[i]] = grade
    
    if i <= N-2:
        if sList[i] == sList[i+1]:
            pass
        else:
            grade+=1

ansList = list(map(gradeFunc, posList))

print(" ".join(map(str,ansList)))