import os.path #path경로를 가져오기 위한 모듈
path="module_ksw.py"
print(os.path.isfile(path)) #path변수에 저장되어 있는 파일이 존재하는지 여부

XXX=open("제주관광호텔업객실수.txt",'r',encoding='UTF-8')
list_all=XXX.readlines()

hotel_n_rooms={}
hotel=[]
rooms=[]
star1 = []
star2 = []
star3 = []
star4 = []
star5 = []


def hotel_to_list():
    list_1=[]
    list_2=[]
    list_3=[]
    for i in list_all:
       if "관광호텔업" in i:
           list_1.append(i)
    for i in list_1:
        temp = i.replace('\n', '')
        list_2.append(temp)
    for i in list_2:
        list_3.append(i.split('\t'))
    for i in list_3:
        hotel.append(i[1])

def rooms_to_list():
    list_1=[]
    list_2=[]
    list_3=[]
    for i in list_all:
       if "관광호텔업" in i:
           list_1.append(i)
    for i in list_1:
        temp = i.replace('\n', '')
        list_2.append(temp)
    for i in list_2:
        list_3.append(i.split('\t'))
    for i in list_3:
        rooms.append(i[2])
rooms_to_list()

def hotel_n_rooms_dict():
    global hotel_n_rooms
    hotel_n_rooms={hotelname:roomcount for hotelname, roomcount in zip(hotel,list(map(int,rooms)))}

def star_standard(x):
    hotel_n_rooms_dict()
    if hotel_n_rooms[x]<50:
        print("1성급호텔")
    elif 50<=hotel_n_rooms[x]<100:
        print("2성급호텔")
    elif 100 <= hotel_n_rooms[x] < 150:
        print("3성급호텔")
    elif 150 <= hotel_n_rooms[x] < 200:
        print("4성급호텔")
    elif hotel_n_rooms[x] >= 200:
        print("5성급호텔")

def hotel_to_star():
    for i in hotel_n_rooms.keys():
        if hotel_n_rooms[i]<50:
            star1.append(i)
        elif 50<=hotel_n_rooms[i]<100:
            star2.append(i)
        elif 100 <= hotel_n_rooms[i] < 150:
            star3.append(i)
        elif 150 <= hotel_n_rooms[i] < 200:
            star4.append(i)
        elif hotel_n_rooms[i] >= 200:
            star5.append(i)
    print("1성급호텔 목록:%s" % star1[:])
    print("2성급호텔 목록:%s" % star2[:])
    print("3성급호텔 목록:%s" % star3[:])
    print("4성급호텔 목록:%s" % star4[:])
    print("5성급호텔 목록:%s" % star5[:])


while True:
    hotel_to_list()
    print("제주 관광호텔업 업체목록")
    print(hotel)
    rc=input("객실수를 확인하시겠습니까?(네/아니오):")
    if rc=="네":
        hotel_n_rooms_dict()
        print("호텔별 객실수")
        print(hotel_n_rooms)
    elif rc=="아니오":
        pass
    else:
        print("잘못된 명령입니다. 네,아니오로만 응답해주십시오.")
        print("*" * 100)
        continue
    while True:
        jejuhotel = input("호텔명 입력(목록에 등록된 정확한 상호명을 입력해주세요.):")
        while jejuhotel:
            if jejuhotel in hotel:
                star_standard(jejuhotel)
                if __name__=="__main__":
                    hotel_to_star()
                    print("*" * 100)
                    break
                else:
                    print("*" * 100)
                    break
            else:
                print("제주 관광호텔업에 등록된 호텔이 아닙니다. 다시 입력해주세요")
                print("*"*100)
                break
