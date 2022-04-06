#모듈
#함수나 변수 또는 클래스를 모아 놓은 파일이다.
#다른 사용자에게 배포가 가능하다.
def add(a,b):
    return a+b

def sub(a,b):
    return a+b

#모듈 불러오기 방법:import
#import 모듈명(파일명)

import mod1
mod1.printX()

print(mod1.mod1X)

#모듈 내부의 함수나 변수 사용방법: 모듈이름.모듈내부함수명 or 모듈이름.모듈내부변수명

from mod1 import * #mod1모듈에서 전부다 가져오겠다.

printX() #'from 모듈명 import 함수명'으로 가져왔기 때문에 바로 사용 가능
printY()
print(mod1X) #가져오지 않은 변수는 사용 불가능 #*을 찍었을 시에는 사용가능
print(__name__)