#顺序语句
#选择语句 if
#循环语句 for while do-while foreach 

#if
#if [elif] [elif] [else]
# if 条件:
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
countiune
'''

l1=[1,2,3,4,5,6,7]
index=0
maxlength=len(l1)
while index < maxlength :
    print(l1[index])
    pass
    index=index+1
print("over...")

#loop
while True:
    oprt = input("请选择您要执行的功能:")
    print("您选择了功能:",oprt)
    if oprt=='1':
        print('正在查看余额...')
        continue
        print("BBBB")
    elif oprt=="2":
        print('正在取款...')
    elif oprt=="3":
        print('正在存款...')
    elif oprt=="exit":
        print('正在exit...')
        break
    else:
        print('按错了,请重新输入...')
    print("asdtfijokl")
print("End...")

