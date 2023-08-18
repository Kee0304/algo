def fee(swimplan,month):           
    accfee = 0
    b = [('1일', '1일', '1일'), ('1일', '1일', '1달'),                  # 3달을 1일과 1달 플랜으로 나눈 중복조합
         ('1일', '1달', '1일'), ('1일', '1달', '1달'),
         ('1달', '1일', '1일'), ('1달', '1일', '1달'),
         ('1달', '1달', '1일'), ('1달', '1달', '1달')]
    c=[('1일','1일'),('1일','1달'),('1달','1일'),('1달','1달')]         # 2달을 1일과 1달 플랜으로 나눈 중복조합

    while month <= 10:                                                 # month가 10월 이하이면 
        pmf = feelist[2]                                               # 3개월간 최소 비용을 저장할 함수. 일단 3개월 비용을 저장

        for idx in range(len(b)):                                      # 중복조합에 대해 탐색
            pacf = 0                                                   # 해당 중복조합의 비용
            for j in range(3):
                if b[idx][j] == '1일':                                 # 한 달을 다 1일 비용으로 이용
                    if swimplan[month + j] != 0:                       # 이용 일수가 0이 아니면
                        pacf += swimplan[month + j] * feedict['1day']  # 일수*일 이용비
                elif b[idx][j] == '1달':                               # 한 달을 한 달 비용으로 이용
                    if swimplan[month + j] != 0:                       # 이용 일수가 0이 아니면
                        pacf += feedict['1month']                      # 한달 이용비

            if pmf > pacf:                                             # 중복조합에서 계산된 이용금액이 현재 저장된 금액보다 작으면
                pmf = pacf                                             # 교체

        accfee += pmf                                                  # 모든 중복조합에 대해 탐색한 후 교체

        month += 3                                                     # 3개월 이후로 이동

    if month > 12:                                                     # 1월부터 시작한 경우 month=13이 될 것

        if accfee <= feelist[3]:                                       # 그럼 그냥 1년 비용이랑 비교해서 낮은 쪽을 반환
            return accfee
        else:
            return feelist[3]

    elif month == 11:                                                  # 2월부터 시작해서 11월에 도달했으면
        pmf = feelist[2]                                               # 일단 3개월 비용을 저장
        for idx in range(len(c)):                                      # 2달에 대한 중복조합에 대해
            pacf=0                                         
            for j in range(2):                                         # 11월, 12월 두 개 밖에 없다.
                if c[idx][j] == '1일':
                    if swimplan[month + j] != 0:
                        pacf += swimplan[month + j] * feedict['1day']
                elif c[idx][j] == '1달':
                    if swimplan[month + j] != 0:
                        pacf += feedict['1month']

            if pmf > pacf:
                pmf = pacf

        accfee += pmf
        if accfee <= feelist[3]:
            return accfee
        else:
            return feelist[3]

    elif month == 12:                                                  # 3월부터 시작해서 12월에 도착했으면
        if swimplan[month] != 0:                                       # 이용일수가 0이 아닐 때
            accfee+=min(swimplan[month]*feedict['1day'],feedict['1month'],feedict['3month'])
                                                                       # 1달 이용일수*하루 이용 금액, 1달 이용 금액, 그리고 3달 이용 금액 중 최솟값을 더해준다.
        if accfee <= feelist[3]:
            return accfee
        else:
            return feelist[3]


T = int(input())

for t in range(1,T+1):
    feelist=list(map(int,input().split()))
    feedict={'1day':feelist[0],
        '1month':feelist[1],
        '3month':feelist[2],
        '1year':feelist[3]
        }

    swimplan=[0]+list(map(int,input().split()))
    c = [('1일', '1일'), ('1일', '1달'), ('1달', '1일'), ('1달', '1달')]

    jan=fee(swimplan,1)
    feb=fee(swimplan,2)
    if swimplan[1] != 0:                                                            # 2월부터 구한 거니까 1월 거 더해준다.
        feb+=min(swimplan[1]*feedict['1day'],feedict['1month'],feedict['3month'])

    mar=fee(swimplan,3)
    pmf=feedict['3month']
    for idx in range(len(c)):                                                       # 3월부터 구한 거니까 1,2월 거 더해준다.
        pacf=0
        for j in range(2):
            if c[idx][j] == '1일':
                if swimplan[1 + j] != 0:
                    pacf += swimplan[1 + j] * feedict['1day']
            elif c[idx][j] == '1달':
                if swimplan[1 + j] != 0:
                    pacf += feedict['1month']

        if pmf > pacf:
            pmf = pacf

    mar += pmf

    print(f'#{t} {min(jan,feb,mar,feelist[3])}')