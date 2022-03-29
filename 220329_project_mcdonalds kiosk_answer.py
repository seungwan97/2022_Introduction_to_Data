

#kiosk 소스코드

#메뉴 데이터 선언
dict_set={"빅맥세트":4500,"상하이세트":4500}
dict_set_list=list(dict_set)
dict_b={"빅맥":[3000,10],"상하이":[3200,2],"불고기":[2800,10],"슈슈":[3300,10],"슈비":[3300,10]}
dict_b_list=list(dict_b)
dict_s={"감튀":[1500,10],"치즈스틱":[2000,10],"해쉬브라운":[1800,10],"스낵랩":[2500,10],"맥너겟":[2000,10]}
dict_s_list=list(dict_s)
dict_d={"콜라":[1500,10],"사이다":[1500,10],"생수":[1000,10],"우유":[1200,10],"제로콜라":[1400,10]}
dict_d_list=list(dict_d)
setlist=[]
#화면의 종류
# 1.포장or매장 / 2.메뉴카테고리 선택 / 3.메뉴 선택 3-1.세트 3-2.단품 3-3.사이드 3-4.음료 / 4.메뉴선택 4-1.반복 or 4-2.끝내기 / 5.장바구니 확인 / 6.결제
#사용자에게 선택지가 없는것은 while문이 하위로 파고들지만 아닌것은 동등한 while문에 놓아야 한다.
stringTemp=""
#바구니
basket={}
basket_set={}
extra=700

while True:#프로그램이 구동되는 동시에 while에 무조건 진입하여 무한 반복 루프로 들어간다.
    print("프로그램 시작")
    where=input("포장 or 매장:") #1.
    print("*"*100)
    while where:
        menu_ct=input("1.세트 2.단품 3.사이드 4.음료 5.장바구니") #2.
        print("*"*100)
        #3.
        if menu_ct=="세트":
            for i in dict_set_list: #리스트에 있는 요소들 중에서 처음부터 끝까지 출력해라(i를 통해서) #단 각 요소마다 줄이 바뀌어서 출력됨
                stringTemp=stringTemp+i
                stringTemp=stringTemp+" " #for문의 값을 줄이 바뀌는 것이 아닌 옆으로 쭉 출력하고 싶을때
                stringTemp=stringTemp+str(dict_set[i]) #가격까지 같이 출력하고 싶을때
                stringTemp=stringTemp + " "
            print(stringTemp) #들여쓰기 해제 한 이유:들여쓰기 하면 매 단계마다 출력되기 때문
            stringTemp="" #다른 메뉴를 골랐을 시 메뉴판을 초기화하기 위함
            menu_sel=input("메뉴를 선택하세요:")
            if menu_sel in dict_set_list and dict_b[menu_sel.split("세트")[0]][1]>0:
                print("주문이 가능합니다. %s개" % dict_b[menu_sel.split("세트")[0]][1])
            else:
                print("메뉴입력 오류 or 수량이 없습니다. 주문불가.")
                continue
            while True:
                print("사이드 선택 상황")
                for i in list(dict_s):  # 리스트에 있는 요소들 중에서 처음부터 끝까지 출력해라(i를 통해서) #단 각 요소마다 줄이 바뀌어서 출력됨
                    stringTemp = stringTemp + i
                    stringTemp = stringTemp + " "  # for문의 값을 줄이 바뀌는 것이 아닌 옆으로 쭉 출력하고 싶을때
                    stringTemp = stringTemp + str(dict_s[i][0])  # 가격까지 같이 출력하고 싶을때
                    stringTemp = stringTemp + " "
                print(stringTemp)  # 들여쓰기 해제 한 이유:들여쓰기 하면 매 단계마다 출력되기 때문
                stringTemp = ""  # 다른 메뉴를 골랐을 시 메뉴판을 초기화하기 위함
                side_sel=input("사이드를 선택하세요.:")
                if side_sel in list(dict_s) and dict_s[side_sel][1]>0:
                    print("선택한 사이드 가능합니다.")
                    break
                else:
                    print("메뉴가 틀렸거나 재고가 없거나 주문이 불가합니다.")
                    continue
            while True:
                print("음료 선택 상황")
                for i in list(dict_d):  # 리스트에 있는 요소들 중에서 처음부터 끝까지 출력해라(i를 통해서) #단 각 요소마다 줄이 바뀌어서 출력됨
                    stringTemp = stringTemp + i
                    stringTemp = stringTemp + " "  # for문의 값을 줄이 바뀌는 것이 아닌 옆으로 쭉 출력하고 싶을때
                    stringTemp = stringTemp + str(dict_d[i][0])  # 가격까지 같이 출력하고 싶을때
                    stringTemp = stringTemp + " "
                print(stringTemp)  # 들여쓰기 해제 한 이유:들여쓰기 하면 매 단계마다 출력되기 때문
                stringTemp = ""  # 다른 메뉴를 골랐을 시 메뉴판을 초기화하기 위함
                drink_sel=input("움료를 선택하세요.:")
                if drink_sel in list(dict_d) and dict_d[drink_sel][1]>0:
                    print("선택한 음료 가능합니다.")
                    break
                else:
                    print("메뉴가 틀렸거나 재고가 없거나 주문이 불가합니다.")
                    continue
            while True:
                set_size=input("라지or일반:")
                basket_set_temp=basket_set #기존에 저장된 장바구니를 temp라는 공간에 백업해놓기 위함 #원본내용이 계속 변경되면 이전 내역이 사라지므로 일종의 변수를 설정해서 임시로 저장해놓고 필요할때 불러오기 위함이다.
                if set_size == "라지":
                    print("라지 세트로 주문")
                    if basket_set_temp.get(menu_sel+"라지"):
                        basket_set[menu_sel+"라지"]=[basket_set_temp[menu_sel+"라지"][0]+dict_set[menu_sel]+extra,basket_set_temp[menu_sel+"라지"][1]+1]
                    else:
                        basket_set[menu_sel + "라지"] = [dict_set[menu_sel] + extra,1]

                    if basket_set_temp.get(side_sel):
                        basket_set[side_sel] = [0,basket_set_temp[side_sel][1]+1]
                    else:
                        basket_set[side_sel] =[0,1]
                    if basket_set_temp.get(drink_sel):
                        basket_set[drink_sel] = [0, basket_set_temp[drink_sel][1] + 1]
                    else:
                        basket_set[drink_sel] = [0, 1]
                    dict_b[menu_sel.split("세트")[0]][1]=(dict_b[menu_sel.split("세트")[0]][1]-1)
                    dict_s[side_sel][1]=dict_s[side_sel][1]-1
                    dict_d[drink_sel][1] = dict_d[drink_sel][1] - 1
                    setlist.append(menu_sel+"라지")
                    setlist.append(side_sel)
                    setlist.append(drink_sel)
                    print(basket_set_temp)
                    #print(dict_b[menu_sel.split("세트")[0]][1],dict_s[side_sel][1],dict_d[drink_sel][1])
                    break
                elif set_size == "일반":
                    print("일반 세트로 주문")
                    if basket_set_temp.get(menu_sel):
                        basket_set[menu_sel] = [basket_set_temp[menu_sel][0] + dict_set[menu_sel],basket_set_temp[menu_sel][1] + 1]
                    else:
                        basket_set[menu_sel] = [dict_set[menu_sel], 1]

                    if basket_set_temp.get(side_sel):
                        basket_set[side_sel] = [0, basket_set_temp[side_sel][1] + 1]
                    else:
                        basket_set[side_sel] = [0, 1]
                    if basket_set_temp.get(drink_sel):
                        basket_set[drink_sel] = [0, basket_set_temp[drink_sel][1] + 1]
                    else:
                        basket_set[drink_sel] = [0, 1]
                    dict_b[menu_sel.split("세트")[0]][1] = (dict_b[menu_sel.split("세트")[0]][1] - 1)
                    dict_s[side_sel][1] = dict_s[side_sel][1] - 1
                    dict_d[drink_sel][1] = dict_d[drink_sel][1] - 1
                    setlist.append(menu_sel)
                    setlist.append(side_sel)
                    setlist.append(drink_sel)
                    print(basket_set_temp)
                    #print(dict_b[menu_sel.split("세트")[0]][1], dict_s[side_sel][1], dict_d[drink_sel][1])
                    break
                else:
                    print("라지 or 일반 중 선택하세요. 다시 입력.")
                    continue

        elif menu_ct=="단품":
            #1.단품 메뉴 고르기
            #2.고른메뉴 재고확인
            #.장바구니 재고반영
            for i in dict_b_list:
                print(dict_b_list.index(i)+1,i,dict_b[i][0])
            bs=input("버거단품 메뉴를 입력하세요.:")
            for i in dict_b_list:
                if i == bs:
                    if dict_b[i][1]>0:
                        print("선택가능")
                        while True:
                            bcount=int(input("수량을 입력하세요:"))
                            if bcount>dict_b[i][1]:
                                print("재고 부족")
                                continue
                            else:
                                print("재고 있음")
                                if basket.get(i): #get함수는 없을때 오류가 아닌 none이 뜸 그래서 index가 아닌 get을 쓴다.
                                    basket[i]=dict_b[i][0]*(basket[i][1]+bcount),basket[i][1]+bcount
                                else:
                                    basket[i]=[dict_b[i][0]*bcount,bcount]
                                dict_b[i][1]=dict_b[i][1]-bcount
                                print(basket)
                                break
                    else:
                        print("선택불가, 재고없음.")

        elif menu_ct=="사이드":
            for i in dict_s_list:
                print(dict_s_list.index(i) + 1, i, dict_s[i][0])
            bs = input("사이드 메뉴를 입력하세요.:")
            for i in dict_s_list:
                if i == bs:
                    if dict_s[i][1] > 0:
                        print("선택가능")
                        while True:
                            bcount = int(input("수량을 입력하세요:"))
                            if bcount > dict_s[i][1]:
                                print("재고 부족")
                                continue
                            else:
                                print("재고 있음")
                                if basket.get(i):  # get함수는 없을때 오류가 아닌 none이 뜸 그래서 index가 아닌 get을 쓴다.
                                    basket[i] = dict_s[i][0] * (basket[i][1] + bcount), basket[i][1] + bcount
                                else:
                                    basket[i] = [dict_s[i][0] * bcount, bcount]
                                dict_s[i][1] = dict_s[i][1] - bcount
                                print(basket)
                                break
                    else:
                        print("선택불가, 재고없음.")

        elif menu_ct=="음료":
            for i in dict_d_list:
                print(dict_d_list.index(i) + 1, i, dict_d[i][0])
            bs = input("음료를 입력하세요.:")
            for i in dict_d_list:
                if i == bs:
                    if dict_d[i][1] > 0:
                        print("선택가능")
                        while True:
                            bcount = int(input("수량을 입력하세요:"))
                            if bcount > dict_d[i][1]:
                                print("재고 부족")
                                continue
                            else:
                                print("재고 있음")
                                if basket.get(i):  # get함수는 없을때 오류가 아닌 none이 뜸 그래서 index가 아닌 get을 쓴다.
                                    basket[i] = dict_d[i][0] * (basket[i][1] + bcount), basket[i][1] + bcount
                                else:
                                    basket[i] = [dict_d[i][0] * bcount, bcount]
                                dict_d[i][1] = dict_d[i][1] - bcount
                                print(basket)
                                break
                    else:
                        print("선택불가, 재고없음.")

        elif menu_ct=="장바구니":
            basket_set_list=list(basket_set)
            basket_list=list(basket)
            sum1=0
            sum2=0
            if len(basket_set_list)!=0:
                print(basket_set)
                for i in basket_set_list:
                    sum1+=basket_set[i][0]
            if len(basket_list)!=0:
                print(basket)
                for i in basket_list:
                    sum2+=basket[i][0]
            print(setList)
            b=0
            s=0
            d=0
            for i in list(basket):
                if dict_b.get(i):
                    b+=basket[i][1]
                elif dict_s.get(i):
                    s+=basket[i][1]
                elif dict_d.get(i):
                    d+=basket[i][1]
            set_num=min(b,s,d)
            print("총 %d세트임"%set_num)
            print(sum1+sum2-(set_num*1000))









