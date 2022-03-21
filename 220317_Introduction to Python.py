# and or not

# 조건을 판단하기 위해 사용되는 논리 연산
# x or y : x조건과 y조건중 하나만 참이어도 참이다.
# x and y : x조건과 y조건이 모두 참이어야 참이다.
# not x : x가 거짓이면 참이다.

#돈이 3000원 이상 : 택시
#돈이 1000~3000원 미만 : 버스
#돈이 1000원 미만 : 도보
#주머니에 버스티켓이 있으면 돈이 없어도 버스탑승 가능
#주머니에 신용카드가 있으면 돈이 없어도 택시 가능
#택시의 유무를 taxi 변수에 True False로 지정할 것
#input을 통해 주머니에 소지품을 추가하라. pocket은 빈 리스트[]로 시작한다.
#택시가 있다 1, 없다 0
taxi=0 #값을 아무거나 만들어놓긴 해야 그 이후 input 과정을 실행할 수 있음
taxi=input("택시가 있으면 1 없으면 0 입력")
taxi=int(taxi) #문자열을 숫자형,리스트형,불자료형 으로 변환하는 과정:형 변환
print(taxi)
print(type(taxi))
pocket=[]
money=input("주머니에 넣을 금액 임력") #input함수로 입력받은 값을 money에 저장
money=int(money) #money변수에 저장된 문자열을 숫자형으로 변환후 다시 money변수에 저장, 형 변환
pocket.append(money) #윗 줄에서 숫자형으로 변환된 money를 pocket리스트에 append 함수를 사용하여 추가
print(pocket) #pocket리스트를 화면에 출력

if pocket:
    if ((pocket[0]>=3300) or ("credit" in pocket)) and taxi==1:
        print("택시가 있다")
        print("돈이 3000이상이거나 credit이 있어서")
        print("택시")
    elif (pocket[0]>=1000) or ("credit" in pocket) or ("ticket" in pocket):
        print("돈이 1000이상이거나 credit이 있거나 ticket이 있어서")
        print("버스")
    else:
        print("돈이 1000미만이어서")
        print("도보")
else:
    print("주머니가 비어있어서")
    print("도보")
# input : 프로그램이 계속 돌아가고 있는 상태임을 표현하기 위함, 컴퓨터가 사용자가 명령을 주길 대기하는 상태
# x=input("입력:")
# print(x)
# print(type(x)) #input 함수로 입력받은 값은 어떤 형식이든 간에 전부 '문자열'로 저장된다.