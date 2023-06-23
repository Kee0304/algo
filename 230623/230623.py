T = int(input())

for t in range(1, T+1):
    dailyPass, monthlyPass, tmonthlyPass, yearPass = map(int, input().split())
    plan = list(map(int,input().split()))

    # 먼저 day month 중 작은 쪽으로 전부 치환해주자
    for index in range(12):
        if plan[index]*dailyPass > monthlyPass:
            plan[index] = monthlyPass
        else:
            plan[index] = plan[index]*dailyPass

    # 누적 요금을 저장할 리스트
    acFee = [0] * 12

    # 1, 2월치 저장
    acFee[0] = plan[0]
    acFee[1] = plan[0]+plan[1]

    # 3월은 1,2,3월 월별 합과 3개월 패스를 비교해서 작은 쪽을 저장
    acFee[2] = min(plan[0]+plan[1]+plan[2], tmonthlyPass)

    # 4월부터 돌면서
    for monthIndex in range(3,12):
        acFee[monthIndex] = min(
            acFee[monthIndex-3] + tmonthlyPass,    # 세 달 전까지의 요금 + 3개월 패스의 값과
            acFee[monthIndex-1] + plan[monthIndex] # 한 달 전까지의 요금 + 한 달 요금 을 비교해서
            )                                      # 작은 놈이 누적 요금에 저장된다.
    
    # 그렇게 계산된 12월의 누적 값과 11월에 3개월 치를 내는 경우와 연간 패스를 비교해서 작은 놈이 값  
    result = min(acFee[11], acFee[9] + tmonthlyPass, yearPass)

    print(f'#{t} {result}')