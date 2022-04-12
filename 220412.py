#클래스
#class

#절차지향 프로그래밍 언어 : C언어
#객체지향 프로그래밍 언어 : 파이썬, 자바스크립트
#클래스는 꼭 필요하지는 않다.

class Calculator:
    #클래스의 정의 : 일종의 틀을 만드는것
    def __init__(self):
        self.result=0

    def add(self,num):
        self.result+=num
        return self.result

    def minus(self,num):
        self.result-=num
        return self.result

    def double(self,num):
        self.result*=num
        return self.result

c1=Calculator() #c1객체를 생성함 : cal 클래스를 이용해서 만듬
c2=Calculator() #c2객체를 생성함 : cal 클래스를 이용해서 만듬
#같은 클래스로 생성한 객체끼리는 상호 영향을 주지 않고 독립적이다.

print(c1.add(5))
print(c2.add(10))
print(c1.add(3))
print(c1.minus(7))
print(c2.double(10))

class cookie: #클래스명이 cookie
    pass
ck1=cookie() #객체명이 ck1
ck2=cookie() #객체명이 ck2

#객체는 클래스의 인스턴스이다.
#클래스:틀
#클래스로 만든 객체를 인스턴스라고도 한다.
#ck1 객체는 cookie클래스의 인스턴스
#ck1은 인스턴스이다.
#ck1은 쿠키클래스의 인스턴스이다.

class FourCal:
    lastname='김' #클래스 변수
    def __init__(self,x,y): #생성자 메서드 #객체 생성과 동시에 실행
        self.first=x
        self.second=y
    def setdata(self,x,y): #클래스 내부 함수:메서드
        self.first=x
        self.second=y
    def add(self):
        result=self.first+self.second
        return result
a=FourCal(4,5)
print(type(a))
x=10
print(type(x))
a.setdata(4,2)
#첫 매개변수 self는 특별한 기능이 있다.
#setdata 메서드의 첫 매개변수 self에는 setdata 메서드를 호출한 객체 a가 자동으로 전달된다.
print(a.first)
print(a.second)

FourCal.setdata(a,5,3)
print(a.first)

x1=FourCal(4,5)
x2=FourCal(4,5)

x1.setdata(3,5)
x2.setdata(100,200)

print(x1.first)
print(x2.first)
print(x1.add())
print(x1.first)

#__init__메서드
#생성자 메서드

a=FourCal(4,5)
print(a.first)
print(a.second)
b=FourCal(40,50)
b.setdata(400,500)
print(b.first)

print(a.add())

#클래스의 상속
#물려받기

class FourCal2(FourCal):
    def pow(self):
        result=self.first**self.second
        return result
x=FourCal2(10,20)
print(x.first)
print(x.add())

#왜 상속을 하는가?
#기존 클래스를 보존하면서 기존 클래스의 기능에 변경이나 추가를 원한다면 상속한다.
print(x.pow())

#라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황과 같은 경우 상속받아서 쓴다.

#메서드 오버라이딩
class F3(FourCal):
    def add(self):
        print("123123123")

v=F3(20,10)
print(v.first)
print(v.second)
print(v.add())
print(FourCal.add(v))
#부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서도 오버라이딩(덮어쓰기)라고 한다.
#이렇게 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.

#클래스 변수

class Family:
    lastname='김'
    def __init__(self,x,y):
        self.a=x
        self.b=y
F1=Family(10,20)
F2=Family(40,50)

print(F1.a,F1.b,Family.lastname)
print(F2.a,F2.b,F2.lastname)

print(id(F1.lastname)) #클래스변수는 같은 메모리값을 갖는다.
print(id(F2.lastname)) #클래스변수는 같은 메모리값을 갖는다.
print(id(F1.a))
print(id(F2.a))

#클래스 변수 접근 방법
#1. 객체명.클래스변수명
#2. 클래스명.클래스변수명

#클래스 함수 호출 방법
#1. 객체명.메서드명
#2. 클래스명.메서드명

#은행계좌 account 라는 클래스 생성
#5명의 객체 생성
# 기능:메서드 / 속성:클래스변수
#속성: 예금주명,잔액,은행명,계좌번호
# =>클래스변수로 만든다.
#단, 개별적인 정보를 부여해야 할때는 =>객체변수로 만든다.
#기능: 입금,출금,잔액확인
#1.공통속성:클래스변수
#2.객체속성:객체변수
#생성자 메서드 구현

class account:
    name = '김승완'
    accountnumber = '98000310201014'
    bank = '농협'
    def __init__(self):
        self.result = 0
    def inMoney(self,num):
        self.result+=num
        return num
    def outMoney(self,num):
        self.result-=num
        return num
    def confirmMoney(self):
        return self.result
m = account()
print("계좌정보:",account.name,account.accountnumber,account.bank)
print("입금금액:",m.inMoney(10000))
print("잔액:",m.confirmMoney())
print("출금금액:",m.outMoney(3000))
print("잔액:",m.confirmMoney())
print("입금금액:",m.inMoney(1000))
print("잔액:",m.confirmMoney())

class account2:
    clvar= "계좌정보"
    def __init__(self,name,bal,bank,accnum):
        self.name=name
        self.bal=bal
        self.bank=bank
        self.accnum=accnum
    def inM(self,m):
        self.bal+=m
        return self.bal
    def outM(self,m):
        self.bal-=m
        return self.bal
    def checkBal(self):
        print(self.bal)

h1=account2('학생1',10000,'농협',123456789)
print(h1.clvar)
print(h1.name)
print(h1.bank)
print(h1.accnum)
print(h1.bal)
h1.inM(30000)
print(h1.bal)


def addH(a,b,c,d):
    global listx
    listx.append(account2(a,b,c,d))
listx=[]
while True:
    mode = input("1.추가 2.종료")
    if mode =="1":
        a = input("이름")
        b = int(input("잔액"))
        c = input("은행")
        d = int(input("계좌번호"))
        addH(a, b, c, d)
    else:
        break

for i in range(len(listx)):
    print(listx[i].clvar)
    print(listx[i].name)
    print(listx[i].bal)



for n in range(len(listx)):
    globals()['no_{}'.format(n)]=listx[n]

print(no_1)