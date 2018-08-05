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
# strTarget='568'
# beginIndex=0
# endIndex=len(strOrign)-1
# lowestIndex=-1

# i=0
# while i<=endIndex:
#     if strTarget[0] == strOrign[i]:
#         index=i
#         originNextIndex=i+1
#         targetNextIndex=0+1
#         #检查一下以上两个index有没有越位
#         pass
#         while strTarget[targetNextIndex]==strOrign[originNextIndex]:
#             originNextIndex=originNextIndex+1
#             targetNextIndex=targetNextIndex+1
#             #如果源字符串到头了,循环结束
#             #如果目标到头了，循环也结束
#             if originNextIndex>=len(strOrign):
#                 break
#             if targetNextIndex>=len(strTarget):
#                 break
#         #这两个下标的关系:tNextIndex+i=oNextIndex
#         print(targetNextIndex)
#         print(originNextIndex)
#         # targetNextIndex==2
#         # targetNextIndex==len(strTarget)//找到了
#         if targetNextIndex==len(strTarget):
#             pass
#             #找到了
#             lowestIndex=i
#             break
#         else:
#             pass
#             #没找到
#             i=originNextIndex
#             continue
#         pass
#     else:
#         if i==endIndex:
#             lowestIndex=-1
#             break
#         i=i+1
#         continue
#     i=i+1
# print("xxxxxxx=",lowestIndex)

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


# 7.list.index方法的实现：
# 方法定义：index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
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