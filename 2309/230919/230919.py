import sys
input = sys.stdin.readline

ans = 0
sum = 0
hakSum = 0

def sumG(grade, hak):
    global sum
    global hakSum
    if grade != "P":
        if grade == "A+":
            sum += 4.5*hak
        elif grade == "A0":
            sum += 4.0*hak
        elif grade == "B+":
            sum += 3.5*hak
        elif grade == "B0":
            sum += 3.0*hak
        elif grade == "C+":
            sum += 2.5*hak
        elif grade == "C0":
            sum += 2.0*hak
        elif grade == "D+":
            sum += 1.5*hak
        elif grade == "D0":
            sum += 1.0*hak
        elif grade == "F":
            sum += 0
        hakSum += hak
    else:
        return

for _ in range(20):
    sub, hak, grade = input().split()
    sumG(grade, float(hak))

if hakSum == 0:
    print(0.0)
else:
    print(sum/hakSum)