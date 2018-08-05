#list.append(...)
#添加一个项
'''
listOriginal=[1,2,3,344,4,1.5,'aa','ab',' ',]
listInsert=['a','b','c']
Len=len(listOriginal)
i=0
result=[]
result=[0 for i in range(Len+1)]
indexOriginal=0
while True :
   if i<Len :
        result[i]=listOriginal[indexOriginal]
        indexOriginal+=1
   i+=1
   if i==Len :
       result[i]=listInsert
       break
print(result)
'''
#list.clear
#清空列表
'''
listOriginal=[1,2,3,344,4,1.5,'aa','ab',' ',]
consult=[]
Len=len(listOriginal)
i=0
listOriginal=consult
print(listOriginal)
'''
#list.copy()
#复制,与赋值的区别:改变复制的内容,不改变原来的内容,赋值两个都改变
'''
listOriginal=[1,2,3,344,4,1.5,'aa','ab',' ',]
Len=len(listOriginal)
i=0
result=[]
result=[0 for i in range(Len)]
indexOriginal=0
while i<Len :
    result[i]=listOriginal[indexOriginal]
    i+=1
    indexOriginal+=1
print(result)
'''
#list.count()
#计算指定的元素在列表中出现了多少
'''
listOriginal=[1,2,3,344,'[',[1,1,4],1.5,'*','aa','ab',' ']
Len=len(listOriginal)
target='aa'
i=0
num=0
print(type(target))
while i<Len :      
    if type(target)==type(1):
        while i<Len:
            if listOriginal[i] == target:
                num+=1
            i+=1 
    elif type(target)==type([1]) :
        while i<Len:
            if listOriginal[i] == target:
                num+=1
            i+=1
    elif type(target)==type((1,2)) :
        while i<Len:
            if listOriginal[i] == target:
                num+=1
            i+=1
    elif type(target)==type(1.5) :
        while i<Len:
            if listOriginal[i] == target:
                num+=1
            i+=1
    elif type(target)==type('d') :
        while i<Len:
            if listOriginal[i] == target:
                num+=1
            i+=1               
print(num)
'''
#list.extend(...)
#同时将多个值附加到列表末尾
'''
listInsert=['a','b','c']
Len=len(listOriginal)
LenInsert=len(listInsert)
i=0
result=[]
result=[0 for i in range(Len+LenInsert)]
indexOriginal=0
indexInsert=0
while i<len(result) :
   if i<Len :
        result[i]=listOriginal[indexOriginal]
        indexOriginal+=1
   if i>=Len and i<len(result) :
        result[i]=listInsert[indexInsert]
        indexInsert+=1
   i+=1
print(result)
'''
#list.index(..,[ ,[]])
#从哪一个位置到哪一个位置查找哪一个值,返回第一个的下标
'''
listOriginal = list(input("please input some word:"))
Target = list(input("please input words which you want to find:"))
intStart = int(input("please input the index where you want to start:"))
intEnd = int(input("please input the index where you want to end:"))
print(listOriginal)
print(Target)
listOriginal1=listOriginal[intStart:intEnd]
index=0
result=-1
while index<len(listOriginal) :
    if Target[0]==listOriginal[index] :
        if 1==len(Target) :
            result=index
            break
        else :
            indexTarget=0+1
            indexOriginal=index+1
            while Target[indexTarget]==listOriginal[indexOriginal] :
                indexTarget+=1
                indexOriginal+=1
                if indexTarget==len(Target) :
                    break
                if indexOriginal==len(listOriginal) :
                    break
            if indexTarget==len(Target) :
                result=index
                break
            else :
                index=indexOriginal
                continue
    else :
        if index == len(listOriginal):
            print("-1")
            break
        index+=1
        continue
    index+=1
print(result)
'''
#list.insert()
#在第几个位置插入
'''
listOriginal=[1,2,3,4,5]
listInsert=[9]
indexIn=int(input("please input a index which you want to insert:"))
lList=listOriginal[:indexIn]
rList=listOriginal[indexIn:]
print(lList+listInsert+rList)
'''
#list.pop()
#弹出最后一个的值
'''
listOriginal=[1,2,3,4,5]
Len=len(listOriginal)-1
print(listOriginal[Len])
'''
#list.remove()
#移除某值(下标最小)
'''
listOriginal=[1,2,3,4,5]
rm=[3]
i=0
while i<len(listOriginal) :
    if listOriginal[i]==rm[0] :
        Llist=listOriginal[:i+1]
        Rlist=listOriginal[i+1:]
        a=Llist.pop()
        print(Llist+Rlist)
        break
    i+=1
'''
#list.reverse()
#反向输出
'''
listOriginal=[1,2,3,4,5]
a=listOriginal[::-1]
print(a)
'''
#list.sort()
#排序
'''
listOriginal=[1,2,3,4,5,9,6,3]
i=0
j=1
k=[0]
while i<len(listOriginal) :
    j=i+1
    while j<len(listOriginal):
        if listOriginal[i]>listOriginal[j]:
            k[0]=listOriginal[i]
            listOriginal[i]=listOriginal[j]
            listOriginal[j]=k[0]
        j+=1
    i+=1
print(listOriginal)
'''

#str.center()
#通过在两边添加填充字符（默认为空格）让字符串居中
'''
strOriginal="qwertyuiop"
strFill=input("please input a word what you want to fill:")
width=int(input('please input width you want:'))
Len=len(strOriginal)
halfLen=int(Len/2)
halfWidth=int(width/2)
lNewStr=strOriginal[0:halfLen]
rNewStr=strOriginal[halfLen:]
lNewStr1=''
Len1=len(lNewStr)
Len2=len(rNewStr)
index=0
while index<halfWidth-Len2 :
    rNewStr=rNewStr+strFill
    index+=1
index1=0
while index1<=halfWidth-Len1-1 :
    lNewStr1=lNewStr1+strFill
    if index1==halfWidth-Len1-1 :
        lNewStr1=lNewStr1+lNewStr
        break
    index1+=1
print(lNewStr1+rNewStr)
'''
#str.count()
#统计某个字符或字符串出现的次数
'''
strOriginal='fdgga435656 ^&* asdhfah'
target=input("please input what you should inquiry:")
i=0
num=0
while i<len(strOriginal):
    if strOriginal[i] == target:
        num+=1
    i+=1 
print(num)  
'''     
#str.endswith()
#判断字符串是否由指定字符结尾
'''
Original = list(input("please input some word:"))
Target = list(input("please input words which you want to find:"))
intStart = int(input("please input the index where you want to start:"))
intEnd = int(input("please input the index where you want to end:"))
NewStr = Original[intStart:intEnd+1]
OppOriginal = NewStr[::-1]
OppTraget = Traget[::-1]
Len=len(OppOriginal)
result=False
indexTarget,indexOriginal=0,0
while indexTarget<Len :
    if OppTarget[indexTarget]==OppOriginal[indexOriginal]:
        result=True
    else:
        result=False
        break
    indexTarget+=1
    indexOriginal+=1
print(result)
'''
#str.find
##查找子串,如果找到，就返回子串的第一个字符的索引，否则返回-1
'''
StrOriginal='qwrtyqreet'
StrTarget='re'
index=0
boolJudge= StrTarget in StrOriginal 
if boolJudge==False :
    print("-1")
else :
    while index<len(StrOriginal) :
        if StrTarget[0]==StrOriginal[index] :
            if 1==len(StrTarget) :
                result=index
                break
            else :
                indexTarget=0+1
                indeOriginal=index+1
                while StrTarget[indexTarget]==StrOriginal[indexOriginal] :
                    indexTarget+=1
                    indexOriginal+=1
                    if indexStrget==len(StrTarget) :
                        break
                    if indexOriginal==len(StrOriginal) :
                        break
                if indexTarget==len(StrTarget) :
                    result=index
                    break
                else :
                    index=indexOriginal
                    continue
        else :
            if index == len(StrOriginal):
                print("-1")
                break
            index+=1
            continue
        index+=1
    print(index)
'''
#str.isalnum()
#判断字符串中的字符是否全部是数字和字母
'''
strOriginal='1234asdsdgf'
index=0
isbool=False
while index<len(strOriginal):
    if 48<=ord(strOriginal[index])<=57 or 65<=ord(strOriginal[index])<=90 or 97<=ord(strOriginal[index])<=122:
        isbool=True
    else :
        isbool=False
        break
    index+=1
print(isbool)
'''
#str.isdigit()
#判断字符串中的是否全是数字
'''
strOriginal='1234asdsdgf'
index=0
isbool=False
while index<len(strOriginal):
    if 48<=ord(strOriginal[index])<=57:
        isbool=True
    else :
        isbool=False
        break
    index+=1
print(isbool)
'''
#str.istitle()
#判断是否是title形式
'''
strOriginal=" Gr Fty Ed Rf Gfg h"
index=0
i=1
isbool=False
while index<len(strOriginal):
    if ord(strOriginal[index])==32 or 65<=ord(strOriginal[index])<=90 or 97<=ord(strOriginal[index])<=122:
        if strOriginal[0]!=' ':
            if 65<=ord(strOriginal[0])<=90 :
                 while i<len(strOriginal)-1:
                    if strOriginal[i]==' ':
                        while strOriginal[i+1]!=' ':
                            if 65<=ord(strOriginal[i+1])<=90:
                                isbool=True
                                break
                            else :
                                isbool=False
                                break
                        if isbool==False:
                            break
                    i+=1
            else :
                isbool=False
                break        
        else :
            while index<len(strOriginal):
                if strOriginal[index]==' ':
                    while strOriginal[index+1]!=' ':
                        if 65<=ord(strOriginal[index+1])<=90:
                            isbool=True
                            break
                        else :
                            isbool=False
                            break
                    if isbool==False :
                        break
                index+=1
    else :
        isbool=False
        break
    if isbool == False :
        break
    index+=1
print(isbool)
'''
#str.isupper()
#判断字符串的字母是否都是大写
'''
strOriginal='JHUIHO4#&F'
isbool=True
index=0
i=0
while index<len(strOriginal):
    if 65<=ord(strOriginal[index])<=90 :
        while i<len(strOriginal) :
            if 97<=ord(strOriginal[i])<=122:
                isbool=False
                break
            i+=1
    index+=1
print(isbool)
'''
#str.jion()
#使用指定字符或字符串，拼接由字符串组成的数组，返回字符串
'''
listOriginal=['sddf','dsff','sgfdg']
connect=input("please input what you want to connect:")
Len=len(listOriginal)
strResult=''
index=0
while index<Len :
    strResult=strResult+listOriginal[index]+connect
    index+=1
strResult=strResult[:len(strResult)-1]
print(strResult)
'''
#str.ljust()
##左对齐,参数可写宽度和填充字符
'''
strOriginal='   JHUIHO4#&F'
width=int(input("please input width what you what:"))
strFill=input("please input what you want to fill:")
index=0
strResult=strOriginal
while index<width:
    strResult=strResult+strFill
    index+=1
print(strResult)
'''
#str.lower()
##将字符串中的所有字母改成小写
'''
strOriginal='   JH UIHO 4#&F'
index=0
while index<len(strOriginal):
    if 65<=ord(strOriginal[index])<=90:
        a=chr(ord(strOriginal[index])+32)
        lNewStr=strOriginal[:index]
        rNewStr=strOriginal[index+1:]
        NewStr=lNewStr+a+rNewStr
        strOriginal=NewStr       
    index+=1
print(NewStr)
'''
#str.replace()
#原字符串中的字符(第一个参数),被新的字符(第二个参数)替换,替换几个(第三个参数count)
'''
strOriginal='agasfe234trh'
str1=input("please input what you want to replace:")
str2=input("please input theword you want replace:")
num=int(input("please input numbers what you want:"))
i=0
Len=len(str1)
index=strOriginal.find(str1)
while i<num :  
    Len=len(str1)
    index=strOriginal.find(str1)
    lNewStr=strOriginal[:index]
    rNewStr=strOriginal[index+Len:]
    NewStr=lNewStr+str2+rNewStr
    strOriginal=NewStr
    i+=1
print(NewStr)
'''
#str.rindex()
#从右边找到字符,输出最大下标,找不到报错
'''
strOriginal='jakjsgfl2343gf'
oppStrOriginal=strOriginal[::-1]
StrTarget='0'
index=0
boolJudge= StrTarget in strOriginal 
if boolJudge==False :
    print("error")
else :
    while index<len(oppStrOriginal) :
        if StrTarget[0]==oppStrOriginal[index] :
            if 1==len(StrTarget) :
                result=index
                break
            else :
                indexTarget=0+1
                indexOppStrOriginal=index+1
                while StrTarget[indexTarget]==oppStrOriginal[indexOppStrOriginal] :
                    indexTarget+=1
                    indexOppStrOriginal+=1
                    if indexTarget==len(StrTarget) :
                        break
                    if indexOppStrOriginal==len(oppStrOriginal) :
                        break
                if indexTarget==len(StrTarget) :
                    result=index
                    break
                else :
                    index=indexOppStrOriginal
                    continue
        index+=1
    print(len(strOriginal)-index-1)
'''
#str.split()
#使用指定字符或字符串将原字符串切割
'''
strOriginal='adgffg43243tf55t'
strAppoint=input("please input what you want to appiont:")
num=int(input('please input times you want:'))
NewStr=strOriginal.replace(strAppoint,',',num)
listResult=[]
index=0
while index<len(NewStr):
    if NewStr[index]==',':
        result=NewStr[:index]
        rNewStr=NewStr[index+1:]
        listResult.append(result)
        NewStr=rNewStr
        index=-1
    index +=1
listResult.append(NewStr)
print(listResult)
'''
#str.startswith()
#判断字符串是否以..开头
'''
Original = list(input("please input some word:"))
Target = list(input("please input words which you want to find:"))
intStart = int(input("please input the index where you want to start:"))
intEnd = int(input("please input the index where you want to end:"))
NewStr = Original[intStart:intEnd+1]
Len=len(Original)
result=False
indexTarget,indexOriginal=0,0
while indexTarget<len(Target) :
    if Target[indexTarget]==Original[indexOriginal]:
        result=True
    else:
        result=False
        break
    indexTarget+=1
    indexOriginal+=1
print(result)
'''
#str.swapcase()
#字符串中大小写转换
'''
strOriginal1='fsgfheBYUGHLULtrythg34t5y6'
strOriginal=list(strOriginal1)
index=0
while index<len(strOriginal):
    if 65<=ord(strOriginal[index])<=90:
        strOriginal[index]=chr(ord(strOriginal[index])+32)        
    elif 97<=ord(strOriginal[index])<=122:
        strOriginal[index]=chr(ord(strOriginal[index])-32) 
    index+=1
result=''
i=0
while i<len(strOriginal):
    result=result+strOriginal[i]
    i+=1
print(result)
'''
#str.title()
#将字符串转成title形式
'''
strOriginal1=' gfgerg43t 53tg1g1 1f3 fa34'
index=0
strOriginal=list(strOriginal1)
i=1
while index<len(strOriginal):
    if strOriginal[0]!=' ':
        if 97<=ord(strOriginal[0])<=122 :
            strOriginal[0]=chr(ord(strOriginal[0])-32)
            while i<len(strOriginal)-1:
                if strOriginal[i]==' ':
                    while strOriginal[i+1]!=' ':
                        if 97<=ord(strOriginal[i+1])<=122:
                            strOriginal[i+1]=chr(ord(strOriginal[i+1])-32)
                            break
                        else :
                            break
                i+=1
        else:
            break               
    else :
        while index<len(strOriginal):
            if strOriginal[index]==' ':
                while strOriginal[index+1]!=' ':
                    if 97<=ord(strOriginal[index+1])<=122:
                        strOriginal[index+1]=chr(ord(strOriginal[index+1])-32)
                        break
                    else :
                        break
            index+=1
    index+=1
j=0
result=''
while j<len(strOriginal):
    result=result+strOriginal[j]
    j+=1
print(result)
'''
#str.zfill()
#用0在左边填充
'''
strOriginal=' gft 53tg1 fa34'
width=int(input("please input width you want:"))
Len=len(strOriginal)
index=0
result=''
while index<width-Len:
    result=result+'0'
    index+=1
result=result+strOriginal
print(result)
'''