import os.path #path경로를 가져오기 위한 모듈
path= "module_jejuhotel_220407_unfinished.py"
print(os.path.isfile(path)) #path변수에 저장되어 있는 파일이 존재하는지 여부

XXX=open("제주관광호텔업.txt",'r',encoding='UTF-8')
list_all=XXX.readlines()
hotel_n_money={}
hotel_n_rooms={}
hotel=[]
rooms=[]
money=[]
star1 = {}
star2 = {}
star3 = {}
star4 = {}
star5 = {}

def hoteljeju_to_list(x): #해당도시의 호텔목록을 나타내는 함수 #매개변수:도시명
    list_1 = []
    list_2 = []
    list_3 = []
    hotel=[]
    rooms=[]
    money = []
    for i in open("제주관광호텔업.txt",'r',encoding='UTF-8').readlines():
        if x == "제주시":
            if "관광호텔업" and "도 제주시" in i:
                list_1.append(i)
        elif x == "서귀포시":
            if "관광호텔업" and "도 서귀포시" in i:
                list_1.append(i)
    for i in list_1:
        temp = i.replace('\n', '')
        list_2.append(temp)
    for i in list_2:
        list_3.append(i.split('\t'))
    for i in list_3:
        hotel.append(i[1])
        rooms.append(i[3])
        money.append(i[4])
    start = 0
    end = len(hotel)
    div = 5
    for i in range(start, end + div, div):
        star = hotel[start:start + div]
        if star != []:
            print(star)
        start = start + div
    print("총 %d개" % len(hotel))

def hotel_n_money_dict(x): #해당도시의 호텔당 1박 숙박료 #매개변수:도시명
    hotel = []
    rooms = []
    money = []
    def hoteljeju_to_list():  # 해당도시의 호텔목록을 나타내는 함수 #매개변수:도시명
        list_1 = []
        list_2 = []
        list_3 = []

        for i in open("제주관광호텔업.txt", 'r', encoding='UTF-8').readlines():
            if x == "제주시":
                if "관광호텔업" and "도 제주시" in i:
                    list_1.append(i)
            elif x == "서귀포시":
                if "관광호텔업" and "도 서귀포시" in i:
                    list_1.append(i)
        for i in list_1:
            temp = i.replace('\n', '')
            list_2.append(temp)
        for i in list_2:
            list_3.append(i.split('\t'))
        for i in list_3:
            hotel.append(i[1])
            rooms.append(i[3])
            money.append(i[4])
    hoteljeju_to_list()
    hotel_n_money = {hotelname: roomcount for hotelname, roomcount in zip(hotel, list(map(int, money)))}
    hotel_n_rooms = {hotelname: roomcount for hotelname, roomcount in zip(hotel, list(map(int, rooms)))}
    for k, v in hotel_n_money.items():
        result="{} : {}".format(k, v)
        print(result)



def hotel_to_star(x):
    star1 = {}
    star2 = {}
    star3 = {}
    star4 = {}
    star5 = {}

    hotel = []
    rooms = []
    money = []

    def hoteljeju_to_list():  # 해당도시의 호텔목록을 나타내는 함수 #매개변수:도시명
        list_1 = []
        list_2 = []
        list_3 = []

        for i in open("제주관광호텔업.txt", 'r', encoding='UTF-8').readlines():
            if x == "제주시":
                if "관광호텔업" and "도 제주시" in i:
                    list_1.append(i)
            elif x == "서귀포시":
                if "관광호텔업" and "도 서귀포시" in i:
                    list_1.append(i)
        for i in list_1:
            temp = i.replace('\n', '')
            list_2.append(temp)
        for i in list_2:
            list_3.append(i.split('\t'))
        for i in list_3:
            hotel.append(i[1])
            rooms.append(i[3])
            money.append(i[4])

    hoteljeju_to_list()
    hotel_n_money = {hotelname: roomcount for hotelname, roomcount in zip(hotel, list(map(int, money)))}
    hotel_n_rooms = {hotelname: roomcount for hotelname, roomcount in zip(hotel, list(map(int, rooms)))}

    for i in hotel_n_money.keys():
        if hotel_n_rooms[i]<50:
            star1[i]=hotel_n_money[i]
        if 50<=hotel_n_rooms[i]<100:
            star2[i]=hotel_n_money[i]
        if 100 <= hotel_n_rooms[i] < 150:
            star3[i]=hotel_n_money[i]
        if 150 <= hotel_n_rooms[i] < 200:
            star4[i]=hotel_n_money[i]
        if hotel_n_rooms[i] >= 200:
            star5[i]=hotel_n_money[i]


def line_up(x):
    start = 0
    end = len(x)
    div = 5
    for i in range(start, end + div, div):
        star = x[start:start + div]
        if star != []:
            print(star)
        start = start + div

def line_up_dict(x):
    for k, v in x.items():
        print("{} : {}".format(k, v))

def priceupanddown(x,y):
    list1 = []
    list2 = []
    list3 = []
    for i in x.items():
        list1.append(list(i))
        list2.append(i[1])
    a = y(list2)
    for i in list1:
        if a in i:
            list3.append(i)
    print(list3)

if __name__=="__main__":

    while True:
        hotel.clear()
        rooms.clear()
        star1.clear()
        star2.clear()
        star3.clear()
        star4.clear()
        star5.clear()
        city = input("제주시 or 서귀포시:")
        if city == "제주시" or city == "서귀포시":
            print("%s 호텔현황" % city)
            print("*" * 100)
            hoteljeju_to_list(city)
            while True:
                room = input("호텔별 1박요금을 보시겠습니까?(네/아니오):")
                if room == "네":
                    print("*" * 100)
                    print("%s 호텔 별 1박 요금" % city)
                    print("*" * 100)
                    hotel_n_money_dict(city)
                    break
                elif room == "아니오":
                    break
                else:
                    print("잘못 입력하셨습니다. 네/아니오로 대답해주세요.")
                    print("*" * 100)
                    continue
        else:
            print("제주도에 속해있지 않은 지역입니다. 다시 선택해주십시오.")
            print("*" * 100)
            continue
        while True:
            print("*" * 100)
            star = input("1성 or 2성 or 3성 or 4성 or 5성:")
            if star=="1성":
                print("1성급호텔 목록")
                print("*" * 100)
                hotel_to_star(city)
                print(star1)
                print("총 %d개" % len(star1))
            elif star == "2성":
                print("2성급호텔 목록")
                print("*" * 100)
                hotel_to_star(city)
                print("총 %d개" % len(star2))
            elif star == "3성":
                print("3성급호텔 목록")
                print("*" * 100)
                hotel_to_star(city)
                print("총 %d개" % len(star3))
            elif star == "4성":
                print("4성급호텔 목록")
                print("*" * 100)
                hotel_to_star(city)
                print("총 %d개" % len(star4))
            elif star == "5성":
                print("5성급호텔 목록")
                print("*" * 100)
                hotel_to_star(city)
                print("총 %d개" % len(star5))
            else:
                print("잘못입력하셨습니다.")
                continue
            break
        while True:
            price=input("해당 호텔 중 최저가 or 최고가 가격을 보시겠습니까?(최저가/최고가):")
            if price=="최저가":
                if star=="1성":
                    priceupanddown(star1,min)
                elif star=="2성":
                    priceupanddown(star2, min)
                elif star == "3성":
                    priceupanddown(star3, min)
                elif star == "4성":
                    priceupanddown(star4, min)
                elif star == "5성":
                    priceupanddown(star5, min)
            elif price=="최고가":
                if star == "1성":
                    priceupanddown(star1, max)
                elif star == "2성":
                    priceupanddown(star2, max)
                elif star == "3성":
                    priceupanddown(star3, max)
                elif star == "4성":
                    priceupanddown(star4, max)
                elif star == "5성":
                    priceupanddown(star5, max)
            else:
                print("잘못 입력하셨습니다. 다시 입력해주세요.")
                print("*" * 100)
                continue

            break












"""
    while True:
        print("*" * 100)
        otherhotel=input("다른 호텔을 찾으십니까?(네/아니오):")
        if otherhotel =="네":
            hoteljeju_to_list(city)
            print("%s 호텔현황" % city, "(총 %d개)" % len(hotel))
            line_up(hotel)
            jejuislandhotel = input("호텔명 입력(목록에 등록된 정확한 상호명을 입력해주세요.):")
            if jejuislandhotel in hotel:
                star_standard(jejuislandhotel)
                namemain()
                break
            else:
                print("%s에 등록된 호텔이 아닙니다. 다시 입력해주세요." % city)
        elif otherhotel =="아니오":
            namemain()
            break
        else:
            print("잘못 입력하셨습니다. 네/아니오로 대답해주세요.")
            continue
"""







