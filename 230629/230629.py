# 2진수 -> 10진수
def BintoDec(binnum):
    decnum = 0
    for index in range(len(binnum)):
        decnum+=binnum[index]*(2)**(len(binnum)-index-1)
    
    return decnum

# 3진수 -> 10진수
def TertoDec(ternum):
    decnum = 0
    for index in range(len(ternum)):
        decnum+=ternum[index]*(3)**(len(ternum)-index-1)

    return decnum

# 비교하기
def BinTer(binnum, ternum):
    # 2진수를 순회하면서
    for binIndex in range(len(binnum)):
        copybin = binnum[:]

        # 값을 반대로 바꾸고
        if binnum[binIndex] == 0:
            copybin[binIndex] = 1
        else:
            copybin[binIndex] = 0

        # 3진수를 순회하면서 
        for terIndex in range(len(ternum)):
            copyter = ternum[:]

            # 해당 인덱스를 다른 값으로 교체해본다.
            for value in range(0,3):
                if ternum[terIndex] != value:
                    copyter[terIndex] = value

                    # 비교해서 같으면 성공
                    if BintoDec(copybin) == TertoDec(copyter):
                        return BintoDec(copybin)


T = int(input())

for t in range(1, T+1):
    binnum = list(map(int,list(input())))
    ternum = list(map(int,list(input())))
    res = BinTer(binnum, ternum)

    print(f'#{t} {res}')