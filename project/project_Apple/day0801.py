#顺序语句
#选择语句 if
#循环语句 for while( do-while foreach )

#if
#if [elif] [elif] [else]
# if 条件1:
#     语句1
# elif 条件2:
#     语句2
# elif 条件3:
#     语句3
# else:
#     语句4

# def func(age):
#     #1.检查参数合法性
#     #2.做方法该做的事情
#     #3.输出合法的返回值
    
'''
tagetAge=18
inputAge=-1
print(inputAge)
inputAge=int(input("请输入您的年龄:"))
flag=inputAge>tagetAge
flag1=inputAge>16
print(flag)
if flag:
    print("巨婴")
    print("你成年了,请负起责任,不要当巨婴")
    if inputAge>50:
        print("AAA:你老了")
    else:
        print("BBB:你壮了")
    print("FFFFF")
elif flag1:
    print("你该付刑事责任了..")
    pass
else:
    print("你还小,不要喝酒")
    pass
print('请吃饭了2....')
'''

#1.数据初始化或者定义
#2.数据的获取
#3.分析并处理数据
#3.1 基本比较
#3.2 不同年两端的处理
#3.2.1 if1
#3.2.1.1
#3.2.1.2
#3.2.2 if2
#3.2.3 else
#4.打印了东西

#循环语句
#1.while
'''
while 条件:
    pass1(循环体内容)
pass2

break
continue
'''

# l1=[1,2,3,4,5,6,7]
# index=0
# maxlength=len(l1)
# while index < maxlength :
#     print(l1[index])
#     pass
#     index=index+1
# print("over...")
'''
1
2
3
4
5
6
7
over...
'''

#loop
# while True:
#     oprt = input("请选择您要执行的功能:")
#     print("您选择了功能:",oprt)
#     if oprt=='1':
#         print('正在查看余额...')
#         continue
#         print("BBBB")
#     elif oprt=="2":
#         print('正在取款...')
#     elif oprt=="3":
#         print('正在存款...')
#     elif oprt=="exit":
#         print('正在exit...')
#         break
#     else:
#         print('按错了,请重新输入...')
#     print("asdtfijokl")
# print("End...")

#2. for
'''
c: 
for(int i=4;i<10;i++)
{
    prskdljsl;
}
python:遍历
for x in y:
    pass
'''
l2=[88,'dsf',(1,2,3),16,True,150,[1,2,3,4],'170',151,1.5]
#1.normal
# print(l2[0])
# ...
# print(l2[9])

#2.while
# index=0
# lens=len(l2)
# while index < lens :
#     print(l2[index])
#     index=index+1

#3.for
#class 
# l3=[[1,2,3,4,5],[11,22,33,44,55],[111,222,333,444,555]]
# for a in l3 :
#     print(type(a))
#     for b in a:
#         print(b)
# print(l3)


#print拓展用法
# print(1,2,3,4)
# print(1,2,3,4,sep=' ',end='\n')
# print(1,2,3,4,sep='-',end='\n')
# print(1,2,3,4,sep='*',end=' ')
# print(1,sep='-',end='\n')
# print(111111)

#3.0
# for
#3.1 
'''
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0 
'''
# l31=[]
# #1.生成list
# i=0
# while i<6:
#     l32=[]
#     j=0
#     while j<6:
#         l32.append(0)
#         j=j+1
#     l31.append(l32)
#     i=i+1
# # print(l31)
# #2.格式化输出list
# for line in l31:
#     for key in line:
#         print(key,end=' ')
#     print(' ')

#3.2 extend
'''
请输入棋盘大小:3
3x3棋盘如下:
0 0 0
0 0 0
0 0 0
请输入棋盘大小:6
6x6棋盘如下:
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0 
请输入棋盘大小:q
end...
'''
fiveMap=[]
while True:
    oper=input("size=")
    if oper=='q':
        #exit
        break
    num = int(oper)
    #绘制棋盘，size=num*num
    #1.创建num*num的列表list
    #1.1 先来一个空棋盘
    #1.2 填充num个元素
    #1.3 每一个元素都是一个num个0的列表
    #2.将list以指定的形式打印到屏幕
    #2.0 分析这个列表该如何输出。将列表里面的元素依次打印到各行，
    #    其中屏幕的每一行显示当前元素的所有子内容，以空格分开
    #2.1 先输出list的每个元素到每行
    #2.2 单个元素的所有子内容输出到同一行,只显示子元素本身，
    #    以空格隔开,最后一位以换行符结束
    
    #开工了
    #1
    #1.1
    fiveMap=[]
    #1.2
    i=0
    while i<num:
        #1.3
        #k=[0,0........0]共计num个
        k=[]
        j=0
        while j < num:
            k.append('0')
            j=j+1
        fiveMap.append(k)
        i=i+1
    #1 end
    print(fiveMap)
    #2
    #2.1
    for elem in fiveMap:
        # print(elem)
        for atom in elem:
            print(atom,end=' ')
        print('')
    #2 end


# 写代码的方式---从外层向内层写
#1.数据初始化或者定义
#2.数据的获取
#3.分析并处理数据
#3.1 基本比较
#3.2 不同年两端的处理
#3.2.1 if1
#3.2.1.1
#3.2.1.2
#3.2.2 if2
#3.2.3 else
#4.打印了东西
