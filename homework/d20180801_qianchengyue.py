########
# l1=[]
# i=0
# a='q'
# while True:
#     qmax=int(input('请输入棋盘行数:'))
#     if type(qmax)==type(i):
#         while i<qmax:
#             l1.append(0)
#             i=i+1       
#         l2=[l1]*qmax
#         for line in l2:
#             for key in line:
#                 print(key,end=' ')
#             print(' ')
#     elif type(qmax)==type(a):
#             print('exit...')
#             break
#     else:
#         pass
########以上代码有问题 

l1=[]
while True :
    l1.clear()
    i=0
    qmax = int(input("请输入棋盘行数(输入0来退出):"))
    while i<qmax :   
        k=[]
        j=0
        while j<qmax :
            k.append(0)
            j=j+1
        l1.append(k)
        i=i+1
    print(qmax,'*',qmax,"表格如下:")
    for line in l1 :
        for key in line :
            print(key,end=' ')
        print(' ') 
    if qmax == 0:
        break
print("正在关闭系统。。。")