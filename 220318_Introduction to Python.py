#while문은 반복문

x=10
if x==10:
    print(123)

#while 조건식:
#     수행문1
#     수행문2
#     수행문3
#     ....

#무한으로 실행되는 while세트를 무한루프라고 한다.

x=10
while x>0:
    print("안녕하세요")
    print("123123")
    x=x-1

treehit=0
while treehit<10:
    treehit=treehit+1
    print("나무를 %d번 찍었다." % treehit)
    if treehit==10:
        print("나무 넘어갑니다.")

shoot=24
while shoot>0:
    print("선방")
    shoot=shoot-1
    if shoot==0:
        print("골")

onoff=1
count=0
while onoff==1: #!= : 같지않다
    count=count+1
    x=int(input("답 입력:")) #while 안에 input을 쓰면 맞는 답이 아닐시 계속 질문을 한다.
    if x==10:
        print("%s번째에 정답 맞춤" % count)
        onoff=0
    else:
        print("다시")

a=[1,2,3]#true
b=[]#false
x=3
while b:
    print("123123123") #만약 작동시키고자한다면 append등의 함수를 이용해서 데이터를 수정해야한다.

while a:
    print("123123123")
    break #break:반복문을 종료하고 탈출한다.

while a:
    print("123123123")
    x=x-1
    if x==0:
        break #while문을 3번만들고 종료한다.


