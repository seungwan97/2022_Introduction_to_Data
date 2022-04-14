"""
1. 학생의 정보 : 이름, 성별, 점수, i or e,
2. 학생의 정보는 클래스 구조로 객체화
3. 학생의 정보는 txt파일로 존재 (형식제공)
4. random모듈을 이용하여 셔플
5. 조는 x인 구성 (x는 input 가능)
6. 조당 x명의 점수 합이 다른 조의 구성 점수 총합과 오차범위 +-10점
7. 조원의 MBTI가 전부 I이거나 전부 E면 안됨
9. 맞는범위가 나올때까지 알아서 돌아가게 할 것
"""
XXX=open("220414_random draw_sample_update.txt", 'r', encoding='UTF-8')
list_all=XXX.readlines()
list1 = []
stu_list = []
for i in list_all:
    if "이름" in i:
        continue
    else:
        list1.append(i.replace("\n", ""))
for i in list1:
    stu_list.append(i.split("\t"))

def cleandata(x):
    global name
    global gender
    global score
    global mbti
    name=[]
    gender=[]
    score=[]
    mbti=[]
    age=[]
    for i in x:
        name.append(i[0])
        gender.append(i[1])
        score.append(i[2])
        mbti.append(i[3])
        age.append(i[4])
    return name, gender, score, mbti, age

class student:
    info = '학생정보'
    def __init__(self,name,gender,score,mbti,age):
        self.name = name
        self.gender = gender
        self.score = score
        self.mbti = mbti
        self.age = age

def howmany(e):
    start = 0
    div = e
    listx = []
    z = 0
    result1 = []
    result2 = []
    list3=[]
    for i in range(start, len(h1.name), div):
        result1.append(h1.name[i:i + div])
    ageint=list(map(int,h1.age))
    for i in range(start, len(ageint), div):
        result2.append(ageint[i:i + div])
    for i in range(start, len(h1.name) + div, div):
        s1 = h1.name[start:start + div]
        if s1 != []:
            for m in range(0, len(h1.name) // div):
                listx.append(m + 1)
            if len(s1) >= div:
                print("%d조:" % listx[z], s1)
                for n in range(len(result2)):
                    a = result1[n][result2[n].index(max(result2[n]))]
                    list3.append(a)
                print("%d조 조장:" % listx[z],list3[z])
            else:
                print("깍두기조:", s1)
                for n in range(len(result2)):
                    a = result1[n][result2[n].index(max(result2[n]))]
                    list3.append(a)
                print("깍두기조 조장:",list3[z])
            z = z + 1
        start = start + div

def whatmbti(e):
    start = 0
    div = e
    listmbti=[]
    listmbtiint=[]
    for i in range(start, len(h1.mbti) + div, div):
        s1 = h1.mbti[start:start + div]
        if s1 != []:
            listmbti.append(s1)
            for m in listmbti:
                a=m.count("I")
                b=m.count("E")
            listmbtiint.append(a)
            listmbtiint.append(b)

        start = start + div
    return listmbtiint

def totalscore(e):
    start = 0
    div = e
    listscore=[]
    for i in range(start, len(h1.score) + div, div):
        s1 = h1.score[start:start + div]
        if s1 != []:
            ints1=list(map(int, s1))
            if len(ints1)==div:
                sum(ints1)
                listscore.append(sum(ints1))
        start = start + div
    return listscore

import random as rd
listscore = []
people = int(input("몇명:"))
print("편성중입니다.")
while True:
    rd.shuffle(stu_list)
    x=cleandata(stu_list)
    h1 = student(x[0], x[1], x[2], x[3], x[4])
    y=whatmbti(people)
    z=totalscore(people)
    if max(z)-min(z)<=10:
        if people not in y:
            print("*"*100)
            print("편성완료")
            howmany(people)
            print("한 팀당 I와 E의 수(2개씩 끊어서 보기):", y)
            print("구성원이 이루어졌을 시 각 조 총점:", z)
            print("조편성가능")
            break
        else:
            continue
    else:
        continue