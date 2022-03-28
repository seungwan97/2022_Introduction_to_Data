
"""
1.버거1종, 사이드1종, 음료1종 즉 항목별 1개이상 선택하면 세트로 반영되어 세트할인가 -1000원 적용
ex)버거2종+사이드1종+음료2종의 경우:1세트로 적용
2.각 제품의 재고 수량 반영
3.기존 세트 할인보다 더 저렴하게 판매하는 '할인세트'메뉴가 2종 있다.
빅맥세트4500원 & 상하이세트4500원
4.자료형과 코드의 구성은 자유아되 프로그램의 흐름은 본인이 제출한 다이어그램의 시퀀스 흐름도에 일치하도록 작성
5.라지세트는 700원 추가
"""
bur = ["빅맥버거세트", "상하이버거세트", "맥치킨버거", "빅맥버거", "더블빅맥버거", "트리플치즈버거", "맥스파이스버거", "1955버거", "더블불고기버거", "슈비버거", "슈슈버거", "베이컨토마토버거"]
bur_price = [4500, 4500, 3000, 3200, 3500, 3400, 3500, 3700, 3200, 3400, 3500, 3300]
bur_stock = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
sd = ["s맥너겟", "s해쉬브라운", "s스트링치즈", "s치즈스틱", "s후렌치후라이", "s스파이시맥너겟", "s치킨스낵랩", "s소시지스낵랩", "s치킨텐더", "s맥플러리", "d콜라", "d제로콜라", "d사이다",
      "d오렌지주스", "d밀크쉐이크", "d딸기쉐이크", "d초코쉐이크", "d환타", "d생수", "d우유"]
sd_price = [2000, 1200, 1400, 2000, 1500, 2100, 2000, 2200, 1900, 2500, 1500, 1500, 1500, 1500, 2000, 2000, 2000, 1500,
            1000, 1000]
sd_stock = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
order_list = [] #주문내역 #인덱스짝수값(0포함):품목/인덱스홀수값:수량
pay_list = [] #결제내역
saleset=bur[:2] #할인세일품목

while True:  # 폼1.포장유무 선택
    take0ut = input("매장식사 or 포장:")
    if take0ut:
        order_list.clear() #이후과정에서 초기화 했을때 주문내역을 비우기 위함
        pay_list.clear() #이후과정에서 초기화 했을때 결제내역을 비우기 위함
    print("*" * 100) #포장이던 식사던 같은 화면이 나와야 하므로
    while take0ut:  # 폼2.Menu
        print("메뉴판 출력")
        print("*" * 100)
        cate = input("세트 or 단품 or 사이드 or 음료:")
        if cate == "세트" or cate == "단품":
            if cate == "세트":
                print(bur[:2])
            elif cate == "단품":
                print(bur[2:])
            while cate:
                choi = input("선택:")
                number = input("수량:")
                print("남은수량:%d개" % int(bur_stock[bur.index(choi)] - int(number)))
                #버거리스트에서 선택한 버거명의 인덱스값을 추출하여 재고리스트의 인덱스 값으로 배정, 수량을 빼주었음
                #해당 재고리스트의 인덱스값인 전체수량에서 입력한 수량을 int한 상태에서 빼 남은수량 표시
                order_list.append(choi)#비어있던 주문리스트에서 선택품목 추가
                order_list.append(number)#비어있던 주문리스트에서 수량 추가
                pay_list.append((int(bur_price[bur.index(choi)] * int(number))))
                #위와 같은 방식으로 버거가격을 추출하여 수량을 곱한 값을 비어있던 결제리스트에 추가
                if int(bur_stock[bur.index(choi)]) - int(number) < 0: #만약 버거재고에서 설정한 수량을 뺀값이 0이하라면
                    print("재고가 없습니다.")
                    del order_list[-2:] #재고가 없으므로 주문내역에서 마지막항목만 삭제
                    del pay_list[-1] #재고가 없으므로 결제내역에서 마지막항목만 삭제
                    continue
                ask = input("더 구매하시겠습니까?(네,아니오로 응답):")
                while ask:
                    if ask == "네": #더 구매한다
                        break
                    elif ask == "아니오":
                        print("주문내역:", order_list)
                        print("합계:%d원" % int(sum(pay_list)))
                        finm = input("이전 or 완료:")
                        if finm == "이전":
                            print("*" * 100)
                            ask = False
                            cate = False
                            take0ut = False #맨처음화면이동
                        elif finm == "완료":
                            print("*" * 100)
                            size = input("라지변경 하시겠습니까?:")
                            while size: # 폼3.Size
                                x=0
                                while x==0:
                                    if size == "네":
                                        choi = input("어떤버거를 변경하시겠습니까?:")
                                        largenumber = input("수량:")
                                        if int(order_list[order_list.index(choi)+1]) - int(largenumber) < 0:
                                            print("기존 선택한 수량을 초과했습니다. 다시 입력해주십시오")
                                            continue
                                        order_list.append("(라지사이즈업)"+choi)
                                        order_list.append(largenumber)
                                        pay_list.append(700*int(largenumber))
                                        ask = input("다른 버거도 변경하시겠습니까?")
                                        while ask:
                                            if ask == "네":
                                                break
                                            elif ask == "아니오":
                                                ask=False
                                                x=x+1
                                    elif size =="아니오":
                                        x=x+1
                                while x==1:
                                    print("주문내역:", order_list)
                                    print("합계:%d원" % int(sum(pay_list)))
                                    fins = input("취소 or 이전 or 완료:")
                                    if fins == "취소":
                                        print("*" * 100)
                                        size = False
                                        ask = False
                                        cate = False
                                        take0ut = False
                                        break
                                    elif fins == "이전":
                                        print("*" * 100)
                                        size=False
                                        ask=False
                                        cate = False
                                        break
                                    elif fins == "완료":
                                        print("*" * 100)
                                        sd = ["맥너겟", "해쉬브라운", "스트링치즈", "치즈스틱", "후렌치후라이", "스파이시맥너겟", "치킨스낵랩", "소시지스낵랩","치킨텐더","맥플러리",
                                              "콜라", "제로콜라", "사이다", "오렌지주스", "밀크쉐이크", "딸기쉐이크", "초코쉐이크", "환타", "생수", "우유"]
                                        sd_price = [2000, 1200, 1400, 2000, 1500, 2100, 2000, 2200, 1900, 2500,
                                                    1500, 1500, 1500, 1500, 2000, 2000, 2000, 1500, 1000, 1000]

                                        y=0
                                        while y==0:
                                            cus = input("사이드추가 or 음료추가 or 선택안함/선택완료:")
                                            while cus:  # 폼4.customize
                                                if cus == "사이드추가":
                                                    print(sd[:10])
                                                    choi1 = input("선택:")
                                                    number = input("수량:")
                                                    order_list.append(choi1)
                                                    order_list.append(number)
                                                    pay_list.append(int(sd_price[sd.index(choi1)] * int(number)))
                                                    if int(sd_stock[sd.index(choi1)]) - int(number) < 0:
                                                        print("재고가 없습니다.")
                                                        del order_list[-2:]
                                                        del pay_list[-1]
                                                        continue
                                                    elif int(sd_stock[sd.index(choi1)]) - int(number) >= 0:
                                                        ask = input("다른 사이드를 추가하시겠습니까?")
                                                        while ask:
                                                            if ask == "네":
                                                                break
                                                            elif ask == "아니오":
                                                                ask = False
                                                                cus = False
                                                elif cus == "음료추가":
                                                    print(sd[10:])
                                                    choi2 = input("선택:")
                                                    number = input("수량:")
                                                    order_list.append(choi2)
                                                    order_list.append(number)
                                                    pay_list.append(int(sd_price[sd.index(choi2)] * int(number)))
                                                    print("남은수량:%d개" % int(sd_stock[sd.index(choi2)] - int(number)))
                                                    if int(sd_stock[sd.index(choi2)]) - int(number) < 0:
                                                        print("재고가 없습니다.")
                                                        del order_list[-2:]
                                                        del pay_list[-1]
                                                        continue
                                                    elif int(sd_stock[sd.index(choi2)]) - int(number) >= 0:
                                                        ask = input("다른 음료를 추가하시겠습니까?")
                                                        while ask:
                                                            if ask == "네":
                                                                break
                                                            elif ask == "아니오":
                                                                ask = False
                                                                cus = False
                                                else:
                                                    print("선택안함/선택완료")
                                                    print("주문내역:", order_list)
                                                    print("합계:%d원" % int(sum(pay_list)))
                                                    finc = input("완료하셨습니까?:")
                                                    if finc == "네":
                                                        matching1=[s for s in order_list if "버거" in s]
                                                        matching2 = [s for s in order_list if "s" in s]
                                                        matching3 = [s for s in order_list if "d" in s]
                                                        if (matching1 and matching2 and matching3) in (bur and sd):#?
                                                            if matching1 in bur[0:2]:#?
                                                                print("*" * 100)
                                                                print("최종주문확인")
                                                                print("최종주문내역:", order_list)
                                                                print("최종합계:%d원" % int(sum(pay_list)))
                                                            else:
                                                                print("*" * 100)
                                                                print("최종주문확인")
                                                                print("최종주문내역:", order_list)
                                                                print("세트할인가 적용","최종합계:%d원" % (int(sum(pay_list))-1000))
                                                        else :
                                                            print("*" * 100)
                                                            print("최종주문확인")
                                                            print("최종주문내역:", order_list)
                                                            print("최종합계:%d원" % int(sum(pay_list)))
                                                        last = input("이전 or 완료:")
                                                        while last: #폼5. Last Menu Check
                                                            if last == "이전":
                                                                last = False
                                                                cus = False
                                                            elif last=="완료":
                                                                print("*" * 100)
                                                                print("장바구니") # 폼6.장바구니
                                                                print(order_list)
                                                                break









        elif cate == "사이드" or cate == "음료":
            if cate == "사이드":
                print(sd[:10])
            elif cate == "음료":
                print(sd[10:])
                while cate:
                    choi = input("선택:")
                    number = input("수량:")
                    print("남은수량:%d개" % int(sd_stock[sd.index(choi)] - int(number)))
                    order_list.append(choi)  # 비어있던 주문리스트에서 선택품목 추가
                    order_list.append(number)  # 비어있던 주문리스트에서 수량 추가
                    pay_list.append((int(sd_price[sd.index(choi)] * int(number))))
                    if int(sd_stock[sd.index(choi)]) - int(number) < 0:  # 만약 버거재고에서 설정한 수량을 뺀값이 0이하라면
                        print("재고가 없습니다.")
                        del order_list[-2:]  # 재고가 없으므로 주문내역에서 마지막항목만 삭제
                        del pay_list[-1]  # 재고가 없으므로 결제내역에서 마지막항목만 삭제
                        continue
                    ask = input("더 구매하시겠습니까?(네,아니오로 응답):")
                    while ask:
                        if ask == "네":  # 더 구매한다
                            break
                        elif ask == "아니오":
                            print("주문내역:", order_list)
                            print("합계:%d원" % int(sum(pay_list)))
                            finm = input("이전 or 완료:")
                            if finm == "이전":
                                print("*" * 100)
                                ask = False
                                cate = False
                                take0ut = False
                            elif finm == "완료":
                                print("*" * 100)
                                print("최종주문확인") # 폼5. Last Menu Check
                                print("최종주문내역:", order_list)
                                last = input("이전 or 완료:")
                                while last:
                                    if last == "이전":
                                        last = False
                                        ask = False
                                        cate=False
                                    elif last == "완료":
                                        print("*" * 100)
                                        print("장바구니")  # 폼6.장바구니
                                        print(order_list)
                                        break