#字典的简单预习
'''
people ={
    'kobe':{'phone':'12345','sex':'男'},
    'xiaoju':{'phone':'678910','sex':'女'}
}
labels ={'phone':'phone  number','sex':'sex'}
phone = 'phone'
sex = 'sex'
a = input("please input who you want to find:")
if a in people:
    print("{}'s {} is{},{} is {}.".format(a,labels[phone],people[a][phone],labels[sex],people[a][sex]))
'''
# append
'''
a = [1,2,3]
add = list(input("please input a num:"))
print('append result is:',a+add)
'''
#if的简单练习
'''
StaAge=18
inputAge=1
inputAge=int(input("please input age which you want to inquery:"))
if inputAge>StaAge:
    if inputAge<36:
        print("you are just a youth!")
    elif 36<=inputAge<60 :
        print("you are already a middle-age man!")
    elif 120>inputAge>=60:
        print("you are alreade a old man ,please pay attention your health")
    elif inputAge>120:
        print("you are not a people probablely!")
elif inputAge==StaAge:
    print("Congratulation!you are just growing up!")
elif inputAge<StaAge:
    if 0<inputAge<=1 :
        print("woo,you are a baby now!")
    elif 1<inputAge<5:
        print("you are a child now!")
    elif 5<=inputAge<12:
        print("you are a young-one!")
    elif 12<=inputAge<18:
        print("you are a early youth and will be grow up!")
'''
#while练习
'''
list1 = [1,2,3,4,5,6]
index = 0
while index <= len(list1)-1 :
    print(list1[index])
    index += 1
print("......")
'''
#while-if的练习
'''
while True :
    inquery=input("please choose a num(1-3,beyond 3 will exit!) what you want:")
    print("The number you choose is:",inquery)
    if inquery == '1':
        print("please choose 2!")
    elif inquery == '2':
        print("Welcome,Please continue:")
        while True :
            next=input("please choose function(a,b)(input exit to back) what you want to continue:")
            print("The surprise is :",next)
            if next == 'a':
                print("hhh,what a lucky pig")
            elif next == 'b':
                print("you should choose 'a'")
            elif next =='exit':
                print("bye...a foolish man!!")
                print("Will be come back the last!")
                break
    elif inquery == '3':
        print("you should choose '1'")
    else :
        break
print("So boring!!!")
'''
#棋盘
'''
while True :
    a=[]
    i=0
    list1 = int(input("please input the list what you want(input 0 to exit):"))    
    k=[0]*list1
    if list1 == 0:
        break
    while i<list1 : 
        a.append(k)
        i += 1
    print(list1,'*',list1,"'s chessboard is :")
    for b in a :
        for d in b :
            print(d,end=' ')
        print(' ')  
print("ending...")
'''
#乘法表
'''
a=[1,2,3,4,5,6,7,8,9]
print("乘法表:")
for b in a:
    for c in a :
        if b<=c:
            print(b,'*',c,'=',b*c,end='\t')
    print('')
'''
'''
a=[1,2,3,4,5,6,7,8,9]
print("乘法表:")
for b in a :
    for c in a :
        if b>=c :
            print(b,'*',c,'=',b*c,end='\t')
    print(' ')
'''
'''
a=[1,2,3,4,5,6,7,8,9]
print("乘法表:")
for b in a :
    for c in a :
        if c>=b :
            print(b,'*',c,'=',b*c,end='\t')
        elif c<b :
            print('        ',end='\t')
    print(' ')
'''
#str.endswith()
'''
Or = list(input("please input some word:"))
Tr = list(input("please input words which you want to find:"))
St = int(input("please input the index where you want to start:"))
En = int(input("please input the index where you want to end:"))
NewStr = Or[St:En+1]
NewStr2 = NewStr[::-1]
NewStr1 = Tr[::-1]
Len=len(NewStr1)
result=False
i,j=0,0
while i<Len :
    if NewStr2[i]==NewStr1[j]:
        result=True
    else:
        result=False
        break
    i+=1
    j+=1
print(result)
'''
#str.expandtabs()
'''
a='qwrtyqreet'
b='re'
i=0
c= b in a 
if c==False :
    print("-1")
else :
    while i<len(a) :
        if b[0]==a[i] :
            if 1==len(b) :
                result=i
                break
            else :
                x=0+1
                y=i+1
               # print(x,y)
                while b[x]==a[y] :
                    x+=1
                    y+=1
                    if x==len(b) :
                        break
                    if y==len(a) :
                        break
                if x==len(b) :
                    result=i
                    break
                else :
                    i=y
                    continue
        else :
            if i == len(a):
                print("-1")
                break
            i+=1
            continue
        i+=1
    print(result)
'''
#str.strip
'''
sta = "           adfdf fadsf            "
Len=len(sta)
i=0
while i<=Len:
    if sta[i]!=' ':
        NewStr=sta[i:]
        j=0
        while j<=Len:
            if sta[Len-j-1]!=' ':
                result=NewStr[:j-1]
                print(result,end="*")
                break
            j+=1
        break
    i+=1
'''
#list.extend()
'''
a = [1,2,3,4,5]
b = ["a","f"]
#a.extend(b)
a=a+b
print(a)
'''