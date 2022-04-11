import time as t
print(t.time())
#UTC라는 시간을 기준으로 얼마나 경과되었는가
#UTC : 협정 세계 표준시, 1970년 1월 1일 0시 0분 0초 기준
#초단위, 실수형태

print(t.localtime)
#연도-월-일-시간-분-초-요일 등 형태로 표현하는 함수
print(t.asctime(t.localtime()))
print(type(t.asctime(t.localtime())))

print(t.ctime())

print(t.strftime('%a',t.localtime()))
#  %a 요일(짧은버전) / %A 요일(풀버전) / %w 요일(숫자버전,0~6,0이 일요일 /
#  %d 일(01~31) / %b 월(짧은버전) /  %B 월(풀버전) /  %m 월(숫자버전, 01~12) /
#  %y 연도(짧은 버전) / %Y 연도(풀버전) / %H 시간(00~23) / %l 시간(00~12) /
#  %p AM/PM /  %M 분(00~59) /  %S 초(00~59) /  %f 마이크로초(000000~999999)/
#  %Z 표준시간대(ex.PST) /  %j 1년중 며칠째인지 (001~366) /
#  %U 1년 중 몇 주째인지(00~53, 일요일이 한 주의 시작이라고 가정)/
#  %W 1년 중 몇 주째인지(00~53, 월요일이 한 주의 시작이라고 가정)/


for i in range(5):
    print(i)
    t.sleep(0.3) #프로세스가 ()초 동안 잠깐멈추고 실행 #많이쓰임

import calendar as c
print(c.calendar(2022,10)) #x년의 달력이 y간격으로 쭉나옴

print(c.weekday(2015,1,1))

print(c.monthrange(2022,10)) #튜플형태로 출력, [0]값은 요일(0~6,0이 월요일)/[1]값은 몇일까지 있는지

import random as rd
for i in range(100):
    print(rd.random())
#ramdom모듈의 random함수는 0.0~1.0 사이의 실수 형태 난수 생성

listx=[]
for i in range(10000):
    listx.append(int(rd.random()*11)+20)
print("*"*100)
print(max(listx))
print("*"*100)
for i in range(100):
    print(rd.randint(1,45))