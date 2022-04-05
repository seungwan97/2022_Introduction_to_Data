import os.path #path경로를 가져오기 위한 모듈
path="220405_project_mcdonalds kiosk.py"
print(os.path.isfile(path)) #path변수에 저장되어 있는 파일이 존재하는지 여부
#True/False로 리턴
#파일이 존재하는지를 물어봐야 하기 때문에 위 세줄을 써야함 : 키오스크를 예로 들면 완전 그 기계의 첫손님인지 아닌지 판별하기 위해
#가장 윗줄에 써야함

#1.파일의 생성 => 파일 존재 유무에 따라서 프로그램의 가장 처음
#2.파일의 저장 => 실제로 결제가 되고 나서 재고가 실제로 감소 했을 때에만 그 즉시 저장이 되어야함
#3.파일의 불러오기 =>프로그램의 가장 처음
#1,2,3번 전부 함수로 만들어야함


#==================================================================================
stock=100
if os.path.isfile(path):
    pass #불러오기
else:
    pass #첫 생성
while True:
    if '예'==input("예/아니오"):
        stock-=1
        #저장
    else:
        print(stock)
        pass





"""
stra="123"
stra.isdigit()

raw=open("220405_project_mcdonalds kiosk.py",'r',encoding='UTF-8')
rawdata=raw.readlines()

print(rawdata)
"""