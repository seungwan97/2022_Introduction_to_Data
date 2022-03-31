XXX=open("코로나.txt",'r',encoding='UTF-8')
list_all=XXX.readlines()
listdaily=[]
#n제거
#t제거
#,제거

def notn(s,e):
    list_temp=[]
    list_res=[]
    for i in list_all:
        if "\n" in i:
            listdaily.append(i)
            for m in listdaily:
                m.replace("\n","")
            print(m)
notn()

def nott():
    for i in list_all:
        if "\n" in i:
            listdaily.append(i)
            for m in listdaily:
                m.replace("\t","")
            print(m)
nott()
"""
    #일일 확진자
    a=listdaily[0][3:].replace(",","")
    a1=a.replace("\n","")
    list_day=a1.split("\t")
    print(list_day)
    #신규입원 현황
    b1=listdaily[1][3:].replace("\n","")
    list_new=b1.split("\t")
    print(list_new)
    #중환자
    c1=listdaily[2][3:].replace("\n","")
    list_wor=c1.split("\t")
    print(list_wor)
    #사망자
    d1=listdaily[3][3:].replace("\n","")
    list_die=d1.split("\t")
    print(list_die)

    list_day_int=map(int, list_day)
    avg=sum(list_day_int)/len(list_day)
print("3.25~3.31 일일 확진자 평균: %d명" % avg)

list_new_int=map(int, list_new)
print("1주일간 확진자 대비 입원비율: %0.2f%%" % (sum(list_new_int)/(sum(list_day_int)/100)))

list_die_int=map(int, list_die)
print("1주일간 확진자 대비 사망인원비율: %0.2f%%" % (sum(list_die_int)/(sum(list_day_int)/100)))
"""













"""
for m in listdaily:
    if "," in m:
        m.replace(",","")
        continue
    else:
        m=m[3:]
        m.split("\t")
        m[-1].replace("\n","")
print(m)

"""


"""
def add(*a):
    res=0
    for i in list_all:
        res=res+i
    return res
result=add(1,2,3,4,5,6,7,8,9,10) #a는 튜플형태로 저장됨
print(result)

XXX.close()



XXX=open("코로나.txt",'r',encoding='UTF-8')

lines=XXX.readlines()
daily=lines[2]
daily2=daily.split("\t")
a=daily2[-1].replace("\n","")
daily2.pop()
daily2.append(a)
daily3=daily2[1:]
daily3int=map(int, daily3) #일일 확진자 리스트
q1=sum(daily3int) #일일 확진자 총합
hosp=lines[6]
hosp2=hosp.split("\t")
b=hosp2[-1].replace("\n","")
hosp2.pop()
hosp2.append(b)
hosp3=hosp2[1:]
hosp3int=map(int,hosp3) #신규입원현황 리스트
q2=sum(hosp3int) #신규입원현황 총합
sick=lines[10]
sick2=sick.split("\t")
c=sick2[-1].replace("\n","")
sick2.pop()
sick2.append(c)
sick3=sick2[1:]
sick3int=map(int,sick3) #중환자 리스트
die=lines[14]
die2=die.split("\t")
d=die2[-1].replace("\n","")
die2.pop()
die2.append(d)
die3=die2[1:]
die3int=map(int,die3) #신규입원현황 리스트
q4=sum(die3int) #신규입원현황 총합
print(daily3)
print(hosp3)
print(sick3)
print(die3)
print("3.25~3.31 일일 확진자 평균:",int((q1)/len(daily3)))
print("1주일간 확진자 대비 입원비율: %0.3f%%" % (q2/(q1/100)))


print("계속 증가하는 추세를 보이는 항목:",lines[8])
print("1주일간 확진자 대비 사망인원비율: %0.3f%%" % (q4/(q1/100)))
XXX.close()

#def daily(x):
#    lines[2]
"""