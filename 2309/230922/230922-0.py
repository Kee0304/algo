inputList = [3,2,1,5,2,6,3,2,2,4,9,8]

inLen = len(inputList)

enList = [0]*inLen
for i, el in enumerate(inputList):
    enList[i] = [i,el]

enList = sorted(enList, key= lambda x: x[1], reverse= True)

ansList = [0]*inLen
rank = 1
diff = 1
for i in range(len(enList)):
    oI, value = enList[i]
    if i == 0:
        ansList[enList[i][0]] = rank
    else:
        if enList[i][1] == enList[i-1][1]:
            ansList[enList[i][0]] = rank
            diff +=1
        else:
            rank+=diff
            diff=1
            ansList[enList[i][0]] = rank

print(ansList)
