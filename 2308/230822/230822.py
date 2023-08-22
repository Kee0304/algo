import sys
inp = sys.stdin.readline

tsdict = {
    '0':0, '1':1, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
    'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15,'G':16,'H':17,'I':18,'J':19,
    'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,
    'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35
           }
tsIndex = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# 36진법 -> 10진법
def toDec(numStr):
    strList = list(numStr)
    length = len(strList)
    sum = 0
    for index in range(length):
        sum += tsdict[strList[index]]*(36**(length - index -1))

    return sum

# 10진법 -> 36진법
def to36(decNum):
    strList = []
    maxSquare = 0
    while decNum >= 36**(maxSquare):
        maxSquare+=1
    maxSquare-=1

    while maxSquare >= 0:
        quo = decNum//(36**(maxSquare))
        decNum = decNum%(36**(maxSquare))
        strList.append(tsIndex[quo])
        maxSquare-=1
    
    ans = "".join(strList)
    if ans == "":
        ans = "0"
    return ans



tsList = []
wholesum = 0
# key가 되는 문자를 Z로 바꾸었을때 값의 차이
diffDict = dict()

N = int(inp())
for _ in range(N):
    inpStr = inp().rstrip()
    tsList.append(inpStr)
    length = len(inpStr)
    notZeroExist = False
    # 문자를 바꿨을 때 그 차이를 저장
    for index in range(length):
        if inpStr[index] != '0':
            notZeroExist = True
            if inpStr[index] in diffDict:
                diffDict[inpStr[index]] += (35-tsdict[inpStr[index]])*36**(length-index-1)
            else:
                diffDict[inpStr[index]] = (35-tsdict[inpStr[index]])*36**(length-index-1)
        else:
            if notZeroExist == True:
                if inpStr[index] in diffDict:
                    diffDict[inpStr[index]] += (35-tsdict[inpStr[index]])*36**(length-index-1)
                else:
                    diffDict[inpStr[index]] = (35-tsdict[inpStr[index]])*36**(length-index-1)

    # 36진법 문자열을 10진법으로 변환하여 더하기
    wholesum += toDec(inpStr)

K = int(inp())

sortedKey = sorted(diffDict.keys(), key= lambda x: -diffDict[x])
if len(sortedKey) >= K:
    for i in range(K):
        wholesum += diffDict[sortedKey[i]]
else:
    for i in range(len(sortedKey)):
        wholesum += diffDict[sortedKey[i]]

print(to36(wholesum))