#1.函数的定义
#2.异常的捕获处理---程序的健壮性（鲁棒性）

#1.函数的定义
#参数个数>=0
#不一定有返回值
#命名规则:动词+名词(DoSomething)

'''
#name,age 形参(形式参数)
def MethodName(name,age):
    '这里是注释'
    result=1
    print(name,age)
    return 1


#调用方式1
MethodName('rong',18)#传入实参
#调用方式2
MethodName(age=18,name='qin')#传入实参
print('asdfghjk')

a=4
b=a
print(b)

c=MethodName
c('qiang',99)

#函数嵌套
def GoMyHome():
    def OpenGirlRoom():
        print('This is GirlRoom')
    def OpenBathRoom():
        def CleanYourFace():
            print('your face is clear')
        print('This is BathRoom')
        CleanYourFace()

    print('This is livingroom')
    OpenBathRoom()
    

GoMyHome()
'''

#2异常
#raise+异常类型
# a=input("a=")
# b=input("b=")
# c=a*b
# raise TypeError
# print(c)

#如何捕获异常
# try:
#     pass
# except TypeError:
#     pass
# except Error:
#     pass
# else:
#     pass
# finally:
#     pass
a='a'
b='cc'
try:
    c=a*b
    print(c)
except ValueError:
    print('渣渣强')
except TypeError:
    print('你输入的是字符串,两个字符串不能相乘')
    c=int(a)*int(b)
    print(c)
except:
    print('ss')
else:
    print('啥错误都木得')
finally:
    print('终于到这里了')

print('this is End')



#1,没有函数
#顺序，更符合机器
# while True
# if
# for
#     for

#2,学了函数
#更符合人的思维

#3，对象Class
#就是人
'''
1.拿一副棋
2.下棋
3.有人赢了
fiveChess=FiveChess()
where True:
    if fiveChess.isPlayer1
        fiveChess.Player1XiaQi(1,2)
    else:
        fiveChess.Player2XiaQi(1,2)
'''