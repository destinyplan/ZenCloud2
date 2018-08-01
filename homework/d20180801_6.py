# a=[1,1,1]
# print(a)
# a.append("eeeeeee")
# a.clear()
# b = a.copy()
# print(a)
#列表提供的方法
# a=[1,2,3,5,5,4,3,6,3,7,3,8,4,2]
# # print(a)
# # a.append(["1",""])
# # a.remove(505)
# # a.reverse()
# a.remove
# print(a)

# 元组（序列的一种）
# a=(1,2,3,4)
# b=a[1:3]
# print(b)


#选择语句 if
#顺序语句
#循环语句 for while do-while foreach



#if
#if [elif] [elif] [else]
#if 条件：
#     语句1
# elif    条件2：
#     语句2
# elif    条件3：
#     语句3
# else:
#     语句4
# def func(age):
    #1.检查参数的合法性
    #2.做方法该做的事情
    #3.输出合法的返回值



# tagetAge=18
# inputAge=-1
# inputAge=int(input("请输入您的年龄："))
# flag=inputAge>tagetAge
# flag1=inputAge>16
# print(flag) #数据的初始化或者定义
# if flag:
#     print("小哥哥")
#     print("你成年了，请负起责任，不要当巨婴")
#     if inputAge>50:
#         print("aaa:你真好看")
#     else:
#         print("bbb:你胖了")
#     print("FFFFF")
# elif flag1:
#     print("你做错事就会负刑事责任")
#     pass
# else:  #分析或处理数据
#     print("你还小，请不要喝酒")
#     pass #占位语句
# print("请吃饭了1....") 


#循环语句
#1.while
# '''
# while 条件:(条件为真执行循环体内容，知道pass2，只要满足while条件就会继续执行)
#     pass1(循环体内容)
# pass2
#break
#countiue
# '''

# l1=[1,2,3,4,5,6,7]
# index=0
# maxlength=len(l1)
# while index < maxlength :
#     print(l1[index])
#      index=index+1
#  print("over...")
# def tishi():
#     print("欢迎您！尊敬的用户！")
#     print("注意事项：")
#     print("1.取款请注意周围环境。")
#     print("2.在自动提款机取钱的时候，一定要小心，必须要防止别人偷窥您的密码。")
#     i = input("输入任意键跳转")
def jiemian():
    print("=" * 10, "欢迎你！", "=" * 10)
    print("=" * 10, " " * 4, "1.查询余额", " " * 4, "=" * 10)
    print("=" * 10, " " * 4, "2.存款", " " * 8, "=" * 10)
    print("=" * 10, " " * 4, "3.取款", " " * 8, "=" * 10)
    print("=" * 10, " " * 4, "4.退出", " " * 8, "=" * 10)
    # while True:
    #      oprt = input("请选择您要执行的操作")
    #     print("您选择了功能:",oprt)
    #     if oprt=='1':
    #         print('正在查询余额...')
    #         continue
    #     elif oprt=='2':
    #     print('正在取款...')
    #     elif oprt=='3':
    #         print('正在存款...')
    #      elif oprt=='exit':
    #         print('您选择了退出程序...')
    #         break
    # print("正在退出...")