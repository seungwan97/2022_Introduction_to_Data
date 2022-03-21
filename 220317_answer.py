#목적지까지의 거리를 input으로 입력받는다.

ts=60
bs=20
ws=4

tsPerM=ts/60*1000 #택시 스피드 1분당 이동거리
bsPerM=bs/60*1000 #버스 스피드 1분당 이동거리
wsPerM=ws/60*1000 #걷기 스피드 1분당 이동거리

print(tsPerM)
print(bsPerM)
print(wsPerM)

dis=input("목적지까지 거리 입력(단위:m)")
dis=int(dis)

#목적지까지 몇분
tr=int(input("나의 여유 시간:"))
#목적지까지의 거리를 택시로 갈 돈이 있으면 택시 탑승
#아니면 버스 선택
#버스비용도 없으면 도보 선택
money=int(input("돈입력:"))

#택시요금
#기본 요금 3300원 2km동안 3300원 고정
#추가 133미터마다 100원 추가
#목적지까지 거리에 따른 총 요금 계산
#변수 설정부분
over=((dis-2000)//133)*100 #기본료 외 추가요금 변수
print("기본료 제한 추가요금:",over*100)
print("총 택시 요금:",3300+(over*100))
total=3300+over #총 택시 요금 변수
fare_dif=1500-total #택시와 버스 요금차이
con=int(input("1km당 편의성 값:")) #1km당 택시의 편안함을 500원으로 임의 설정
print(con)
conondis=round(con*(dis/1000)) #택시를 타고 이동할때 총 이동거리동안 얼만큼 편한가
#round함수 : 소수점 반올림 처리, 정수형태로 변환
#정수와 정수의 나눗셈 결과는 실수 형태로 반환된다.
#정수와 실수 / 실수와 정수도 마찬가지.

#시간,돈,편의성을 다 돈으로 환산하는데 이때 시간은 '최저시급'으로 판단한다.
time_t=round(dis/tsPerM) #택시로 이동하면 얼마나 걸리는지 : 시간
time_b=round(dis/bsPerM) #버스로 이동하면 얼마나 걸리는지 : 시간
time_w=round(dis/wsPerM) #도보로 이동하면 얼마나 걸리는지 : 시간

tr #나의 여유 시간
tr_taxi=tr-time_t #택시를 탔을 경우 남는 시간
tr_bus=tr-time_b #버스를 탔을 경우 남는 시간
allok=(tr>=time_b) #택시와 버스 모두 여유시간 안에 도착할 경우
timetaxi=tr_bus<0<=tr_taxi #택시를 타면 안늦을 경우
timeover=tr_taxi<0 #택시를 타도 늦는 경우
ret=tr_taxi-tr_bus #택시를 탔을때 남은 시간과 버스를 탔을 때 남은 시간의 차이
#시간의 여유가 있는 경우
#시간이 늦어 택시를 타야할 경우
#택시를 타도 늦는 경우는 "뭘타도 늦는다"라고 출력

time_dif=(time_b-time_t) #버스와 택시 시간차이(단위:분)
m=(9160/60) #최저분급
p1=round(time_dif*m) #버스대신 택시를 타서 아낀 시간을 돈으로 환산
#=>시간,돈,편의성을 돈으로 환산한 값을 다 더한 값이 음수면 손해, 양수면 이득이라는 뜻

print(fare_dif) #택시버스 요금차이
print(conondis) #택시를 타서의 편리함을 돈으로 환산한 것
print(p1) #택시를 타서 아낀 시간을 돈으로 환산한 것

res=fare_dif+conondis+p1 #택시를 타면서 시간,편의성,돈을 다 고려했을 때

#최저시급:9160
#1.2000m 이하더라도 택시를 타고 싶을 경우?
#2.알바생,직장인에 따른 효율성을 구분한 경우 (편리함의 값은 각자의 가치에따라 산정)
#3.가격에 택시 편리함의 값을 산정한경우 (편리함의 값은 최저시급으로 산정)

if total <= money:
    print("택시와 버스 모두 선택 가능.")
    print(res)
    if allok:
        if res >= 0: # 시간,편의,돈 전부 합쳤을 때의 결과가 이득인 경우
            print("여유있으니 택시탈것")
        else:
            print("여유있으니 버스탈것")
    elif timetaxi:
        print("여유없으니 택시탈것")
    elif timeover:
        print("택시를 타도 늦음")
elif total>money and money>=1500:
    print("bus")
    print("택시타기에 부족한 금액:",total-money)
    print("버스 소요시간:",dis/bsPerM)
else:
    print("가진 돈",money,"로는 아무것도 못 탐")
    print("걸어")
    print("도보 소요시간:",dis/wsPerM)

