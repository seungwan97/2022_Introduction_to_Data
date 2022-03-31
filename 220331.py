
#파일 읽고 쓰기

#open()함수에서 인스로 쓰이는 w
#1. r : 읽기모드 - 파일을 읽기만 할때
#2. w : 쓰기모드 - 파일에 내용을 쓸때
#3. a : 추가모드 - 파일의 마지막에 새로운 내용을 추가할때

fileX=open("문서.txt",'w',encoding='UTF-8') #파일 생성 (쓰기(w:write))
for i in range(1,100): #파일에 데이터 추가 (write)
    data="%d번째 줄.\n" %i
    fileX.write(data)
fileX.close() #파일객체를 닫는다.

# 방금 쓰기모드로 생성한 문서에 있는 파일 읽어오기
fileX=open("문서.txt",'r',encoding='UTF-8')
line=fileX.readline() #readline() 함수를 사용하면 파일의 첫번째줄이 읽힘
print(line)
fileX.close()

#문서의 모든 줄을 가져오는 방법
#1번째방법 (잘안씀)
fileX=open("문서.txt",'r',encoding='UTF-8')
while True:
    line = fileX.readline()
    if not line:
        print("더 이상 읽을 줄 없음")
        break
    print(line)
fileX.close()

#2번째방법 (후처리를 해줄때, 가장 많이 쓰는 방법)
#readlines 함수
fileX=open("문서.txt",'r',encoding='UTF-8')
lines=fileX.readlines() #readlines() : 파일의 모든 내용을 리스트 형태로 가져온다.
print(lines)
for line in lines:
    print(line)
fileX.close()

#3번째방법 (전부다 그냥 출력해 줄때)
fileX=open("문서.txt",'r',encoding='UTF-8')
data=fileX.read() #문서 전체 내용을 가져온다. 단, str형태로 반환한다.
print(type(data))
fileX.close()

fileX=open("문서.txt",'a',encoding='UTF-8') #a모드(추가모드)는 마지막줄에서 시작한다.
for i in range(100,200):
    data="%s번째 줄. \n" % i
    fileX.write(data)
fileX.close()

#with문과 함께 사용하기 (일종의 줄임말로 사용하는 다른방식 중 하나)
with open("문서.txt",'w',encoding='UTF-8') as fileX:
    fileX.write("with문으로 w모드에서 작성한 파일 fileX")
#with as 방식으로 파일을 open하면 따로 close없어도 with문 아래 수행문으로 작성되어 있는 코드가 전부 읽힐시~
#~자동으로 파일 객체가 close된다.

fileX=open("새파일.txt",'r',encoding='UTF-8')
lines=fileX.readlines()
print(lines)
del lines[2:5]
del lines[3]
del lines[8:11]
for line in lines:
    print(line)
fileX.close()

fileX=open("새파일.txt",'r',encoding='UTF-8')
lines=fileX.readlines()
for line in lines:
    if '.' in line:
        del line
    else:
        continue
print(line)
fileX.close()
