import sys
input = sys.stdin.readline

def disting(s):
    global curStatus
    global strNum
    if s == "+":
        if curStatus == "plus":
            plus.append(int(strNum))
            strNum = ""
        else:
            minus.append(int(strNum))
            strNum = ""

    elif s == "-":
        if curStatus == "plus":
            plus.append(int(strNum))
            curStatus = "minus"
            strNum = ""
        else:
            minus.append(int(strNum))
            strNum = ""

    elif s == "\n":
        if curStatus == "plus":
            plus.append(int(strNum))
            strNum = ""
        else:
            minus.append(int(strNum))
            strNum = ""

    else:
        strNum += s

inputStr = input()
plus = []
minus = []
curStatus = "plus"
strNum = ""
for i in range(len(inputStr)):
    s = inputStr[i]
    disting(s)

print(sum(plus)-sum(minus))