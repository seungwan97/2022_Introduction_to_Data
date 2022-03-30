#함수
#기능이 정해져있다.
#기능단위

#과일:재료 / input / 입력값
#믹서기:함수 / function
#주스:결괏값 / output / return / 반환

#함수를 사용하는 이유?

#사용자에게 16자리 카드번호를 입력받아서(문자열)
#카드 번호의 자릿수가 16자리인지 유효성 검토
#카드 번호 16자리가 모두 숫자형태의 문자로 되어있는지 검토
#입력양식 = (xxxx-xxxx-xxxx-xxxx) 하이픈 포함하여 입력
#처리할 때 하이픈 제거 후 처리


x=[0,1,2,3,4,5,6,7,8,9]
while True:
    card = input("카드번호 입력,입력양식:xxxx-xxxx-xxxx-xxxx")
    if len(card) == 19:
        data=card.split('-')
        carddata="".join(data)
        carddatalist=list(carddata)
        if carddatalist[0] in x :
            if int(carddata) in range(0,10000000000000000):
                print("유효한 카드입니다.")
                break
        else:
            print("숫자형태가 아님. 유효한 카드가 아닙니다.")
            break
    else:
        print("자릿수 오류. 유효한 카드가 아닙니다.")
        continue

sample="0123456789"
#if len(cardnum)==19:
while True:
    cardnum = input("카드번호입력:")
    if len(cardnum)==19:
        cardnum_list = cardnum.split('-')
        if len(cardnum_list)==4:
            for i in cardnum_list:
                if len(i)==4:
                    for m in cardnum_list:
                        for n in m:
                            if n in sample:
                                pass
                            else:
                                print("숫자형태가 아님. 유효한 카드가 아닙니니다.")
                                continue
                else:
                    print("번호가 각 4개씩 구성되지 않음. 유효한 카드가 아닙니다.")
                    continue
        else:
            print("-이 3개가 아님. 유효한 카드가 아닙니다.")
            continue
    else:
        print("카드번호가 16개가 아님. 유효한 카드가 아닙니다.")
        continue
        


#파이썬 함수 만드는 방법
def myprint(): #함수의 정의/생성방법 #호출보다 먼저 나와야 한다.
    print("안녕하세요")
    print("123")
myprint() #함수의 사용/호출방법 #정의보다 뒤에 위치해야 한다.

#def x1(매개변수):
#매개변수:재료를 넣는 칸
#매개변수명:마음대로 지으면 된다.

def myprint2(x):
    x=x+1
    print(x)
myprint2(100)



def myfunc(x,y):
    print(x)
    print(y)
myfunc(100,200)


def myfunc2():
    print("함수 수행문")
myfunc2()

def myfunc3(x):
    print(x)
myfunc3("재료")

def myfunc4():
    return 'hello'
str1=myfunc4()

def myfunc5(x):
    return x + 'hello'
text1=myfunc5("say")
print(text1)

def myfunc6(x):
    return x + "김승완"
p1=myfunc6("이름:")
print(p1)

m = float(input("키(단위cm):")) #float:실수형태
kg = float(input("몸무게"))
def mybmi(x,y): #키,몸무게
   z=y/((x*0.01)**2)
   return z
bmi=mybmi(m,kg)
print("%.1f" % bmi) #소수점 1자리까리 표현하도록 포매팅


def add(a,b):
    return a+b
add(b=1,a=2) #순서를 지정하는 것도 가능

#함수의 입력값이 몇개가 될지 모를때
#def 함수이름(*매개변수):
def add(*a): #매개변수 앞에 *을 붙여놓으면 몇개든 호출할수 있다.
    res=0
    for i in a:
        res=res+i
    return res
result=add(1,2,3,4,5,6,7,8,9,10) #a는 튜플형태로 저장됨
print(result)




#매개변수: 재료 넣는 칸의 이름 parameter
#인수: 함수를 호출할 때 전달하는 입력값을 의미한다.

#함수의 구분:매개변수의 유무
#return의 유무


# + - / * 함수중 4개를 정의 및 호출해보기
#사용자 입력값 2개를 입력받아 두 수를 사칙연산.
x=input("첫번쨰")
y=input("두번째")
list1=[]
list2=[]
def add(f,s):
    #두 재료가 숫자형태의 문자열이면 사칙연산+결과 출력
    sample="0123456789"
    m=0
    for i in s+f:
        if i in sample:
            m=m+1
            if m==len(s+f):
                print(int(f) + int(s))

add(x,y)



#매개변수: 재료 넣는 칸의 이름 parameter
#인수: 함수를 호출할 때 전달하는 입력값을 의미한다.

#함수의 구분:매개변수의 유무
#return의 유무


#print("a","b","c")
#myprint("a","b","c") #결과값이 a b c 가 아닌 abc로 나오는 함수myprint를 만들어보기

def myprint(*x):
    sample=""
    for i in x:
        sample=sample+i
    return sample
alpa=myprint("a","b","c")
print(alpa)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def cal(a,b,m):
    if m=="더하기":
        return a+b
    elif m=="빼기":
        return a-b
print(cal(10,5,"빼기"))

def breaking():
    print(1)
    return 123, 222  #return은 반환임과 동시에 탈출(break)이기도 하기때문에 이후 내용은 읽히지 않는다.
    #return은 한번에 두개는 못쓰지만 그 값은 두개이상 쓸 수 있다. (이때 출력값은 튜플로 나옴)
res=breaking()
print(res)

def hello(age,name,man=True): #여기서 마지막 매개변수에 True를 지정해놓는것은 미리 조건을 설정해놓을수도 있다는 것을 보여줌
                              #미리 조건을 설정하는 것은 맨 마지막 매개변수만 지정가능함
    print("이름은 %s" % name)
    print("나이는 %d" % age)
    if man:
        print("성별은 남성")
    else:
        print("성별은 여성")
hello(10,"mmm") #미리 조건을 설정(man=True) 했다면 총 3칸이아닌 한칸을 비워놓을 수도 있음

x="hello"
print(x.split())

x=10
def hello(): #재귀함수,재귀호출 : 끊임없이 값을 호출하는것 #특징:1000번까지 재귀된다.(limit이 정해져있음)
    print("hello")
    global x #global은 전역변수를 선언하는 것으로, 밖에 있는 값에 영향을 받아 안에 있는 값을 실제로 변하게 함
    x=x-1
    if x>0:
        hello()
hello()
print(x)

x=10 #전역변수x
def func1(x): #매개변수x
    print(x) #매개변수x
func1(x) #전역변수x

x=10 #전역변수x
def func2(a): #매개변수a
    global x #전역변수x
    print(x) #전역변수x
    print(a) #매개변수a
    print(x+a)
func1(x) #전역변수x

x=10

#랑다 표현 lambda
mul=lambda a,b:a*b #a와 b를 받아서 하는일은 a*b이다 라는 뜻
print(mul(3,4))
#기존 표현 def
def mul2(a,b):
    return a*b
print(mul2(4,3))
#여기서 랑다표현과 기존표현으로 만든 두 코드는 같은 뜻임 #랑다표현은 잘 안씀