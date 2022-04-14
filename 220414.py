#예외 오류 처리 방법
#try except
#오류가 발생했을 때 프로그램이 종료되는 것을 막고
#오류의 종류에 따른 코드를 실행하는 방법

#오류의 종류
#ValueError
#KeyError
#IndexError
#ZeroDivisionError
#FileNotFoundError
#TypeError


try:
    file =open('1234.txt','r',encoding='UTF-8')
    print(4/0)
except ZeroDivisionError as e: #except뒤에 오류명을 부여하면 그 에러일때만 해당 코드를 수행하라는 뜻(일종의 조건문)
#해당 조건의 에러가 아닐시에는 try의 하위 수행문일지라도 오류가 뜸
    print("0으로 나누기 불가")
#try 안의 수행문이 수행되지 않을지라도 그저 시도만 한다는 개념으로, 다음 코드들은 그대로 작동함
#try 안의 수행문이 몇개이건 한개라도 오류일 경우에는 다음으로 넘어간다.
except FileNotFoundError:
    print("파일이 존재하지 않는다.")
    #except문이 몇개이건 try문의 맨처음 코드를 읽고 그에 따른 except문 만을 출력한다.(다른 except문은 출력되지 않는다.)

try:
    print(4 / 0)
    a=[1,2]
    print(a[3])
except (ZeroDivisionError, IndexError) as e: #except문을 여러개 쓰지 않고 합쳐쓰는 방법
    #여러개 쓰는 것과 결과는 동일하게 try문의 맨 위 수행문에 해당되는 것만 출력됨
    print(e)

try:
    x=int(input("숫자 입력"))
except: #try에서 문제가 있으면 진입
    print("숫자가 아닌듯")
else: #try에서 문제가 없으면 진입
    print("else진입")



#번호 4자리 입력상황
#사용자가 숫자만 잘 입력하는 경우 =>통과
#숫자형태가 아닌 문자를 입력하는 경우 =>다시 번호 4자리 입력하도록 반복
while True:
    try:
        x = int(input("숫자 4자리 입력:"))
        if len(str(x))==4:
            pass
        else:
            print("4자리 숫자가 아닙니다.")
            continue
    except :
        print("4자리 숫자형태가 아닙니다. 다시 4자리의 번호를 입력해주세요.")
        continue
    else:
        print("통과")
        #break를 쓰지 않는 이유: 하위에 코드가 있을시 이를 구동시키기 위함
    print("하위문장")
    break

class MyError(Exception):#나만의 오류 상황 및 오류 이름 정의
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(n):
    if n =='바보':
        raise MyError() #에러를 발생시킨다. raise
    print(n)

try:
    say_nick('바보')
except MyError as e: #오류로 정의한 class 안의 return 값을 받아서 출력
    print(e)