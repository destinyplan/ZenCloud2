# 1.list.clear方法的实现：
# 方法定义：clear() 函数用于清空列表。
# list1=[1,2,3,4]
# list2=[]
# list1=list2
# print(list1)

#2.listOri.pop()
#弹出列表最后一个元素，并且删除列表已弹出的元素
# list1=[1,2,3,4]
a=[1,2,3,4,5]
# len1=len(a)-1
# print(a[len1])

#3.list.sort
list1=[1,4,3,2,7,5,9,6,3]
i=0
j=0
k=[0]
while i<len(list1) :
     j=i+1
     while j<len(list1):
         if list1[i]>list1[j]:
             k[0]=list1[j]
             list1[j]=list1[i]
             list1[i]=k[0]
         j=j+1
     i=i+1
print(list1)

#4.list.reverse
#列表中的元素顺序反转
list1=[1,2,3,4,5]
list2=list1[::-1]
print(list2)

#5.list.remove
#函数用于移除列表中某个值的第一个匹配项
list=[1,2,3,4,5]
x = list.index(3)
del list[x]
print(list)

#6.list.insert
insert() 函数用于将指定对象插入列表的指定位置。
list=[1,2,3,4,5]
x=[3]
y=2
A=list[0:2]
B=list[2:]
print(A+x+B)

#7.list.copy
#copy() 函数用于复制列表。
x=[1,2,3,344,4,1.5,'aa','ab',' ',]
Len=len(x)
result=[]
i=0
result=[0 for i in range(Len)]
j=0
while i<Len:
    result[i]=x[j]
    i=i+1
    j=j+1
print(result)

#8.list.count()
#计算指定的元素在列表中出现了多少
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

#9.list.extend
x=[1,2,3,4]
y=[2,3,5]
len2=len(y)
i=0
while i<len2:
    x=x+[y[i]]
    i=i+1
print(x)  

#10.list.index





