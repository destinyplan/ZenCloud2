#while循环体
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
    else:
        print("输入有误，请重新输入！")
print("Game over")

#棋盘
l1=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
for a in l1:
    print(0,0,0,0,0,0,sep=' ',end='\n')


#规定棋盘大小
while True:
    oper=input("size=")
    if oper=='q':
        break
    num=int(oper)
    if num:
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
