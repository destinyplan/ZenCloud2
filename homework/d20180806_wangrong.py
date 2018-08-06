#while循环体
'''
while True :
    oprt = input("请输入季节：")
    print("你选择的季节是:",oprt)
    if oprt=='1':
        print('春季')
    elif oprt=='2':
        print('夏季')
    elif oprt=='3':
        print('秋季')
    elif oprt=='4':
        print('冬季')
    elif oprt=="q":
        print('正在退出')       
        break
    else：
        print("输入有误，请重新输入！")
print("Game over")
'''
#棋盘
'''
l1=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
for a in l1:
    print(0,0,0,0,0,0,sep=' ',end='\n')
'''

#规定棋盘大小
'''
while True:
    oper=input("size=")
    if oper=='q':
        break
    num=int(oper)
    if num>0:
        chessMap=[]
        i=0
        while i<num:
            k=[]
            j=0
            while j<num:
                k.append(0)
                j=j+1
            chessMap.append(k) 
            i=i+1
        print(chessMap)
        for elem in chessMap:
            for atom in elem:
                print(atom,end=' ')
            print('')
'''
#乘法表 
'''
i=1
while i<10:
    j=1
    while j<=i:
        print(i,'*',j,'=',i*j,end=' ')
        j=j+1
    print('')
    i=i+1
    '''
#反向输出乘法表
'''
i = 9
while i >= 1:
    j=1
    while j<=i:
        print(i,'*',j,'=',i*j,end = ' ')
        j=j+1
    print()
    i=i-1
    '''
#endswith
strOrign="abcdefhi" 
strTarget='i'
beginIndex=0 
endIndex=8 
result=False 
newstr=strOrign[beginIndex:endIndex] 
i=len(strTarget)-1 
index=len(newstr)-1 
while i>=0: 
    print(strTarget[i]) 
    if strTarget[i]==newstr[index]: 
        result=True 
    else: 
        result=False 
        break 
    i=i-1 
    index=index-1 
print(result) 
#1.listOri.append() 
给列表末尾添加一个指定的元素
eg. [1,2,3],'wr' --> [1,2,3,'wr']
code:
newList=[1,2,3]
list2=['wr','dfg',1,4,6]
Len=len(list2)
i=0
result=[]
result=[0 for i in range(Len+1)]
indexlist2=0
while True:
    if i<Len:
        result[i]=list2[indexlist2]
        indexlist2+=1
        i=i+1
        if i==Len:
            result[i]=newList
            break
print(result)
运行结果：['wr', 'dfg', 1, 4, 6, [1, 2, 3]]
#2.listOri.clear() 
清空列表元素
code: 
list1=[1,2,3,'ashdw']
oriList=[]
list1=oriList
print(list1)
运行结果：[]
#3.listOri.copy()
复制列表元素
eg. a=[1,2,3]  b=a.copy()  print(b)  -->b=[1,2,3] 
code:
list1=[1,2,3,4,5]
list2=[]
list2=list1
print(list2)
运行结果：[1, 2, 3, 4, 5]
#4.listOri.count()-->代码不成熟
计算括号中的元素在列表中出现的次数
eg. a=[1,2,3,2,5,7,9,2] b=a.count(2) --> 3
code:
a=[18,2,9,6,2,7,3,'we',2]
index=0
maxlength=len(a)
while index < maxlength:
    print(a[index])
    index=index+1
#5.listOri.extend()
将列表的元素与括号中的元素进行拼接
code：




# #6.listOri.index()
eg. a=[4,2,4,6,7,1,46] a.index(2,0,5)
从下标为0开始到5结束（不包括5），寻找2这个元素
code：


    





# #7.listOri.insert()
eg. a=[4,23,45,4,32,24] a.insert(4,2)
在列表中第4个元素插入2
code：
oriList=[4,23,45,4,32,24]
insert=[2]
i=int(input("输入要插入的下标："))
newList1=oriList[ :i]
newList2=oriList[i:]
newList=newList1+insert+newList2
print(newList)
运行结果：
输入要插入的下标：4
[4, 23, 45, 4, 2, 32, 24]
#8.listOri.pop()
eg. a=[1,3,4,5,6,7,9] b=a.pop()
拿出a列表的最后一个元素，添加到b列表
code：
oriList=[1,2,3,4,5,6,7,9]
a=len(oriList)-1
b=oriList[a]
print(b)
#9.listOri.remove()
eg. a=[2,4,7,5,6,3,5,2] a.remove(5)
# 删去a列表中5这个元素（只删一次）
code：






#10.listOri.reverse()
将列表反向输出
code：
a=[2,3,5,6,8,1,10,12]
b=a[::-1]
print(b)
运行结果：[12, 10, 1, 8, 6, 5, 3, 2]
# #11.listOri.sort()
将列表按升序排列出来
code:
l1=[1,3,4,56,7,73,12]
n= len(l1)
for x in range(n-1):
   for y in range(n-1-x):
      if l1[y]>l1[y+1]:
         l1[y],l1[y+1]=l1[y+1],l1[y]
print(l1)
运行结果：[1, 3, 4, 7, 12, 56, 73]