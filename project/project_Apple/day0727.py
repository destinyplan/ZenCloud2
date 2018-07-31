# a=[8,3,6,9,1,6,2,8,6,4,3,9]
# a.insert(1,'asdasd')
# b=a.pop()
# # c=x in y
# a.append()
# a.remove(5)

# 1
# a.reverse()
# a.remove(5)
# 2
# e = a[::-1]
# e.remove(5)
# print(e)

# g = a[len(a)-1]
# print(g)

# h = a.sort(key=1,reverse=True)
# print(a)
# print(h)

# a=[8,3,6,9,1,6,2,8,6,4,3,9]
# # b = a
# # c = a.copy()
# # a[3]=123
# # print(a[3])
# # print(b[3])
# # print(c[3])

# # b=['a','b','c']
# # c=[[1,2,3],[4,5,6],[7,8,9]]
# # print(c[1][1])
# # # a.append(b)
# # a.extend(c)
# # print(a)
# # a.extend([1,2,3,4,5])
# # print(a)

# a=(1,2,3,4,5,6)
# b=a[2]
# # a[2]=56

# print(a.index(3))


# person2=('male','famale','mid')
# person1=['male','famale','mid']
# # xiaocai.sex=person2[0]

# print(type(2.2))
# print(type(2))
# print(type('asfd'))
# print(type(person2))
# print(type(person1))

str01='ABCDef213欢子ghi213jkle213m21er'
str02='*&^%$#@WSC132'
str03='12'
str041='0x13'
# print(len(str01))
# print(max(str01))
# print('Bjk' in str01)
# print(str01*3)
# print(str01+str02)
# print(str01[1])

# ss = str01.capitalize()
# s1 = str01.upper()
# s2 = str01.lower()
str04 = str01.casefold()
str05 = str02.center(10,'*')
num = str01.count('213',7,len(str01)-1)
flag = str01.endswith('C',0,3)
str06 = str02.expandtabs(20)
index = str01.find('21x3')
str07="we are{},%{},={}"
str08 = str07.format(1,2,3)
#str01.index()
isA = str01.isalnum()
isB = str02.isalnum()
isC = str03.isdecimal()
isD = str041.isdecimal()
isF = '123.4'.isdigit()
isG = "123".isidentifier()
isH = "for".isidentifier()
isI = "1".isnumeric()
isJ = "a".isprintable()
isK = " The  Big News ".istitle()
strL = "   ABCD *B*C  i   "
strM = strL.join("ABCDEFG")
strN = strL.ljust(10,' ')
strO = strL.lstrip()#strO = strL.lstrip(['*',"A"])
tupleA = strL.partition('BC')
#strL.replace
strP = strL.replace("BC","TYUIO")
num3 = strL.rfind('BC')
listL = strL.split(sep=" ")
strL1 = "ABCD *B*C  i\nsdfdsf\n asfdsa\nwf"
listL1 = strL1.splitlines()
flags = strL.startswith("ABC")
strLLLL = strL.strip()
strLLLL = strL.swapcase()
strKKK = strL.zfill()
# '''
# 优化
# '''

# # 1.
# import math

# # num=int(input("num="))
# # pnum =int(input("power="))
# # print(math.pow(num,pnum))

# # 2.
# strInput1 = input("please input num:")
# strInput2 = input("please input power:")
# isNum1 = strInput1.isdigit()
# isNum2 = strInput2.isdigit()
# if isNum1 and isNum2:
#     print(math.pow(int(strInput1),int(strInput2)))
# else:
#     print('您输入的不是数字，醒醒吧愚蠢的人类')

