import collections

T = int(input())

for t in range(1, T+1):
    inputlist = collections.deque(input())
    stack = []      # 괄호를 담을 스택
    cnt = 0         # 봉의 개수를 저장할 변수
    forgwal = None  # 앞의 괄호를 기억할 변수

    while len(inputlist) >=1:       # 입력된 리스트에서 하나씩 빼면서 진행
        gwal = inputlist.popleft()
        if gwal == "(":             # 여는 괄호면
            stack.append(gwal)      # 그냥 넣고
            forgwal = gwal          # 저장
        else:                       # 닫는 괄호면
            stack.pop()             # 스택에서 하나 빼고

            if forgwal == "(":      # 바로 앞이 여는 괄호, 즉 레이저면
                cnt += len(stack)   # 스택의 길이 만큼 더해줌
            else:                   # 바로 앞이 닫는 괄호면
                cnt +=1             # 봉이 하나 끝난 것으로 1을 더해줌
            
            forgwal = gwal          # 괄호 기억
    
    print(f'#{t} {cnt}')