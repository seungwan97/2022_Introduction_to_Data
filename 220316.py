#리스트 데이터 타입 : 여러 요소의 집합을 표현하는 데이터 타입을 말한다.
name="SW"
list1=['가','나','다'] #리스트를 만들 때는 대괄호로 감싸고 요솟값은 쉼표로 구분한다.
list1=3 #이처럼 변수이름이 같게 두번 생성되고 다른 요솟값이 들어갈 경우에는 후순위로 생성된 변수가 덮어쓰게 되므로 주의할 것
print(list1)
list1=[] #요소0
list2=[1,2,3] #요소3 / 숫자,숫자,숫자
list3=['r','e','f'] #요소3 / 문자,문자,문자
list4=[1,2,3,'a','b'] #요소5 /숫자,숫자,숫자,숫자,숫자
list5=[1,2,[1,2,[1,2,3,[1,2]]]] #요소3 / 숫자,숫자,리스트(아무리 많이 중첩되도 하나의 리스트로 취급)
#리스트는 아무것도 포함하지 않는 비어있는 리스트도 가능
#리스트는 숫자, 문자, 숫자와 문자 혼합, 리스트자체를 가질 수도 있다. = 리스트는 어떠한 자료형도 포함할 수 있다.
listx=[] #변수 생성 방식으로 리스트 생성
listy=list() #list함수를 통해 빈 리스트 생성
print(listy)

#리스트의 인덱싱과 슬라이싱
a=[1,2,"hello","python"]
print(a)
print(type(a)) #괄호 안에 있는 데이터가 무엇인지(어떤유형인지)를 리턴해준다.
print(type(a[0])) #결괏값으로 도출된 int는 '정수'라는 뜻
fir=a[0]
sec=a[1]
print(fir+sec) #원본 데이터의 숫자가 유지됨을 여기서도 알 수 있다.
fir=a[2]
sec=a[3]
print(fir+sec) #원본 데이터의 숫자가 유지됨을 여기서도 알 수 있다.
#숫자는 숫자끼리, 문자는 문자끼리만 연산할 수 있다 (숫자와 문자를 혼합해서 연산하는 것은 불가능하다.)
print(a[-1])
b=[1,2,3,['a','b','c']] #요소4개 / 숫자,숫자,숫자,리스트
print(b[3]) #리스트요소도 하나의 데이터로 취급됨을 알 수 있음
print(b[3][0])
print(type(b[3][0])) #결괏값으로 도출된 str은 '문자열'이라는 뜻
print(list5[2][2][2])

listx=[1,2,[4,5],[6,[7,8,[9]]],0]
print(listx)
print(len(listx)) #길이 = 요소의 갯수
print(listx[3][1][2])

#리스트의 슬라이싱
a=[1,2,3,4,5]
print(a[0:2]) #0부터 2미만까지 #문자열 슬라이싱 방법이랑 완전히 동일하다.

#중첩된 리스트에서 슬라이싱
a=[1,2,3,['a','b','c'],4,5]
print(a[2:5]) #리스트를 짤랐을때 안에 있던 요솟값 리스트 결과물은 그대로 리스트로 나온다.
print(a[3][:2]) #인덱싱과 슬라이싱을 혼합해서 쓸 수 있다.

#리스트연산
#1.리스트의 덧셈
a=[1,2,3,4]
b=[5,6,7,8]
print(a+b)
#2.리스트의 곱셈
print(a*3)

#len함수는 문자열, 리스트에 사용가능
#튜플 딕셔너리 데이터 형태에도 사용이 가능

#리스트는 그 안에서 값을 수정하거나 삭제할 수 있다.
listx=[1,2,3]
listx[0]=10
print(listx)
listx=[1,2,3]
del listx[:2] #del같이 주황색 함수들은 무언가의 역할을 가지고 있는 예약어이기 때문에 ()를 안해도 된다.(일종의 규칙)
print(listx)

#리스트 관련 함수들
#append : 리스트에 요소 추가
#.append(x)는 리스트의 맨마지막에 x를 요소로 추가한다.
a=[1,2,3]
b=[4,5,6]
a.append(b)
print(a) #append 함수는 원본데이터에 영향을 끼치는 함수이다.
#sort: 리스트 정렬 (리스트를 순서대로 정렬한다)
a=[1,3,7,2,4,5]
a.sort()
print(a)
a=['z','c','a']
a.sort()
print(a)
#reserse : 리스트 뒤집기
a=['a','c','b']
a.reverse()
print(a)
#index : 위치 변환
#index(x)함수는 리스트에 x값이 없으면 x의 위치를 반환한다.
a=[1,2,3]
print(a.index(3)) #찾아서 인덱스번호 리턴해줌 # #print(a.index(5) 같이 없는 요소는 요류가 발생하므로 주의
#insert : 리스트에 요소 삽입
#insert(a,b)는 리스트의 a번째 위치에 b를 삽입한다.
#a번째는 0부터 시작한다.
a=[1,2,3]
a.insert(0,4)
print(a)
#remove : 리스트 요소 제거
#remove(x)는 리스트에서 첫번째로 나오는 x를 삭제하는 함수
a=[1,2,3,1,2,3]
a.remove(3)
print(a) #del과 remove의 차이? del 함수는 위치를 근거로 삭제하고 remove는 값을 근거로 삭제한다. (삭제이기에 둘다 원본에 영향을 끼침)
#pop : 리스트요소 빼내기
#pop()은 리스트의 맨마지막 요소를 반환하고 그 요소는 삭제된다.
a=[1,2,3]
x=a.pop() #a의 마지막 요소롤 x에 반환(저장)했다는 뜻
print(x)
print(a)
a=[1,2,3]
x=a.pop(1) #값을 지정해준다면 맨마지막 요소 대신 지정한 요소를 반환하는것도 가능하다.
print(x)
print(a)
#count : 리스트에 포함된 요소 x의 개수 세기
a=[1,2,3,1]
print(a.count(1))
#extend : 리스트의 확장
#extend(x)에서 x에는 리스트만 올 수 있다. 원래의 리스트에 x리스트를 더한다.
a=[1,2,3]
a.extend([4,5])
print(a)
b=[1,2,3]
c=[4,5]
print(b+c) #extend함수는 단순 두개의 리스트를 더한것과 같은 값을 도출한다.

#문자열 슬라이싱 다른 방법
string1="121212121212"
print(string1[::2]) #처음부터 2칸씩 뛰어넘은 수만 추출해라 라는 뜻
#슬라이싱 각 칸의 의미 [시작인덱스, 끝인덱스, 오프셋]

#불자료형 : 참과 거짓을 나타냄
#True or Flase
#1 or 0
#bool()

#불 자료형은 2가지 값만 가질 수 있다. (대표형태 : 숫자형(int), 문자형(str), 리스트형(list), 불자료형(bool))
a=[1,2,3] #많은 조합
a="123" #많은 조합
a=123 #많은 조합
a=True #2가지 (True or False) #꼭 첫글자를 '대문자'로 써야 한다.
print(type(a))

if(1==1): #1과 1이 같은 값인가? (조건식)
    print("1은1이다")
print(1==2)

#비교 연산자
# < 작다
# > 크다
# <= 작거다 같다
# >= 크거나 같다
# == 같다
# != 같거나 같지않다

#내용물이 있고없음에 따라 참, 거짓이 나뉜다.
a=[1,2,3]
print(bool(a))
a=[]
print(bool(a))
a="helllo"
print(bool(a))
a=""
print(bool(a))
a=1
print(bool(a))
a=0
print(bool(a))
print(bool(""))
print(bool("11111"))
print(bool(None)) # None : 아무것도 없다 라는 뜻->False값 나옴

#변수
#변수이름 = 변수에 저장할 값
#C언어나 JAVA에서는 변수를 만들 때, 자료형을 직접 지정해야 한다. ex)int x=10;
#파이썬은 그럴필요가 없어 편리하다.
#변수란? 파이썬에서 사용하는 변수는 객체를 가리키는 것이라고도 말할 수 있다.
#객체란 우리가 지금껏 본 자료형과 같은 것을 의미한다.

a=[1,2,3]
print(id(a))
b=a
print(b)
print(id(b)) #a와 b의 id넘버가 같음->a와 b의 대상이 동일하다.
print(a is b) #is : a가 가리키는 객체와 b가 가리키는 객체가 같은지 물어보는 것, is는 ==로 바꿔쓸 수도 있다.
print(a == b)
a[1]=100
print(a)
print(b) #a의 값을 바꿨는데 b도 바뀐이유? a를 b에 부여했기 때문 (둘은 동일시됨)

#a변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 하는 방법
a=[1,2,3]
b=a[:]
a[1]=1000
print(a)
print(b) #a의 값이 바뀐것에 비해 b는 바뀌지 않았다.

#copy 모듈 사용
#모듈 : 어떤 기능을 쓸 수 있는 집단단위 (이러한 모듈들의 모임->라이브러리)
from copy import copy
a=[1,2,3]
b=copy(a)
print(b)
#copy 모듈 copy함수 사용은 b=a[:]와 동일
print(a is b)

listx=[333,444,555]
print(max(listx))
print(min(listx))
print(sum(listx))

#수학 영어 국어 과학
#학생 3명의 수학점수 평균을 구하시오.
#학생 2의 총 평균을 구하시오.
#문자열 포매팅을 통해 '학생3명의 수학점수 평균은 xx.xx입니다.'
list_stu1=[82,67,95,100]
list_stu2=[88,66,90,45]
list_stu3=[90,70,75,77]
print((list_stu1[0]+list_stu2[0]+list_stu3[0])/3)
print(sum(list_stu2)/len(list_stu2))
list_math=(list_stu1[0]+list_stu2[0]+list_stu3[0])/3
print("학생3명의 수학점수 평균은 %0.2f입니다." % list_math)

#if문은 무엇인가? -> 만약, 조건식
money=True
if money: #여기서 콜론뒤에서 엔터를 칠경우 들여쓰기(스페이스4번 Tab1번 기준)가 됨
    print("택시를 타라")
else: #'그렇지 않으면'이라는 뜻
    print("걸어가라")
#비가오면 우비, 눈이오면 버스타라 날씨가 좋으면 걸어가라
# 비가오는 날=R, 눈이오는 날=S, 날씨좋은 날=N
wt="R"
if wt=="R":
    print("우비") #이러한 문장을 '수행문'이라 한다. 수행문은 여러개 올 수 있다.
    print("를 입어라")
elif wt=="S":
    print("버스") #만약 아무것도 실행하고 싶지 않다면 print말고 pass를 써라
    print("를 타라")
elif wt=="N":
    print("걸어")
    print("가라")
else: # tip: else는 내가 미처 생각하지 못한 항목이 있을 수 있으니 항상 남겨두고 내가 생각한 항목은 elif에 몰아넣을 것!
    print("예외")
#if문의 구조
#if 조건식:
#   수행할 문장1
#   수행할 문장2
#else:
#   수행할 문장1
#   수헹힐 문장2
#if문은 하나/if는 무조건 있어야함
#elif는 제한없음/없어도됨
#else는 하나/없어도됨

money=5000
if money:
    print("if 조건식 True로 진입하여 수행문 실행")
else:
    print("돈이 5000원이 아닌 경우 실행문")

#수학 영어 국어 과학
#if조건을 활용하여 학생의 4과목 평균이 90이상이면 A등급, 80이상이면 B등급, 70이상이면 C등급
stu1=[80,55,78,90]
stu2=[90,80,85,92]
avg1=sum(stu1)/len(stu1)
avg2=sum(stu2)/len(stu2)
stu=avg2
if stu>=90:
    print("A등급")
elif stu>=80:
    print("B등급")
elif stu>=70:
    print("C등급")
else:
    print("D등급 이하") #if부터 else까지는 한세트이다. 이 개념을 잘 기억할 것

money=5000 #이렇게 if문에서 처음 시작하는 부분의 변수를 '전역변수'라 한다.
if money: #1세대
    print("돈이 있다.") #2세대
    if money>=5000:
        print("5000원 이상이다.") #3세대

#평균 90이상 A, 80이상 B, 70이상 C, 60이상 D, 60미만 F
# 과목의 점수가 60점 미만이 하나라도 있으면 F
x1=[95,80,90,60]
avg=sum(x1)/len(x1)
if x1[0]<60 or x1[1]<60 or x1[2]<60 or x1[3]<60:
    print("F")
else:
    if avg>=90:
        print("A")
    elif avg>=80:
        print("B")
    elif avg>=70:
        print("C")
    elif avg>=60:
        print("D")
    elif avg<60:
        print("F")

#and 연산자
#A and B
#조건 A와 조건 B가 모두 참이면 참을 반환
#즉, 조건 A와 조건 B중 하나라도 거짓이면 거짓 반환
#True and True => True
#True and False => False
#False and False => False

#or 연산자
#A or B // A조건식이 참이거나 B조건식이 참이면
#조건 A와 조건 B중 하나라도 참이면 참을 반환
#True or True => True
#True or False => True
#False or True => True
#False or False => False

a=[1,2,3,4]
if 1 in a:
    print("1이 포함되어 있다.")

#if문을 한줄로 작성하는 방법
if 1 in a:
    print("1")
#위아래는 같은것이지만 정석은 위에것이다.
if 1 in a: pass
else: print("없다")

#조건부 표현식 : 조건문이 참인 경우 => "수행문 if 조건식 else 거짓인 경우 수행문"(사용하지 말것)
score=60
if score>=60:
    msg="success"
else:
    msg="fail"
print(msg)
#위에것이 아래것으로 표현된것 같은 뜻임(조건부 표현식) 그러나 가급적이면 정석을 추구할것
msg="suc" if score>=60 else "fail"
print(msg)