#优化-五子棋
# while True:
#     mapSize=int(input("size="))
#     fiveMap=[]
#     i=0
#     k=[0]*mapSize
#     while i<mapSize:
#         fiveMap.append(k)
#         i+=1
#     print(fiveMap)
#     for line in fiveMap:
#         for elem in line:
#             print(elem,end=' ')
#         print("")

# 乘法表
#1: 1*1=1
#2: 1*2=2 2*2=4
#3: 1*3=3 2*3=6 3*3=9
# ...
#9: 1*9=9 ...         9*9=81

#0,分析:输出规律为共计九行，每行列数从1开始，直到第九行为9列，每一个输出内容为 行数*列数=结果
# while i<10:
#     while j<i:
#         print(i,'*',j,'=',i*j)

# i=1
# while i<10:
#     j=1
#     while j<=i:
#         print(i,'*',j,'=',i*j,end=' ')
#         j=j+1
#     print('')
#     i=i+1
'''
1 * 1 = 1 
2 * 1 = 2 2 * 2 = 4 
3 * 1 = 3 3 * 2 = 6 3 * 3 = 9 
4 * 1 = 4 4 * 2 = 8 4 * 3 = 12 4 * 4 = 16 
5 * 1 = 5 5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25 
6 * 1 = 6 6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36 
7 * 1 = 7 7 * 2 = 14 7 * 3 = 21 7 * 4 = 28 7 * 5 = 35 7 * 6 = 42 7 * 7 = 49 
8 * 1 = 8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64 
9 * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81
'''
'''
9 * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81
8 * 1 = 8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64 
...
1 * 1 = 1 
'''

# char 'A' cstring "aedrftgyhu"
#string
#str '' ""
str01='1qasw2'
str02 = str01[2]
str03=str01[2:7]
num=len(str01)
str04=str01+str03
str05=str01*3
str06=''
str07=' '
str08="\n"
str09="\r"
len06 = len(str06)
len07 = len(str07)
len08 = len(str08)
# '\' 叫做转义字符，
print("\\")#\

#str函数共计45个
str09 = str(123)
str11="qdf de edr"
str12 = str11.capitalize()
str13 = str11.title()
str14 = str11.center(10,'*')
num11 = str11.count(' ',0,len(str11)-1)
boole11  = str11.endswith('e',2,6)
#1.str.endswish
# "abcdefdyu asd as iju as ui" "acb" 1,7
'''
#analysis:遍历原字符串
#1.确定要检查的《子》字符串 beginIndex=1,endIndex=7
#2.切片切出要查询的字符串-->"bcdefd"
#3.倒序依次比较字符是否相等
#3.1 倒序遍历要查的字符串中每一个字符
#3.2 比较当前这个字符和切片结果倒序对应位置的字符是否相等
#4.要查询的字符串比较结束后输出结果:True False
strOrign="abcde"#fdyu asd as iju as ui"
strTarget='de'
beginIndex=0
endIndex=5
result=False

newstr=strOrign[beginIndex:endIndex]
i=len(strTarget)-1
index=len(newstr)-1
while i>=0:
    # print(strTarget[i])
    if strTarget[i]==newstr[index]:
        #继续比较下一位
        result=True
    else:
        result=False
        break
    i=i-1
    index=index-1

print(result)
'''
# num22 = "qwyiwqsqwyinedrwe".find("yin",0,4)
#str.find
#"qwewqsqwedrwe" -->"we",0,4
#analysis:遍历原字符串
#1. 在源字符串中找到目标字符串的第一个字符，并记录当前位置,要是到源字符串的末位还没找到,over返回-1
#2. 找到后,继续查看目标字符串第二位和源字符串第一步查询到的当前位置的下一位
#3. 两种情况
#3. 情况1:第二个字符相等，继续比较下一位，直到比较到目标字符串的结尾。程序结束，返回当前记录的位置
#3. 情况2:第二个字符(当前位置的下一位)不相等，目标字符串的第一个和源字符串不相等位置为新的起始位置进行比较
'''
strOrign="123456789ABCDEF"
strTarget='568'
beginIndex=0
endIndex=len(strOrign)-1
lowestIndex=-1

i=0
while i<=endIndex:
    if strTarget[0] == strOrign[i]:
        index=i
        originNextIndex=i+1
        targetNextIndex=0+1
        #检查一下以上两个index有没有越位
        pass
        while strTarget[targetNextIndex]==strOrign[originNextIndex]:
            originNextIndex=originNextIndex+1
            targetNextIndex=targetNextIndex+1
            #如果源到头了,循环结束
            #如果目标到头了，循环也结束
            if originNextIndex>=len(strOrign):
                break
            if targetNextIndex>=len(strTarget):
                break
        #这两个下标的关系:tNextIndex+i=oNextIndex
        print(targetNextIndex)
        print(originNextIndex)
        # targetNextIndex==2
        # targetNextIndex==len(strTarget)//照到了
        if targetNextIndex==len(strTarget):
            pass
            #找到了
            lowestIndex=i
            break
        else:
            pass
            #没找到
            i=originNextIndex
            continue
        pass
    else:
        if i==endIndex:
            lowestIndex=-1
            break
        i=i+1
        continue
    i=i+1
print("xxxxxxx=",lowestIndex)
'''

# a=[1,2,3,4,5]
# for elem in a:
#     print(elem)
# i=0
# while i<5:
#     print(a[i])
#     i=i+1
# i=4
# while i>=0:
#     print(a[i])
#     i=i-1

# 变量命名示例
# listST
# intY
# boolFlag
# userName
# passwd
# weartherData
# httpResult
# httpMessage
# isSuccess
# isNetworkEnable
# isYellow
# maxAge
# minAge
# minTextLength=9

#3.str.strip()
# str1111 = '   as da sda sd  '.strip()
#"as da sda sd"
#analysis
#目的:删除掉字符串的开始和结束的所有空格
#1,从开头找出第一个不是空格的字符的index
#2.从末尾找出第一个不是空格的字符的index
#3.对源字符串执行切片操作,切片的开始和结束index为前两步的值
'''
originStr='    adbuqwhdiwu dwaiojd   '
resultStr=''
beginIndex=0
endIndex=len(originStr)-1

#1
i=0
while i<len(originStr):
    if originStr[i]!=' ':
        beginIndex=i
        break
    i=i+1
#2
j=len(originStr)-1
while j>=0:
    if originStr[j]!=' ':
        endIndex=j
        break
    j=j-1
#3
resultStr=originStr[beginIndex:endIndex+1]
print('*',resultStr,'*',sep='')
'''


#ascii
#chr()  int-->char
#ord()  char-->int
'''
strNum=input('please input num:')
# ‘1234’
#如何判断输入的字符是可以转换为int的字符？
#old:遍历只要strNum里面都是['1','2','3'....,'9']
#new1:因为‘1’的ascii值为48，‘9’的ascii值是57
#     so当每一个字符的ascii值处于47<n<58
i=0
isNum=False
isChar=False
#old:
# listy=['0','1','2','3','4','5','6','7','8','9']
# while i<len(strNum):
#     if strNum[i] in listy:
#         isNum=True
#     else:
#         isNum=False
#         break
#     i=i+1

#new:
# a并且b  &&  and
# a或者b  ||  or
ua = ord('a')
uz = ord('z')
uA = ord('A')
uZ = ord('Z')
u0 = ord('0')
u9 = ord('9')
cA=chr(129)
uYYY=ord(u'元')
print(ua,type(ua))
while i<len(strNum):
    code = ord(strNum[i])
    isAZ = code>64 and code<91
    isaz = code>96 and code<123
    if isAZ or isaz:
    # if code>47 and code<58:
        isNum=True
    else :
        isNum=False
        True
    i=i+1

# isAZ = code>64 and code<91
# isaz = code>96 and code<123
# if isAZ or isaz:

if  isNum:
    num=int(strNum)
    print(num,type(num))
else:
    print('wrong num str')

boolIsan='sdass'.isalnum()
'''

#字符串共计45个函数
#列表共计11个函数
#至少完成[8,16,24]个
#
#量变-->质变

listOri=[1,2,2,3,[1,23]]
strOri='string'

listOri.append(5)    #c = a+b
listOri.clear()      #
listOri.copy()       #
listOri.count('a')   #
listOri.extend([3])
listOri.index(1,2,3) #
listOri.insert(0,[1,3])
listOri.pop()
listOri.remove(2)
listOri.reverse()    # a=[]
listOri.sort()       #

strOri.center(10,'*')
strOri.count('a')
strOri.endswith()
strOri.find('a',1,8)?strOri.index("a",1,8)
strOri.isalnum()
strOri.isdigit()
strOri.istitle()
strOri.isupper()
strOri.join([1,2,3,4])
strOri.ljust(10,'^')
strOri.lower()
strOri.replace('wwe','nba',3)
strOri.rindex()
strOri.split(sep='y',maxsplit=3)
strOri.startswith()
strOri.swapcase()
strOri.title()
strOri.zfill()


1:331, 
2:308,313,
3:308,
4:308,315,306
5:329,
6:
listOri.count('a') 
listOri.index(1,2,3)
listOri.sort() 
strOri.center(10,'*')
strOri.split(sep='y',maxsplit=3)
strOri.title()