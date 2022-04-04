file_c=open('근로소득세.txt','r',encoding='UTF-8')
list_all=file_c.readlines()
print(list_all)


salary=float(input("세전연봉:"))
notax=float(input("비과세액:"))
family=int(input("부양가족수(본인포함):"))


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
   print(dic)
   krsds=dic[1][y-1]
   return krsds

result=sepList(salary,family)
print(result)

raw=open('ㅇㅁ.txt','r',encoding='UTF-8')
rawdata=raw.readlines()
print(rawdata)
lista=[]
for i in range(len(rawdata)):
    rawdata[i]=rawdata[i].split('\t')
print(rawdata)
def changeX(x,y=''):
    for i in range(len(rawdata)):
        for i in range(len(rawdata[i])):
            if x in rawdata[i][j]:
                rawdata[i][j]=rawdata[i][j].replace(x,y)
changeX('\n')
print(rawdata)