'''
while True:
    oprt = input("请选择需要执行的选项:")
    print("你选择了选项:",oprt)
    if oprt == "1":
        print("吃饭")
    elif oprt == "2":
        print("睡觉")
    elif oprt == "3":
        print("打豆豆")
    elif oprt == "exit":
        print("正在退出")
    else:
        print("输入错误，请重新输入")
print("End")
'''

'''
l2 = []
j = 0
while j<6:
    l1 = []
    i = 0
    while i<6:
        l1.append(0)
        i = i+1
    l2.append(l1)
    j = j+1

for a in l2:
    for b in l1:
        print(b,end=" ")
    print(" ")
'''


while True:
    oper = input("Please input the size of chessmap:")
    if oper == "q":
        print("exit")
        break
    num = int(oper)
    if num:
        chessmap = []
        j = 0
        while j<num:
            k = []
            i = 0
            while i<num:
                k.append(0)
                i = i+1
            chessmap.append(k)
            j = j+1
        for a in chessmap:
            for c in a:
                print(c,end=" ")
            print(" ")
