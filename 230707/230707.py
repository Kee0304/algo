T = int(input())

for t in range(1, T+1):
    N = int(input())
    atoms = []
    ans = 0
    for _ in range(N):
        atoms.append(tuple(map(int,input().split())))

    copylst = atoms[:]
    alreadyremoved = set()

    for atom in copylst:
        # 원자 충돌 거리
        minsec = 3000
        minatoms=[]
        if atom not in alreadyremoved:
            for other in copylst:
                if other not in alreadyremoved:
                    if other != atom:
                        # atom이 위로 이동하는 원자라면
                        if atom[2] == 0:
                            # other은 아래로 이동하면서 같은 x축에 있고 other이 atom 보다 위에 있을 때 
                            if other[2] == 1 and other[0] == atom[0] and atom[1] < other[1]:
                                # 반대편에서 서로 충돌할 때에는 시간이 반
                                dissec = (other[1] - atom[1])/2
                                if dissec < minsec:
                                    minatoms.clear()
                                    minatoms.append(other)
                                elif dissec == minsec:
                                    minatoms.append(other)
                            
                            # other은 왼쪽으로 이동하면서 atom과 교차한다
                            elif other[2] == 2 and atom[1] < other[1] and atom[0] < other[0] and abs(atom[0]-other[0]) == abs(atom[1]-other[1]):
                                dissec = abs(atom[0]-other[0])
                                if dissec < minsec:
                                    minatoms.clear()
                                    minatoms.append(other)
                                elif dissec == minsec:
                                    minatoms.append(other)

                            # other은 오른쪽으로 이동하면서 atom과 교차한다
                            elif other[2] == 3 and atom[1] < other[1] and atom[0] > other[0] and abs(atom[0]-other[0]) == abs(atom[1]-other[1]): 
                                dissec = abs(atom[0]-other[0])/2
                                if dissec < minsec:
                                    minatoms.clear()
                                    minatoms.append(other)
                                elif dissec == minsec:
                                    minatoms.append(other)

                        # atom이 아래로 이동하는 원자라면
                        elif atom[2] == 1:
                            # other은 위로 이동하면서 같은 x축에 있고 other이 atom보다 아래에 있을 때
                            if other[2] == 0 and other[0] == atom[0] and atom[1] > other[1]:
                                dissec = (atom[1] - other[1])/2
                                if dissec < minsec:
                                    minatoms.clear()
                                    minatoms.append(other)
                                elif dissec == minsec:
                                    minatoms.append(other)

                            # other은 왼쪽으로 이동하면서 atom과 교차한다
                            elif other[2] == 2 and atom[1] > other[1] and atom[0] < other[0] and abs(atom[0]-other[0]) == abs(atom[1]-other[1]):
                                dissec = abs(atom[0]-other[0])
                                if dissec < minsec:
                                    minatoms.clear()
                                    minatoms.append(other)
                                elif dissec == minsec:
                                    minatoms.append(other)

                            # other은 오른쪽으로 이동하면서 atom과 교차한다
                            elif other[2] == 3 and atom[1] > other[1] and atom[0] > other[0] and abs(atom[0]-other[0]) == abs(atom[1]-other[1]): 
                                dissec = abs(atom[0]-other[0])
                                if dissec < minsec:
                                    minatoms.clear()
                                    minatoms.append(other)
                                elif dissec == minsec:
                                    minatoms.append(other)
                        
                        # atom이 왼쪽으로 이동하는 원자라면
                        elif atom[2] == 2:
                            if other[2] == 3 and other[1] == atom[1] and atom[0] > other[0]:
                                dissec = (atom[0] - other[0])/2
                                if dissec < minsec:
                                    minatoms.clear()
                                    minatoms.append(other)
                                elif dissec == minsec:
                                    minatoms.append(other)
                            
                            elif other[2] == 0 and other[1] < atom[1] and other[0] < atom[0] and abs(atom[0]-other[0]) == abs(atom[1]-other[1]):
                                dissec = abs(atom[0] - other[0])
                                if dissec < minsec:
                                    minatoms.clear()
                                    minatoms.append(other)
                                elif dissec == minsec:
                                    minatoms.append(other)

                            elif other[2] == 1 and other[1] > atom[1] and other[0] < atom[0] and abs(atom[0]-other[0]) == abs(atom[1]-other[1]):
                                dissec = abs(atom[0] - other[0])
                                if dissec < minsec:
                                    minatoms.clear()
                                    minatoms.append(other)
                                elif dissec == minsec:
                                    minatoms.append(other)


                        # atom이 오른쪽으로 이동하는 원자라면
                        else:
                            if other[2] == 2 and other[1] == atom[1] and atom [0] < other[1]:
                                dissec = other[0] - atom[0]
                                if dissec < minsec:
                                    minatoms.clear()
                                    minatoms.append(other)
                                elif dissec == minsec:
                                    minatoms.append(other)

                            elif other[2] == 0 and other[1] < atom[1] and other[0] < atom[0] and abs(atom[0]-other[0]) == abs(atom[1]-other[1]):
                                dissec = abs(atom[0] - other[0])
                                if dissec < minsec:
                                    minatoms.clear()
                                    minatoms.append(other)
                                elif dissec == minsec:
                                    minatoms.append(other)

                            elif other[2] == 1 and other[1] > atom[1] and other[0] < atom[0] and abs(atom[0]-other[0]) == abs(atom[1]-other[1]):
                                dissec = abs(atom[0] - other[0])
                                if dissec < minsec:
                                    minatoms.clear()
                                    minatoms.append(other)
                                elif dissec == minsec:
                                    minatoms.append(other)        

            # 에너지 더하기
            if len(minatoms) >= 1:
                alreadyremoved.add(atom)
                ans += atom[3]
                for minatom in minatoms:
                    alreadyremoved.add(minatom)
                    ans += minatom[3]

    print(f'#{t} {ans}')