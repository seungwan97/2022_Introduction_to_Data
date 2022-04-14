

file=open("220414_sample.txt", 'r', encoding='UTF-8')
file=file.readlines()

class stu:
    def __init__(self,name,gen,score,mbti):
        self.n=name
        self.g=gen
        self.s=score
        self.m=mbti

totalStu=int(input("총 인원 몇?"))
member=int(input("멤버수 설정"))
ex=0
count=0
scoresum=0
teamList = []
scoreList=[]
mbtiList=[]
#totalStu//member 몫:팀의 수
#totalStu%member 나머지:깍두기 수
import random as rd
while True:
    strtemp=[]
    teamList = []
    scoreList = []
    count+=1
    if (totalStu % member) == 0:
        pass
    else:
        print("깍두기",totalStu%member,'명')
        ex=totalStu%member #깍두기 몇명인지 확인
    team=totalStu//member
    listData=[]
    for i in range(len(file)):
        file[i].replace('\n','')
        listData.append(file[i].split("\t"))
    listData=listData[1:]
    print(listData)
    stuList=[]
    for i in range(len(listData)):
        stuList.append(stu(listData[0][0],listData[0][1],listData[0][2],listData[0][3]))
    print(stuList)
    rd.shuffle(stuList)
    print(stuList)
    for i in range(team):
        tempList=[]
        scoresum=0
        for x in range(member):
            tempList.append(stuList[i*member+x].n)
            scoresum+=int(stuList[i * member + x].s)
            strtemp=stuList[i * member + x].m
            if strtemp=='EEE' or strtemp=="III":
                print(strtemp)
                continue

        teamList.append(tempList)
        scoreList.append(scoresum)
        mbtiList.append(strtemp)

    print(teamList)
    print(scoreList)
    print(mbtiList)

    if 'E'*member in mbtiList or 'I'*member in mbtiList:
        continue

    if max(scoreList)-min(scoreList)<=10:
        for i in range(len(teamList)):
            print("%s"%i,teamList[i])
        for i in range(len(scoreList)):
            print(scoreList[i])

        print(count)
        print(strtemp)
        if ex>0:
            while ex:
                ex-=1
                print("깍두기",stuList[totalStu-ex-1].n)
        break