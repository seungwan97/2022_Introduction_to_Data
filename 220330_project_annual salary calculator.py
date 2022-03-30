#연봉계산기
#비과세액, 1년 연봉을 입력하여
#1. 연간 세후 수령금액 표기 : 세전연봉-(각종 과세항목 합*12)
#2. 월 세전 금액 표기 : 세전연봉/12
#3. 월 세후 금액 표기 : 세후연봉/12
#4. 연간 세금 납부액 표기 : 각종과세항목 합*12
#5. 월 세금 납부액 표기 : 각종과세항목 합
#6. 각 세금 항목별 액수 표기
#7. 함수로 만들기
#근로소득세는 50000원 고정 반영
#각종 과세항목 :비과세액x2에 세율반영된 금액
#세후연봉: 세전연봉-(각종 과세항목 합*12)
#세전월급: 세전연봉/12
#세후월급: 세후연봉/12
#연 세금 납부액



salary=float(input("세전연봉:"))
notax=float(input("비과세액:"))
notax2=notax*2
kmyk=notax2*0.045
kkbh=notax2*0.03495
yybh=kkbh*0.1227
kybh=notax2*0.008
krsds=50000
jbsds=5000
def realsalary(x,y):
   p1=x-((kmyk+kkbh+yybh+kybh+krsds+jbsds)*12) #1. 연간 세후 수령금액
   p2=x/12 #2. 월 세전 금액
   p3= p1/12 #3. 월 세후 금액
   p4=(kmyk+kkbh+yybh+kybh+krsds+jbsds)*12 #4. 연간 세금 납부액
   p5=(kmyk+kkbh+yybh+kybh+krsds+jbsds) #5. 월 세금 납부액
   p6=kmyk #6. 국민연금
   p7=kkbh #7. 건강보험
   p8=yybh #8. 요양보험
   p9=kybh #9. 고용보험
   p10=krsds #10. 근로소득세
   p11=jbsds #11. 지방소득세
   return p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11
rs=realsalary(salary,notax)
print("연간 세후 수령금액: %d원" % rs[0])
print("월 세전금액: %d원" % rs[1])
print("월 세후금액: %d원" % rs[2])
print("연간 세금 납부액: %d원" % rs[3])
print("월 세금 납부액: %d원" % rs[4])
print("각 세금 항목별 액수")
print("국민연금: %d원" % rs[5])
print("건강보험: %d원" % rs[6])
print("요양보험: %d원" % rs[7])
print("고용보험: %d원" % rs[8])
print("근로소득세: %d원" % rs[9])
print("지방소득세: %d원" % rs[10])
