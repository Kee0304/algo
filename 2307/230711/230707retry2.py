T = int(input())

for t in range(1, T+1):
    N = int(input())
    atoms = []
    ans = 0
    for _ in range(N):
        atoms.append(tuple(map(int,input().split())))

    # 충돌 가능한 경우
    crushes = dict()

    # 기준 원자
    for aI in range(N-1):
        x, y, d, po = atoms[aI]
        # 다른 원자들

        for oI in range(aI+1, N):
            sx, sy, sd, spo = atoms[oI]
            # 같은 x축에 있고 
            if x == sx:
                # 기준원자가 위, 다른 원자가 아래로 움직이며 
                if d == 0 and sd == 1:
                    # 기준 원자가 아래에 있으면 충돌 가능
                    if sy > y:
                        sec = (sy - y)/2
                        if (x,(y+sy)/2,sec) not in crushes:
                            crushes[(x,(y+sy)/2,sec)] = {(x,y,d,po),(sx,sy,sd,spo)}
                        else:
                            crushes[(x,(y+sy)/2,sec)].add((x,y,d,po))
                            crushes[(x,(y+sy)/2,sec)].add((sx,sy,sd,spo))

                # 기준원자가 아래, 다른 원자가 위로 움직이며 
                elif d == 1 and sd == 0:
                    # 기준 원자가 위에 있으면 충돌 가능
                    if y > sy:
                        sec = (y - sy)/2
                        if (x,(y+sy)/2,sec) not in crushes:
                            crushes[(x,(y+sy)/2,sec)] = {(x,y,d,po),(sx,sy,sd,spo)}
                        else:
                            crushes[(x,(y+sy)/2,sec)].add((x,y,d,po))
                            crushes[(x,(y+sy)/2,sec)].add((sx,sy,sd,spo))
            
            # 같은 y축에 있고
            elif y == sy:
                # 기준원자가 좌, 다른 원자가 우로 움직이며
                if d == 2 and sd == 3:
                    # 기준 원자가 다른 원자보다 오른쪽에 있으면 충돌 가능
                    if x > sx:
                        sec = (x-sx)/2
                        if (x,(y+sy)/2,sec) not in crushes:
                            crushes[(x,(y+sy)/2,sec)] = {(x,y,d,po),(sx,sy,sd,spo)}
                        else:
                            crushes[(x,(y+sy)/2,sec)].add((x,y,d,po))
                            crushes[(x,(y+sy)/2,sec)].add((sx,sy,sd,spo))
                    
                # 기준원자가 우, 다른 원자가 좌로 움직이며
                elif d == 3 and sd == 2:
                    # 기준 원자가 다른 원자보다 왼쪽에 있으면 충돌 가능
                    if x < sx:
                        sec = (sx - x)/2
                        if (x,(y+sy)/2,sec) not in crushes:
                            crushes[(x,(y+sy)/2,sec)] = {(x,y,d,po),(sx,sy,sd,spo)}
                        else:
                            crushes[(x,(y+sy)/2,sec)].add((x,y,d,po))
                            crushes[(x,(y+sy)/2,sec)].add((sx,sy,sd,spo))


            # 두 원자가 대각선 상에 있고
            elif abs(x-sx) == abs(y-sy):
                # 기준 원자가 위로 움직일 때
                if d == 0:
                    # 다른 원자가 왼쪽으로 움직이면
                    if sd == 2:
                        if sx > x and sy > y:
                            sec = sx - x
                            if (x,(y+sy)/2,sec) not in crushes:
                                crushes[(x,(y+sy)/2,sec)] = {(x,y,d,po),(sx,sy,sd,spo)}
                            else:
                                crushes[(x,(y+sy)/2,sec)].add((x,y,d,po))
                                crushes[(x,(y+sy)/2,sec)].add((sx,sy,sd,spo))
                    # 다른 원자가 오른쪽으로 움직이면
                    elif sd == 3:
                        if x > sx and sy > y:
                            sec = x - sx
                            if (x,(y+sy)/2,sec) not in crushes:
                                crushes[(x,(y+sy)/2,sec)] = {(x,y,d,po),(sx,sy,sd,spo)}
                            else:
                                crushes[(x,(y+sy)/2,sec)].add((x,y,d,po))
                                crushes[(x,(y+sy)/2,sec)].add((sx,sy,sd,spo))
                # 기준 원자가 아래로 움직일 때
                elif d == 1:
                    # 다른 원자가 왼쪽으로 움직이면
                    if sd == 2:
                        if sx > x and sy < y:
                            sec = sx - x
                            if (x,(y+sy)/2,sec) not in crushes:
                                crushes[(x,(y+sy)/2,sec)] = {(x,y,d,po),(sx,sy,sd,spo)}
                            else:
                                crushes[(x,(y+sy)/2,sec)].add((x,y,d,po))
                                crushes[(x,(y+sy)/2,sec)].add((sx,sy,sd,spo))
                    # 다른 원자가 오른쪽으로 움직이면
                    elif sd == 3:
                        if x > sx and sy < y:
                            sec = x - sx
                            if (x,(y+sy)/2,sec) not in crushes:
                                crushes[(x,(y+sy)/2,sec)] = {(x,y,d,po),(sx,sy,sd,spo)}
                            else:
                                crushes[(x,(y+sy)/2,sec)].add((x,y,d,po))
                                crushes[(x,(y+sy)/2,sec)].add((sx,sy,sd,spo))


                # 기준 원자가 좌로 움직일 때
                elif d == 2:
                    # 다른 원자가 위로 움직이면
                    if sd == 0:
                        if x > sx and y > sy:
                            sec = x-sx
                            if (x,(y+sy)/2,sec) not in crushes:
                                crushes[(x,(y+sy)/2,sec)] = {(x,y,d,po),(sx,sy,sd,spo)}
                            else:
                                crushes[(x,(y+sy)/2,sec)].add((x,y,d,po))
                                crushes[(x,(y+sy)/2,sec)].add((sx,sy,sd,spo))
                    
                    # 다른 원자가 아래로 움직이면
                    elif sd == 1:
                        if x > sx and sy > y:
                            sec = x - sx
                            if (x,(y+sy)/2,sec) not in crushes:
                                crushes[(x,(y+sy)/2,sec)] = {(x,y,d,po),(sx,sy,sd,spo)}
                            else:
                                crushes[(x,(y+sy)/2,sec)].add((x,y,d,po))
                                crushes[(x,(y+sy)/2,sec)].add((sx,sy,sd,spo))
                
                
                # 기준 원자가 우로 움직일 때
                else:
                    # 다른 원자가 위로 움직이면
                    if sd == 0:
                        if x < sx and y > sy:
                            sec = sx-x
                            if (x,(y+sy)/2,sec) not in crushes:
                                crushes[(x,(y+sy)/2,sec)] = {(x,y,d,po),(sx,sy,sd,spo)}
                            else:
                                crushes[(x,(y+sy)/2,sec)].add((x,y,d,po))
                                crushes[(x,(y+sy)/2,sec)].add((sx,sy,sd,spo))
                    
                    # 다른 원자가 아래로 움직이면
                    elif sd == 1:
                        if x < sx and sy > y:
                            sec = sx - x
                            if (x,(y+sy)/2,sec) not in crushes:
                                crushes[(x,(y+sy)/2,sec)] = {(x,y,d,po),(sx,sy,sd,spo)}
                            else:
                                crushes[(x,(y+sy)/2,sec)].add((x,y,d,po))
                                crushes[(x,(y+sy)/2,sec)].add((sx,sy,sd,spo))               


    # 먼저 충돌하는 순으로 정렬
    sortedCrushes = sorted(crushes.items(), key = lambda x: x[0][2])
    print(sortedCrushes)
    # 충돌한 놈들을 저장할 셋
    removed = set()

    # 돌면서
    for key, crushatoms in sortedCrushes:
        # 현재 충돌할 원자들 중 충돌 가능한 개수
        cnt = 0
        # 원자 충돌 시 에너지
        energy = 0
        # 현재 충돌한 놈들
        temp = set()
        for atom in crushatoms:
            if atom not in removed:
                removed.add(atom)
                cnt +=1
                energy+=atom[3]
                temp.add(atom)

        
        # 2개 이상 충돌 가능하면 에너지를 더해준다
        if cnt >=2:
            ans += energy

        else:
            for atom in temp:
                removed.remove(atom)



    print(f'#{t} {ans}')