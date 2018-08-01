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
# a= [1,2,3,5,5,4,3,6,3,7,3,8,4,2]
# b= a.index(3)
# print(b)
# c= a.index(3,3,)
# print(c)
# d= a.index(3,7,)
# print(d)
# print(e)
# print(a.pop(8))
# print(a)
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
'''
list1 = [1,2,3,4,5,6]
index = 0
while index <= len(list1)-1 :
    print(list1[index])
    index += 1
print("......")
'''
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

a=[]
while True :
    a.clear()
    i=0
    list1 = int(input("please input the list what you want(input 0 to exit):"))
    while i<list1 :   
        k=[]
        j=0
        while j<list1 :
            k.append(0)
            j += 1
        a.append(k)
        i += 1
    print(list1,'*',list1,"'s chessboard is :")
    for b in a :
        for d in b :
            print(d,end=' ')
        print(' ') 
    if list1 == 0:
        break
print("ending...")

'''
a=[1,2,3,4,5,6,7,8,9]
print("乘法表:")
for b in a:
    for c in a :
        if b<=c:
            print(b,'*',c,'=',b*c,end='\t')
    print(' ')
'''