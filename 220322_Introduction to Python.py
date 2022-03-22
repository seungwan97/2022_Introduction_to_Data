#while문은 단순반복
#for문은 while처럼 무작위로 돌리는것이 아닌 특정한 대상에 대해 조회하고 싶다라고 할때

for i in [1,2,3]:
    i=0
    print(i)

listx=["수학","영어","국어","과학"]
lista=[50,70,80,45]
x=0
for i in lista:
    x=x+1
    if i>=50:
        print("%d번째 과목" % x, listx[x-1], "과락아님")
        #1번째 과목 수학은 과락 아니다.
        #2번째 과목 영어는 과락 아니다.
        #3번째 과목 국어는 과락 아니다.
    else:
        print("%d번째 과목" % x, listx[x-1], "과락")
        #4번째 과목 과학은 과락이다.

listx=["수학","영어","국어","과학"]
lista=[50,70,80,45]
x=0
while True:
    if lista[x]>=50:
        print("%d번째 과목" % (x+1), listx[x], "과락아님")
        #1번째 과목 수학은 과락 아니다.
        #2번째 과목 영어는 과락 아니다.
        #3번째 과목 국어는 과락 아니다.
    else:
        print("%d번째 과목" % (x+1), listx[x], "과락")
        #4번째 과목 과학은 과락이다.
    x=x+1
    if len(listx)==x:
        break

#리스트,튜플,문자열 대상으로 반복할 때 : for 사용

marks=[90,25,67,45,80] #누군가의 점수
num=0
for mark in marks: #누군가의 점수를
    break
    num+=1 #카운트 하면서
    if mark<60: #60미만일 경우엔
        continue #계속한다(다시 위로 돌아간다) #for문 continue: 처음으로 돌아간다(다시 위로 돌아간다)
    print("%d번 학생 합격" % num)

#range함수를 생성하는 3가지 방법
a=range(10) #range객체 생성
print(list(a)) #range객체를 리스트 자료형으로 변환해서 출력
b=range(1,20) #start와 end로 range 객체 생성
print(list(b)) #리스트로 변환
c=range(1,20,2) #start와 end, step으로 range 객체 생성 #step은 건너뛰어 출력할 범위를 뜻한다.
print(list(c)) #리스트로 변환

print(1)
print("1")
print(x)
print("123123123","222222")

listxx=[1,3,8,3,3,5,4,3,5,10]
sum=0
for i in listxx:
    sum=sum+i
print(sum)

sum=0
for i in range(30,41):
    sum=sum+i
print(sum)

"""
while True:
    print("113")
    while True:
        print("#333") #333에서 상위 while문이 아닌 하위 while문으로 가기 때문에 113은 한번만 출력되고 333이 무한루프 출력
"""

for i in [1,2,3]:
    print(i)
    for m in [4,5,6]: #여기서는 i가 아닌 다른 변수로 설정해야함
        print(m)

for i in range(1,10):
    for m in range(1,10):
        print(i*m)

for i in [1,2,3]:
    print(i)
    for m in ["가","나","다"]:
        print(m)
        for n in ["a","b","c"]:
            print(n)

for i in range(3,8): #스타트포인트(여기서는 3)는 결과에 포함되지만 엔드포인트(여기서는 8)는 포함되지 않는다.
    print(i)