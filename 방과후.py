'''
twiceDict = {'이름': '트와이스', '구성원수': 9, '데뷰': '서바이벌 식스틴', '대표곡': 'cry for me'}
print(twiceDict)
for k in twiceDict.keys():
    print(k, " ==>", twiceDict[k])'''
'''
store = {}
while True:
    item = input('입력 물품 ==>')
    if item == 'z':
        break
    count = int(input("worhfid ==>"))
    store[item] = count
    
while True:
    item = input("찾을 물품 ==>")
    if item == "":
        break
    if item in store:
        print(store[item], "개 남음")
    else:
        print("물품 없음")
'''
'''
import random
seq = ('가위', '바위', '보')
x = random.choice(seq)
print('무엇을 낼껀가요?')
y = input()
print(x)
if y == '가위':
    if x == '가위':
        print('비김')
    if x == '바위':
        print('패배')
    if x == '보':
        print('승리')
if y == '바위':
    if x == '가위':
        print('이김')
    if x == '바위':
        print('비김')
    if x == '보':
        print('패배')
if y == '보':
    if x == '가위':
        print('패배')
    if x == '바위':
        print('승리')
    if x == '보':
        print('비김')
'''
'''
i = 0
fact = 1
friends_num = input()
for i in range(1, int(friends_num) + 1, 1):
    fact = fact * i
print(fact)
'''
'''
hap = 0

for i in range(1,101,1):
    if i % 4 == 0 or i % 7 == 0:
        continue
    hap += i

print(hap)
'''
'''
import random
s = 0
while True:
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    s = s + 1
    print(s)
    if a == b == c:
        break
'''
'''
import random

a = random.randint(1,5)
for x in range(0,5,1):
    y = input()
    if int(y) == a:
        print('correct')
        break
    else:
        print('wrong')
'''
'''
def hap():
    num1 = int(input("정수 1 ==>"))
    num2 = int(input("정수 3 ==>"))
    return num1 + num2
print("A님. 두 숫자를 입력하세요")
hap_s = hap()
print(hap_s)
'''
'''
coffee = 0

coffee = int(input("어떤 커피를 드릴까요?(1:보통,2:설탕,3:블랙"))

for x in range(0, 10, 1):
    print("이름을 입력해주세요")
    y = input()
    print(y, "님 어떤 커피를 드릴까요?")
    z = input()
    if z  == '':
        print('뜨거운 물을 준비한다')
        print('종이컵을 준비한다')
        print('물을 붓는다')
        print('스푼으로 젓는다')
        print(y, '님 주문하신', z, '여기 있습니다.')
'''
'''
inFp = None
inStr = ""


inFp = open("C:\\Users\\ginok\\OneDrive\\바탕 화면\\talking about nothing.txt", "r", encoding = "UTF-8")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()
'''
'''
inFp = None
inStr = ""


inFp = open("C:\\Users\\ginok\\OneDrive\\바탕 화면\ \talking about nothing.txt", "r")

#for x in range(): , or while True
for x in range(3):
    inStr = inFp.readline()
    print(inStr, end="")

    inStr = inFp.readline()
    print(inStr, end="")

    inStr = inFp.readline()
    print(inStr, end="")

    inFp.close()'''
'''
inFp = None
inList = []

inFp = open("C:\\Users\\ginok\\OneDrive\\바탕 화면\\talking about nothing.txt", "r")

inList = inFp.redlines()
print(inList)
inFp.close()'''

'''
inFp = None
instr = ""
lineNum = 1

inFp = open("C:\\Users\\ginok\\OneDrive\\바탕 화면\\talking about nothing.txt", "r", encoding = "UTF-8")

while True:
    inStr = inFp.readline()
    if inStr == "":
       break
    print(lineNum, ":", inStr, end = "")
    lineNum +=1
inFp.close()
'''

'''
outFile = None
outStr = ""

outFile = open("C:\\Users\\ginok\\OneDrive\\바탕 화면\\talking about nothing.txt", "w")

outStr = "안녕하세요"
outFile.writelines(outStr + "\n")

outStr = "반갑습니다"
outFile.writelines(outStr + "\n")

outStr = "자주만나요"
outFile.writelines(outStr + "\n")

outFile.close()
print("----talking about nothing.txt. 파일이 저장됨")
'''
'''
outFp = None
outstr = ""

outFp = open("C:\\Users\\ginok\\OneDrive\\바탕 화면\\talking about nothing.txt", "w")
while True:
    outstr = input("sodyddlqfur:")
    if outstr != "":
        outFp.writelines(outstr+"\n")
    else:
        break
outFp.close()
'''
'''
infile, outfile = None, None
inStr = ""
inFile = open( ,"r") #파일 지정
outfile = open( ,"r") #파일 지정

inList = infile.readlines()
for inStr in inList:
    outfile.wrielines(inStr)
inFile.close()
outfile.close()
print("---xx노트가 xy로 복사됨")
'''
'''
import turtle
import random
## 클래스 선언부
class Rabbit:
    myTurtle = None
    def __init__(self, kmyTut):
        self.myTurtle = kmyTut
        print("**토끼까 거북이 등에 올라탔습니다.**")
    def print_my_position(self):
        print("거북이 등 위의 토끼 위치는 현재", self.myTurtle.xcor(), ",", self.myTurtle.ycor(),"입니다")
#전역변수 선언부
myTut, myRab = None, None
colorList = ["red", "green", "blue", "black", "magenta", "orange", "gray"]

#메인 코드부
turtle.setup(550, 550)
turtle.screensize(500, 500)

myTut = turtle.Turtle("turtle")
myRab = Rabbit(myTut)
myTut.pensize(5)

for _ in range(20):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    color = random.choice(colorList)
    myTut.pencolor(color)
    myTut.goto(x, y)
    myRab.print_my_position()

turtle.done()'''

import openpyxl
import pandas


exel_file = openpyxl.load_workbook(r"C:\Users\ginok\Downloads\data_set_for_school_porject.xlsx")
selected_sheet = exel_file.active
print(selected_sheet)