#파이썬 기본 내장함수 목록

#파이썬 내장 함수는 외부 모듈 import를 하지 않고도 사용이 가능한 함수

#abs()
#절대값을 반환한다.
print(abs(-3))

#all()
#all(x)는 반복 가능한 자료형 x(ex.리스트형)를 입력 인수로 받아서
#이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False
print(all([1,2,3]))
print(all([1,2,3,0]))
print(all([1,2,'']))
print(all([])) #빈리스트도 True가 나옴 #아예 체크할 요소항목 자체가 없기 때문에

#any(x)
#반복 가능한 자료형 x를 인수로
#x의 요소중 하나라도 참이 있으면 True, 모두 거짓일때는 False

#chr()
#유니코드(특정 문자로 바꿔주는 코드표)를 실제 문자로 변환하는 함수
print(chr(97))

#divmod(a,b)
#2개의 숫자를 입력받아 a를 b로 나눈 몫과 나머지를 튜플 형태로 반환한다.(몫과 나머지가 동시에 나온다.)

#enumerate()
#열거함수
#순서가 있는 자료형 (리스트 튜플 문자열)을 입력받아 인덱스 값을 포함하는 enum객체를 반환
print(enumerate(['f','s','t']))
for i,name in enumerate(['f','s','t']):
    print(i+1,name)

#eval()
print(eval(input("계산하려는 숫자, 계산하려는 연산자 입력")))

#filter()
#첫 인수로 함수 이름
#두번째 인수로 함수에 차례로 들어갈 반복 가능한 자료형을 입력
#반복가능한 자료형을 직접 넣어 판단해 조건에 맞는 True값들만 골라주는 함수
def positive(l):
    result=[]
    for i in l:
        if i>0:
            result.append(i)
    return result
print(positive([1,-3,2,0,-5,6]))

def positive2(x):
    return x>0
print(list(filter(positive2,[1,-3,2,0,-5,6]))) #첫번째 인수로는 '함수호출(괄호)'이 아닌 '함수'가 들어간다.

#map()
#첫 변수: 함수이름
#두번째 변수: 반복가능한 자료형
def two(numberlist):
    result=[]
    for number in numberlist:
        result.append(number*2)
    return result
result=two([1,2,3,4])
print(result)

def two2(x):
    return x*2
print(list(map(two2, [1,2,3,4,5,6,7]))) #첫번째 인수로는 '함수호출(괄호)'이 아닌 '함수'가 들어간다.

#max
#min
#sum

#ord() : 문자의 유니코드를 반환
print(ord("하"))

#pow()
print(pow(2,4))
print(2**4)

#round()
#숫자를 입력받아 반올림해주는 함수
#round(number[, ndigits]) #[, ndigits]는 생략할 수 있다.
#[, ndigits]는 ndigits가 있을 수도 있고 없을 수도 있다는 의미이다.
print(round(7.2))
print(round(7.5))
print(round(7.6))
print(round(7.0))
print(round(7.678,2)) #두번째 매개변수의 뜻은 소수점 n째 자리까지 출력함을 나타낸다.

#zip()
#반복가능한 형태의 데이터들을 쌍을 지어서 묶어주는 역할
print(list(zip([1,2,3],[4,5,6])))

