# 乘法口诀表：
# # 正序输出：
# i=1
# while i<10:
#     j=1
#     while j<i+1:
#         print("%d*%d=%d"%(j,i,i*j),end=' ')
#         j=j+1
#     i=i+1
#     print(' ')

# #倒序输出：
# i=9
# while i>=1:
#     j=1
#     while j<=i:
#         print("%d*%d=%d"%(j,i,i*j),end=' ')
#         j=j+1
#     i=i-1
#     print(' ')

# str.endswith方法的实现
# 方法定义：endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
Orign='asdaq'
Compare='aq'
Begin=0
End=5
result=False

new=Orign[Begin:End]
a=len(Compare)-1
b=len(new)-1
while a>=0:
    if Compare[a]==new[b]:
        result=True
    else :
        result=False
        break
    a=a-1
    b=b-1
print(result)


#str.strip方法的实现：
# 方法定义：strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
# 1.首先从头开始判断第一个不为' '的字符，利用切片切去头部空格并记录其坐标序号
# 2.再利用长度方法Len测出其总的字符串长度自减实现从末尾寻找第一个不为' '的字符，利用切片切去尾部空格并记录其坐标序号
# 3.利用坐标序号切片并输出
a = "         lllllllzzzzzzz          "
Long=len(a)
i=0
while i<=Long:
    if a[i]!=' ':     #从头部判断是否为空格
        New=a[i:]     #利用切片建立新的列表
        j=0
        while j<=Long:
            if a[Long-1-j]!=' ':      #从尾部判断是否为空格
                end=New[:j-1]         #从尾部将新列表切片得到最终值
                print(end)
                break
            j=j+1
        break
    else:
        pass
    i=i+1



# # str.find方法的实现
# # 方法定义：find()方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否自返回-1
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
# 以上为老师上课讲解代码  可供参考




