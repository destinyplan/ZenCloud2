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
#打印出6*6的棋盘
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
'''
#输出num*num的棋盘
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
'''

strOrign="123456789ABCDEF"
strTarget='56'
result=len(strTarget)
beginIndex=0
endIndex=len(strOrign)-1
lowestIndex=-1
i=0
while i<=endIndex:
    if strTarget[0] == strOrign[i]:
        if result==1:
            print(lowestIndex)
        else:   
            oNextIndex=i+1
            tNextIndex=0+1
            while strTarget[tNextIndex]==strOrign[oNextIndex]:
                oNextIndex=oNextIndex+1
                tNextIndex=tNextIndex+1
                if oNextIndex>=len(strOrign):
                    break
                if tNextIndex>=len(strTarget):
                    break
            if tNextIndex==len(strTarget):
                lowestIndex=i
                break
            else:
                i=oNextIndex
                continue
    else:
        if i==endIndex:
            lowestIndex=-1
            break
    i=i+1
print(lowestIndex)