import os.path #path경로를 가져오기 위한 모듈
path="save.txt"
print(os.path.isfile(path)) #path변수에 저장되어 있는 파일이 존재하는지 여부

#1.파일의 생성 => 파일 존재 유무에 따라서 프로그램의 가장 처음
#2.파일의 저장 => 실제로 결제가 되고 나서 재고가 실제로 감소 했을 때에만 그 즉시 저장이 되어야함
#3.파일의 불러오기 =>프로그램의 가장 처음
#1,2,3번 전부 함수로 만들어야함


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
stock_remain={}
sell_infor={}

def show_menu_set(what):
    global stringTemp
    global dict_set_list
    global dict_s_list
    global dict_d_list
    for i in what:  # 리스트에 있는 요소들 중에서 처음부터 끝까지 출력해라(i를 통해서) #단 각 요소마다 줄이 바뀌어서 출력됨
        stringTemp = stringTemp + i
        stringTemp = stringTemp + " "  # for문의 값을 줄이 바뀌는 것이 아닌 옆으로 쭉 출력하고 싶을때
        if what==dict_set_list:
            stringTemp = stringTemp + str(dict_set[i])
        elif what==dict_s_list:
            stringTemp = stringTemp + str(dict_s[i][0])
        elif what==dict_d_list:
            stringTemp = stringTemp + str(dict_d[i][0])
        stringTemp = stringTemp + " "
    print(stringTemp)  # 들여쓰기 해제 한 이유:들여쓰기 하면 매 단계마다 출력되기 때문
    stringTemp = ""  # 다른 메뉴를 골랐을 시 메뉴판을 초기화하기 위함

def show_menu_single(whatdict):
    for i in list(whatdict):
        print(list(whatdict).index(i) + 1, i, whatdict[i][0])

def set_side_n_drink(what,whatdict):
    global side_sel
    global drink_sel
    while True:
        print("%s 선택 상황" % what)
        show_menu_set(list(whatdict))
        if what=="사이드":
            side_sel = input("%s를 선택하세요.:" % what)
            if side_sel in list(whatdict) and whatdict[side_sel][1] > 0:
                print("선택한 %s 가능합니다." % what)
                break
            else:
                print("메뉴가 틀렸거나 재고가 없거나 주문이 불가합니다.")
                continue
        elif what=="음료":
            drink_sel = input("%s를 선택하세요.:" % what)
            if drink_sel in list(whatdict) and whatdict[drink_sel][1] > 0:
                print("선택한 %s 가능합니다." % what)
                break
            else:
                print("메뉴가 틀렸거나 재고가 없거나 주문이 불가합니다.")
                continue

def size_choice(what):
    global basket_set_temp
    if what=="라지":
        if basket_set_temp.get(menu_sel + "라지"):
            basket_set[menu_sel + "라지"] = [basket_set_temp[menu_sel + "라지"][0] + dict_set[menu_sel] + extra,
                                           basket_set_temp[menu_sel + "라지"][1] + 1]
        else:
            basket_set[menu_sel + "라지"] = [dict_set[menu_sel] + extra, 1]
    elif what=="일반":
        if basket_set_temp.get(menu_sel):
            basket_set[menu_sel] = [basket_set_temp[menu_sel][0] + dict_set[menu_sel], basket_set_temp[menu_sel][1] + 1]
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
    if what=="라지":
        setlist.append(menu_sel + "라지")
    elif what=="일반":
        setlist.append(menu_sel)
    setlist.append(side_sel)
    setlist.append(drink_sel)
    print(basket_set_temp)

def menu_sel_single(whatdict):
    for i in list(whatdict):
        if i == bs:
            if whatdict[i][1] > 0:
                print("선택가능")
                def count_single(whatdict):
                    while True:
                        bcount = int(input("수량을 입력하세요:"))
                        global basket
                        if bcount > whatdict[i][1]:
                            print("재고 부족")
                            continue
                        else:
                            print("재고 있음")
                            if basket.get(i):  # get함수는 없을때 오류가 아닌 none이 뜸 그래서 index가 아닌 get을 쓴다.
                                basket[i] = whatdict[i][0] * (basket[i][1] + bcount), basket[i][1] + bcount
                            else:
                                basket[i] = [whatdict[i][0] * bcount, bcount]
                            whatdict[i][1] = whatdict[i][1] - bcount
                            print(basket)
                            break
                count_single(whatdict)
            else:
                print("선택불가, 재고없음.") #3
#def count_single 내장

def basket_finally():
    global basket
    basket_set_list = list(basket_set)
    basket_list = list(basket)
    sum1 = 0
    sum2 = 0
    if len(basket_set_list) != 0:
        print(basket_set)
        for i in basket_set_list:
            sum1 += basket_set[i][0]
    if len(basket_list) != 0:
        print(basket)
        for i in basket_list:
            sum2 += basket[i][0]
        for i in setlist:
            if i == "빅맥세트" or i == "빅맥세트라지" or i == "상하이세트" or i == "상하이세트라지":
                del setlist[setlist.index(i):setlist.index(i) + 3]
    print(setlist)
    b = 0
    s = 0
    d = 0
    for i in list(basket):
        if dict_b.get(i):
            b += basket[i][1]
        elif dict_s.get(i):
            s += basket[i][1]
        elif dict_d.get(i):
            d += basket[i][1]
    set_num = min(b, s, d)
    print("총 %d세트임" % set_num)
    print(sum1 + sum2 - (set_num * 1000))

def stock(whatdict):
    for i in whatdict.keys():
        stock_remain[i]=whatdict[i][1]
    print(stock_remain)
    stock_remain.clear()

def sel_information():
    print("판매목록 정보")
    for i in basket.keys():
        sell_infor[i]=basket[i][1]
    print(sell_infor)

def sel_count(): #판매횟수 출력함수 #미완성
    x=0
    while x==0:
        x+=1
    print("판매횟수:",x)
def cancel(): #취소횟수 출력함수 #미완성
    x = 0
    while x==0:
        x += 1
    print("취소횟수:",x)

def fin_sel():#누적판매총액 출력함수 #미완성
    pass

while True:#프로그램이 구동되는 동시에 while에 무조건 진입하여 무한 반복 루프로 들어간다.
    print("프로그램 시작")
    where=input("포장 or 매장:") #1.
    print("*"*100)
    while where:
        menu_ct = input("1.세트 2.단품 3.사이드 4.음료 5.장바구니")  # 2.
        print("*" * 100)  # 3.
        if menu_ct == "세트":
            show_menu_set(dict_set_list)
            menu_sel = input("메뉴를 선택하세요:")
            if menu_sel in dict_set_list and dict_b[menu_sel.split("세트")[0]][1] > 0:
                print("주문이 가능합니다. %s개" % dict_b[menu_sel.split("세트")[0]][1])
            else:
                print("메뉴입력 오류 or 수량이 없습니다. 주문불가.")
                continue
            set_side_n_drink("사이드",dict_s)
            set_side_n_drink("음료", dict_d)
            while True:
                set_size = input("라지or일반:")
                basket_set_temp = basket_set  # 기존에 저장된 장바구니를 temp라는 공간에 백업해놓기 위함 #원본내용이 계속 변경되면 이전 내역이 사라지므로 일종의 변수를 설정해서 임시로 저장해놓고 필요할때 불러오기 위함이다.
                if set_size == "라지":
                    print("라지 세트로 주문")
                    size_choice("라지")
                    break
                elif set_size == "일반":
                    print("일반 세트로 주문")
                    size_choice("일반")
                    break
                else:
                    print("라지 or 일반 중 선택하세요. 다시 입력.")
                    continue

        elif menu_ct == "단품":
            show_menu_single(dict_b)
            bs = input("버거단품 메뉴를 입력하세요.:")
            menu_sel_single(dict_b)

        elif menu_ct == "사이드":
            show_menu_single(dict_s)
            bs = input("사이드 메뉴를 입력하세요.:")
            menu_sel_single(dict_s)

        elif menu_ct == "음료":
            show_menu_single(dict_d)
            bs = input("음료를 입력하세요.:")
            menu_sel_single(dict_d)

        elif menu_ct == "장바구니":
            basket_finally()
            print("*" * 100)
            pay=input("결제하기(네/아니오)")
            while pay:
                if pay=="네":
                    print("결제완료")
                    print("*" * 100)
                    print("남은 재고수량")
                    stock(dict_b)
                    stock(dict_s)
                    stock(dict_d)
                    print("*" * 100)
                    sel_information()
                    sel_count()
                else:
                    cancel()
                    break





















"""
        elif menu_ct == "장바구니":
            last = input("진행 or 부분삭제 or 비우기")
            while last:
                basket_set_list = list(basket_set)
                basket_list = list(basket)
                print(basket_set)
                print(basket)
                x = 0
                while x == 0:
                    if last == "비우기":
                        basket.clear()
                        basket_set.clear()
                        print(basket_set)
                        print(basket)
                        print("장바구니가 비워졌습니다.")
                        last = False
                        break
                    elif last == "부분삭제":
                        delete = input("삭제할 품목:")
                        if delete in setlist:
                            del setlist[(setlist.index(delete)):(setlist.index(delete) + 3)]
                            x += 1
                            break
                        elif delete in basket:
                            del basket[delete]
                            x += 1
                            break
                    else:
                        x += 1
                        break
                while x == 1:
                    sum1 = 0
                    sum2 = 0
                    if len(basket_set_list) != 0:
                        print(basket_set)
                        for i in basket_set_list:
                            sum1 += basket_set[i][0]
                    if len(basket_list) != 0:
                        print(basket)
                        for i in basket_list:
                            sum2 += basket[i][0]
                    b = 0
                    s = 0
                    d = 0
                    for i in list(basket):
                        if dict_b.get(i):
                            b += basket[i][1]
                        elif dict_s.get(i):
                            s += basket[i][1]
                        elif dict_d.get(i):
                            d += basket[i][1]
                    set_num = min(b, s, d)
                    print("총 %d세트" % set_num)
                    print(sum1 + sum2 - (set_num * 1000))
                    break
"""






