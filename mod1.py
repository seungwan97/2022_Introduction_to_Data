def printX():
    print("mod1파일 내부 printX함수 실행")
def printY():
    print("mod1파일 내부 printY함수 실행")
def printXY():
    print("mod1이 현재 내부에서 사용 중")
def printXY2():
    print("mod1이 현재 외부에서 사용 중")

mod1X=10

if __name__=="__main__": #일종의 고정적인 문법 #현재 실행되는 파일이 불러온 것이 아닌 자기 자신의 파일일때만 실행
                         #다른 파일에서는 문법이 아닌 파일명으로 실행된다.
                         #현재 mod1파일이 모듈로 사용되지 않는 경우(나 자신이 실행되는 경우)에는 printXY를 출력해라
    printXY()
else:
    printXY2()

