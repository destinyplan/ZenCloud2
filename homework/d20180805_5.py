# 1. str.endswith方法的实现
# 方法定义：endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
# Orign='asdaq'
# Compare='aq'
# Begin=0
# End=5
# result=False

# new=Orign[Begin:End]
# a=len(Compare)-1
# b=len(new)-1
# while a>=0:
#     if Compare[a]==new[b]:
#         result=True
#     else :
#         result=False
#         break
#     a=a-1
#     b=b-1
# print(result)

# 2.str.find方法的实现
# 方法定义：find()方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否自返回-1
# 暂时没有完全实现功能：
# strOrign="123456789ABCDEF"
# strcount='568'
# begini=0
# endi=len(strOrign)-1
# lowesti=-1

# i=0
# while i<=endi:
#     if strcount[0] == strOrign[i]:
#         i=i
#         originNexti=i+1
#         countNexti=0+1
#         #检查一下以上两个i有没有越位
#         pass
#         while strcount[countNexti]==strOrign[originNexti]:
#             originNexti=originNexti+1
#             countNexti=countNexti+1
#             #如果源字符串到头了,循环结束
#             #如果目标到头了，循环也结束
#             if originNexti>=len(strOrign):
#                 break
#             if countNexti>=len(strcount):
#                 break
#         #这两个下标的关系:tNexti+i=oNexti
#         print(countNexti)
#         print(originNexti)
#         # countNexti==2
#         # countNexti==len(strcount)//找到了
#         if countNexti==len(strcount):
#             pass
#             #找到了
#             lowesti=i
#             break
#         else:
#             pass
#             #没找到
#             i=originNexti
#             continue
#         pass
#     else:
#         if i==endi:
#             lowesti=-1
#             break
#         i=i+1
#         continue
#     i=i+1
# print("xxxxxxx=",lowesti)

# 3.str.strip方法的实现：
# 方法定义：strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
# 1.首先从头开始判断第一个不为' '的字符，利用切片切去头部空格并记录其坐标序号
# 2.再利用长度方法Len测出其总的字符串长度自减实现从末尾寻找第一个不为' '的字符，利用切片切去尾部空格并记录其坐标序号
# 3.利用坐标序号切片并输出
# a = "         lllllllzzzzzzz          "
# Long=len(a)
# i=0
# while i<=Long:
#     if a[i]!=' ':     #从头部判断是否为空格
#         New=a[i:]     #利用切片建立新的列表
#         j=0
#         while j<=Long:
#             if a[Long-1-j]!=' ':      #从尾部判断是否为空格
#                 end=New[:j-1]         #从尾部将新列表切片得到最终值
#                 print(end)
#                 break
#             j=j+1
#         break
#     else:
#         pass
#     i=i+1

# 第二种方法：
# a = "         lllllllzzzzzzz          "
# Long=len(a)
# i=0
# while i<=Long:
#     if a[i]!=' ':     
#         strat=int(i)   
#         j=0
#         while j<=Long:
#             if a[Long-1-j]!=' ':  
#                 end=int(Long-j-1)
#                 result=a[int(strat):int(end)]        
#                 print(result)
#                 break
#             j=j+1
#         break
#     else:
#         pass
#     i=i+1

# 4.list.append方法的实现：
# 方法定义：append() 方法用于在列表末尾添加新的对象。
# Old=[1,2,3]
# New=[4]
# append=Old+New
# print(append)

# 5.list.clear方法的实现：
# 方法定义：clear() 函数用于清空列表。
# list1=[1,2,3,4]
# New=[]
# list1=New
# print(list1)

# 6.list.copy方法的实现：
# 方法定义：copy() 函数用于复制列表。
# list1=[1,2,3,4,5]
# Len=len(list1)
# i=0
# result=[]
# result=[0 for i in range(Len)]
# list2=0
# while i<Len :
#     result[i]=list1[list2]
#     i+=1
#     list2=list2+1
# print(result)


# 7.list.i方法的实现：
# 方法定义：i() 函数用于从列表中找出某个值第一个匹配项的索引位置。
# list1=[1,2,3,4,5]
# a=3
# i=0
# while i<=4:
#     if list1[i]==a:
#         print(i)
#     else:
#         pass
#     i=i+1

# 8.list.insert方法的实现：
# 方法定义：insert() 函数用于将指定对象插入列表的指定位置。
# list1=[1,2,3,4,5]
# New=[6]
# In=int(input("输入你想要插入的位置："))
# A=list1[:In]
# B=list1[In:]
# print(A+New+B)

# 9.list.pop方法的实现：
# 方法定义：pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# a=[1,2,3,4,5]
# len1=len(a)-1
# print(a[len1])

# 10.list.reverse方法的实现：
# 方法定义：reverse() 函数用于反向列表中元素。
# a=[1,2,3,4,5]
# b=a[::-1]
# print(b)

# 11.list.remove方法的实现：
# 方法定义：remove() 函数用于移除列表中某个值的第一个匹配项。
# list1=[1,2,3,4,5]
# a=[3]
# i=0
# while i<5:
#     if list1[i]==a[0] :
#         Lift=list1[:i+1]
#         Right=list1[i+1:]
#         b=Lift.pop()
#         print(Lift+Right)
#         break
#     i=i+1

# 12.list.sort方法的实现：
# 方法定义：sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
# list1=[1,4,3,2,7,5,9,6,3]
# i=0
# j=1
# k=[0]
# while i<len(list1) :
#     j=i+1
#     while j<len(list1):
#         if list1[i]>list1[j]:
#             k[0]=list1[i]
#             list1[i]=list1[j]
#             list1[j]=k[0]
#         j=j+1
#     i=i+1
# print(list1)

# 13.str.center方法的实现：
# 方法定义：center()返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
# A="qwertyuiop"
# fill=input("please input a word what you want to fill:")
# width=int(input('please input width you want:'))
# Len=len(A)
# halfLen=int(Len/2)
# halfWidth=int(width/2)
# L=A[0:halfLen]
# Rr=A[halfLen:]
# L1=''
# Len1=len(L)
# Len2=len(Rr)
# i=0
# while i<halfWidth-Len2 :
#     Rr=Rr+fill
#     i+=1
# i1=0
# while i1<=halfWidth-Len1-1 :
#     L1=L1+fill
#     if i1==halfWidth-Len1-1 :
#         L1=L1+L
#         break
#     i1+=1
# print(L1+Rr)

# 14.str.count方法的实现：
# 方法的定义：Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
# Old='ewytyuwqteygfhjgfsjhghgyutqwyuteuyqqw'
# count=input("请输入查询内容:")
# i=0
# num=0
# while i<len(Old):
#     if Old[i] == count:
#         num=num+1
#     i=i+1 
# print(num)  

# 15.str.isdigit方法的实现：
# 方法的定义：Python isdigit() 方法检测字符串是否只由数字组成。
# Old='5566342sgytyusfdsqqwe'
# i=0
# a=False
# while i<len(Old):
#     if 48<=ord(Old[i])<=57:
#         a=True
#     else :
#         a=False
#         break
#     i=i+1
# print(a)

# 16.str.isalnum方法的实现：
# 方法的定义：Python isalnum() 方法检测字符串是否由字母和数字组成。
# Old='78979hgajhgdajgqeq'
# i=0
# a=False
# while i<len(Old):
#     if 48<=ord(Old[i])<=57 or 65<=ord(Old[i])<=90 or 97<=ord(Old[i])<=122:
#         a=True
#     else :
#         a=False
#         break
#     i=i+1
# print(a)

# 17.str.isupper方法的实现：
# 方法的定义：Python isupper() 方法检测字符串中所有的字母是否都为大写。
# Old='ghqgeGHGJHuuiyiu'
# a=True
# index=0
# i=0
# while index<len(Old):
#     if 65<=ord(Old[index])<=90 :
#         while i<len(Old) :
#             if 97<=ord(Old[i])<=122:
#                 a=False
#                 break
#             i=i+1
#     index=index+1
# print(a)

# 18.str.lower方法的实现：
# 方法的定义：Python lower() 方法转换字符串中所有大写字符为小写。
# Old='GHGJGyuyiuHUK$$'
# i=0
# while i<len(Old):
#     if 65<=ord(Old[i])<=90:
#         a=chr(ord(Old[i])+32)
#         L=Old[:i]
#         R=Old[i+1:]
#         new=L+a+R
#         Old=new       
#     i+=1
# print(new)

# 19.str.join方法的实现：
# 方法的定义：Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# Old=['qwer','asdf','zxcv']
# Connect=input("请输入连接符:")
# Len=len(Old)
# Result=''
# i=0
# while i<Len :
#     Result=Result+Old[i]+Connect
#     i=i+1
# Result=Result[:len(Result)-1]
# print(Result)

# 20.str.ljust方法的实现：
# 方法的定义：Python ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
# Old='ghgetywtqu!!!!!'
# width=int(input("请输入长度:"))
# fill=input("请输入填充字符:")
# i=0
# result=Old
# while i<width:
#     result=result+fill
#     i=i+1
# print(result)

# 21.str.split方法的实现：
# 方法的定义：Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串。

# 22.str.startswith方法的实现：
# 方法的定义：Python startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
# Old='dhgjaghdgytqeu'
# Target=list(input("请输入需要查找字符:"))
# Start=int(input("请输入开始位置:"))
# End=int(input("请输入结束位置:"))
# NewStr=Old[Start:End+1]
# Len=len(Old)
# result=False
# indexTarget,indexOld=0,0
# while indexTarget<len(Target) :
#     if Target[indexTarget]==Old[indexOld]:
#         result=True
#     else:
#         result=False
#         break
#     indexTarget=indexTarget+1
#     indexOld=indexOld+1
# print(result)

# 23.str.zfill方法的实现：
# 方法的定义：Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
# Old='reqwtrqtwt'
# width=int(input("请输入长度:"))
# Len=len(Old)
# i=0
# result=''
# while i<width-Len:
#     result=result+'0'
#     i=i+1
# result=result+Old
# print(result)

# 24.str.swapcase方法的实现：
# 方法的定义：Python swapcase() 方法用于对字符串的大小写字母进行转换。
# Old='qeASAjhQyffTFtdtDFjrYR'
# lOld=list(Old)
# i=0
# while i<len(lOld):
#     if 65<=ord(lOld[i])<=90:
#         lOld[i]=chr(ord(lOld[i])+32)        
#     elif 97<=ord(lOld[i])<=122:
#         lOld[i]=chr(ord(lOld[i])-32) 
#     i=i+1
# result=''
# a=0
# while a<len(lOld):
#     result=result+lOld[a]
#     a=a+1
# print(result)