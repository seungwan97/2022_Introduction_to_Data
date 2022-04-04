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

#중복된것처리 o
#줄바꾼것처리
#'원'처리된거처리
#-를 0으로 바꿔주는것 처리
#마지막 100만원 넘는 항목 띄어쓰기 안되어있는것 처리
file_c=open('근로소득세.txt','r',encoding='UTF-8')
list_all=file_c.readlines()
print(list_all)


salary=float(input("세전연봉:"))
notax=float(input("비과세액:"))
family=int(input("부양가족수(본인포함):"))


notax2=notax*2
kmyk=notax2*0.045
kkbh=notax2*0.03495
yybh=kkbh*0.1227
kybh=notax2*0.008

def sepList(x,y):
   list_1 = []
   list_2 = []
   list_3 = []

   dic={}
   for i in list_all:
      if "," in i:
         list_1.append(i)

   for i in list_1:
      temp = i.replace(',', '').replace('-', '0').replace('원', '').replace('x', '').replace('\n','').rstrip()
      list_2.append(temp)

   for i in list_2:
      list_3.append(i.split('\t'))

   for i in list_3:
      i[2:] = map(int, i[2:])
      dic[int(i[0]) <= x*0.0001 < int(i[1])] = i[2:]

   krsds=dic[1][y-1]
   return krsds

result=sepList(salary,family)
print(result)





def realsalary(x,y,z):
   result = sepList(salary, family)
   p1=x-((kmyk+kkbh+yybh+kybh+result+result*0.1)*12) #1. 연간 세후 수령금액
   p2=x/12 #2. 월 세전 금액
   p3= p1/12 #3. 월 세후 금액
   p4=(kmyk+kkbh+yybh+kybh+result+result*0.1)*12 #4. 연간 세금 납부액
   p5=(kmyk+kkbh+yybh+kybh+result+result*0.1) #5. 월 세금 납부액
   p6=kmyk #6. 국민연금
   p7=kkbh #7. 건강보험
   p8=yybh #8. 요양보험
   p9=kybh #9. 고용보험
   p10=result #10. 근로소득세
   p11=result*0.1 #11. 지방소득세
   return p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11
rs=realsalary(salary,notax,family)



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
