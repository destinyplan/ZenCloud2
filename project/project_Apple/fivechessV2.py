#五子棋V2 by ZenCloud2 All

def PrintChessMap(listmap):
    '''打印棋盘'''
    print('*'*20)
    for line in listmap:
        for key in line:
            print(key,end=' ')
        print('')
    print('*'*20)

def AI(listmap):
    '''裁判员'''
    return False
    
chessMap=[]
size=int(input('请输入棋盘大小:'))
#打印棋盘
mapKey=['-']#[-,-,-,-,-,-]
i=0
while i<size:
    chessMap.append(mapKey*size)
    i+=1

PrintChessMap(chessMap)

isPlayer1=True
while True:
    #下棋
    if isPlayer1:
        #1下棋
        x=int(input('玩家1请输入行数:'))
        y=int(input('玩家1请输入列数:'))
        chessMap[x][y]='x'
        isPlayer1=False
    else:
        #2下棋
        x=int(input('玩家2请输入行数:'))
        y=int(input('玩家2请输入列数:'))
        chessMap[x][y]='o'
        isPlayer1=True

    #打印棋盘
    PrintChessMap(chessMap)

    #有没有人赢
    hasWin=False
    hasWin=AI(chessMap)
    if hasWin:
        break
    