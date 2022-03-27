
"""
1.버거1종, 사이드1종, 음료1종 즉 항목별 1개이상 선택하면 세트로 반영되어 세트할인가 -1000원 적용
ex)버거2종+사이드1종+음료2종의 경우:1세트로 적용
2.각 제품의 재고 수량 반영
3.기존 세트 할인보다 더 저렴하게 판매하는 '할인세트'메뉴가 2종 있다.
빅맥세트4500원 & 상하이세트4500원
4.자료형과 코드의 구성은 자유아되 프로그램의 흐름은 본인이 제출한 다이어그램의 시퀀스 흐름도에 일치하도록 작성
5.라지세트는 700원 추가
"""
bur = ["빅맥세트", "상하이세트", "맥치킨", "빅맥", "더블빅맥", "트리플치즈", "맥스파이스", "1955", "더블불고기", "슈비", "슈슈", "베이컨토마토"]
bur_price = [4500, 4500, 3000, 3200, 3500, 3400, 3500, 3700, 3200, 3400, 3500, 3300]
bur_large=["빅맥세트L", "상하이세트L", "맥치킨L", "빅맥L", "더블빅맥L", "트리플치즈L", "맥스파이스L", "1955L", "더블불고기L", "슈비L", "슈슈L", "베이컨토마토L"]
bur_large_price=[5200, 5200, 3700, 3900, 4200, 4100, 4200, 4400, 3900, 4100, 4200, 4000]
bur_stock = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
sd = ["맥너겟", "해쉬브라운", "스트링치즈", "치즈스틱", "후렌치후라이", "스파이시맥너겟", "치킨스낵랩", "소시지스낵랩", "치킨텐더", "맥플러리", "콜라", "제로콜라", "사이다",
      "오렌지주스", "밀크쉐이크", "딸기쉐이크", "초코쉐이크", "환타", "생수", "우유"]
sd_price = [2000, 1200, 1400, 2000, 1500, 2100, 2000, 2200, 1900, 2500, 1500, 1500, 1500, 1500, 2000, 2000, 2000, 1500,
            1000, 1000]
sd_stock = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
more = "더 구매하시겠습니까?(네,아니오로 응답)"
more2 = "다른 상품을 구매하시겠습니까?(네,아니오로 응답)"
order_list = []
pay_list = []
change_list=[]
saleset=bur[:1]

# 상위에서 후세대에 설정한 input변수를 쓰고자 할때는 while True를 쓰고 쓰면 된다.
# 결제
while True:  # 폼1.포장유무 선택
    take0ut = input("매장식사 or 포장:")
    if take0ut:
        order_list.clear()
        pay_list.clear()
    print("*" * 100)
    while take0ut: # 폼2.Menu
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
                print("남은수량:%d개" % int(bur_stock[bur.index(choi)] - int(number))) #사이즈 이후 돌아와서 추가로 메뉴를 주문했을때 재고수량 초기화(10)되는 문제 발생
                order_list.append(choi + number)
                pay_list.append((int(bur_price[bur.index(choi)] * int(number))))
                if int(bur_stock[bur.index(choi)]) - int(number) <= 0:
                    print("재고가 없습니다.")
                    order_list.clear()
                    pay_list.clear()
                    continue
                ask = input(more)
                while True:
                    if ask == "네":
                        if int(bur_stock[bur.index(choi)]) - int(number) > 0:
                            m = 1
                            break
                        else:
                            print("재고가 없습니다.")
                            ask2 = input(more2)
                            if ask2 == "네":
                                m = 1
                                break
                            elif ask2 == "아니오":
                                m = 0
                                break
                    elif ask == "아니오":
                        m = 0
                        break
                while m==0:
                    print("주문내역:", order_list)
                    print("합계:%d원" % int(sum(pay_list)))
                    finm = input("이전 or 완료:")
                    if finm == "이전":
                        print("*" * 100)
                        n = 1
                        m=1
                        cate=False
                        take0ut=False
                    elif finm == "완료":
                        n=0
                        break
                while m==0 and n==0:
                    print("*" * 100)  # 폼3.Size
                    size = input("라지변경?:")
                    if size == "네":
                        order_list.append(choi + number)
                        size_order=order_list.pop(-1)
                        pay_list.append(700*int(number))
                        print("주문내역:", order_list)
                        print("라지추가")
                        print("합계:%d원" % int((sum(pay_list))))# 각각 라지여부 따로 설정했을 때 계산 모르겠음
                    else:
                        order_list.append(choi + number)
                        size_order = order_list.pop(-1)
                        print("주문내역:", order_list)#사이즈에서 이전으로 돌아가서 메뉴 추가하고 다시 오면 이전항목 반영 안되어있음 #주문목록의 맨 마지막 리스트의 수량만 반영되어서 금액나옴 ex)상하이2,빅맥1=>빅맥1의 1만 700원 더해져서 계산값 산출됨
                        print("레귤러") #
                        print("합계:%d원" % int(sum(pay_list)))
                    fins = input("취소 or 이전 or 완료:")
                    if fins == "취소":
                        print("*" * 100)
                        n = 1
                        m = 1
                        cate = False
                        take0ut = False
                    elif fins == "이전":
                        print("*" * 100)
                        n = 1
                        m = 1
                        cate = False
                    elif fins == "완료":
                        print("*" * 100)  # 폼4.customize

                        sd = ["맥너겟", "해쉬브라운", "스트링치즈", "치즈스틱", "후렌치후라이", "스파이시맥너겟", "치킨스낵랩", "소시지스낵랩", "치킨텐더",
                              "맥플러리",
                              "콜라", "제로콜라", "사이다", "오렌지주스", "밀크쉐이크", "딸기쉐이크", "초코쉐이크", "환타", "생수", "우유"]
                        sd_price = [2000, 1200, 1400, 2000, 1500, 2100, 2000, 2200, 1900, 2500,
                                    1500, 1500, 1500, 1500, 2000, 2000, 2000, 1500, 1000, 1000]
                        while True:
                            cus = input("사이드추가 or 음료추가 or 선택안함 or 선택완료:")
                            while cus:
                                if cus == "사이드추가":
                                    print(sd[:10])
                                    choi1 = input("선택:")
                                    number = input("수량:")
                                    order_list.append(choi1 + number)
                                    pay_list.append(int(sd_price[sd.index(choi1)] * int(number)))
                                    print("남은수량:%d개" % int(sd_stock[sd.index(choi1)] - int(number)))
                                    if int(sd_stock[sd.index(choi1)]) - int(number) <= 0:
                                        print("재고가 없습니다.")
                                        del order_list[-1]
                                        del pay_list[-1]
                                        continue
                                    elif int(sd_stock[sd.index(choi1)]) - int(number) >0:
                                        break
                                elif cus == "음료추가":
                                    print(sd[10:])
                                    choi2 = input("선택:")
                                    number = input("수량:")
                                    order_list.append(choi2 + number)
                                    pay_list.append(int(sd_price[sd.index(choi2)] * int(number)))
                                    print("남은수량:%d개" % int(sd_stock[sd.index(choi2)] - int(number)))
                                    if int(sd_stock[sd.index(choi2)]) - int(number) <= 0:
                                        print("재고가 없습니다.")
                                        del order_list[-1]
                                        del pay_list[-1]
                                        continue
                                    elif int(sd_stock[sd.index(choi2)]) - int(number) > 0:
                                        break
                                else:
                                    print("선택안함/선택완료")
                                    print("주문내역:", order_list)
                                    print("합계:%d원" % int(sum(pay_list)))
                                    finc = input("완료?:")
                                    if finc == "네":
                                        print("*" * 100)  # 폼5.Last Menu Check
                                        while True:
                                            last = input("사이드변경 or 음료변경 or 변경/완료")
                                            while last:
                                                if last == "사이드변경":
                                                    if choi1 in sd:
                                                        print(sd[:10])
                                                        while True:
                                                            before = ["기존선택:", choi1]
                                                            print(before[0], before[1])
                                                            now = input("변경선택:")
                                                            number = input("수량:")
                                                            if before[1] in sd:
                                                                change_ch = (int(sd_price[sd.index(now)]) - int(sd_price[sd.index(choi1)]))*int(number) # 변경사항 차액
                                                                for i in order_list:
                                                                    temp = i.replace(choi1, now)
                                                                    change_list.append(temp)
                                                                print("주문내역:", change_list)
                                                                print("합계:%d원" % int((sum(pay_list)+(change_ch))))
                                                                p=0
                                                                if p==0:
                                                                    break
                                                                last=False


                                                    else:
                                                        print("주문하신 사이드메뉴가 없습니다.")
                                                        break
                                                elif last == "음료변경":
                                                    if choi2 in sd:
                                                        print(sd[10:])
                                                        p=0
                                                        while True:

                                                            before = ["기존선택:", choi2]
                                                            print(before[0], before[1])
                                                            now = input("변경선택:")
                                                            number = input("수량:")
                                                            if before[1] in sd:
                                                                change_ch = (int(sd_price[sd.index(now)]) - int(
                                                                    sd_price[sd.index(choi2)])) * int(number)  # 변경사항 차액

                                                                for i in order_list:
                                                                    temp=i.replace(choi2,now)
                                                                    change_list.append(temp)


                                                                print("주문내역:", change_list)
                                                                print("합계:%d원" % int((sum(pay_list) + (change_ch))))
                                                                p=p+1
                                                                if p==1:
                                                                    break
                                                                last=False

                                                            print("1212")
                                                    else:
                                                        print("주문하신 음료가 없습니다.")
                                                        break
                                                else:
                                                    finlm=input("이전 or 완료")
                                                    if finlm=="이전":
                                                        n = 1
                                                        m = 1
                                                        cate = False
                                                    elif finlm=="완료":
                                                        print("*"*100) #폼6.장바구니
                                                        print("장바구니")
                                                        print("")




        elif cate == "사이드" or cate == "음료":
            sd = ["맥너겟", "해쉬브라운", "스트링치즈", "치즈스틱", "후렌치후라이", "스파이시맥너겟", "치킨스낵랩", "소시지스낵랩", "치킨텐더", "맥플러리", "콜라", "제로콜라",
                  "사이다", "오렌지주스", "밀크쉐이크", "딸기쉐이크", "초코쉐이크", "환타", "생수", "우유"]
            sd_price = [2000, 1200, 1400, 2000, 1500, 2100, 2000, 2200, 1900, 2500, 1500, 1500, 1500, 1500, 2000, 2000,
                        2000, 1500, 1000, 1000]
            if cate == "사이드":
                print(sd[:10])
            elif cate == "음료":
                print(sd[10:])
            while True:
                choi = input("선택:")
                number = int(input("수량"))
                if choi in sd:
                    print(choi, number, "개, %d원" % (sd_price[sd.index(choi)] * number))
                    ask = input(more)
                    if ask == "네":
                        continue
                    else:
                        finm = input("이전 or 완료:")
                        if finm == "이전":
                            print("*" * 100)
                            break
                            take0ut = False
                        elif finm == "완료":
                            print("*" * 100)  # 폼5.Last Menu Check
                            while True:
                                last = input("사이드변경 or 음료변경 or 선택안함:")
                                if last == "사이드변경":
                                    if choi in sd[:10]:
                                        print(sd[:10])
                                        while True:
                                            before = input("기존선택:")
                                            now = input("변경선택:")
                                            if (before and now) in sd:
                                                print(before, "=>", now, "변경, 차액 %d원" % (
                                                            int(sd_price[sd.index(now)]) - int(
                                                        sd_price[sd.index(before)])))
                                                # change_ch=(int(sd_price[sd.index(now)]) - int(sd_price[sd.index(before)])) #변경사항 차액
                                                break
                                    else:
                                        print("기존 선택된 사이드메뉴가 없습니다.")
                                        print("*" * 100)
                                elif last == "음료변경":
                                    if choi in sd[10:]:
                                        print(sd[10:])
                                        while True:
                                            before = input("기존선택:")
                                            now = input("변경선택:")
                                            if (before and now) in sd:
                                                print(before, "=>", now, "변경, 차액 %d원" % (
                                                            int(sd_price[sd.index(now)]) - int(
                                                        sd_price[sd.index(before)])))
                                                # change_ch=(int(sd_price[sd.index(now)]) - int(sd_price[sd.index(before)])) #변경사항 차액
                                                break
                                    else:
                                        print("기존 선택된 음료메뉴가 없습니다.")
                                        print("*" * 100)
                                elif last == "선택안함":
                                    finl = input("이전 or 완료")
                                    if finl == "이전":
                                        break
                                    elif finl == "완료":
                                        print("*" * 100)  # 폼6.장바구니
                                        break

                            break
                break
            break
