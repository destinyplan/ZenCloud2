#list.append
'''
origList=[1,2,3,4,5]
newList=[6]
len=len(origList)
i=0
result=[]
result=[0 for i in range(len+1)]
indexOrig=0
while True:
    if i<len:
        result[i]=origList[indexOrig]
        indexOrig=indexOrig+1
    i=i+1
    if i==len:
        result[i]=newList
        break
print(result)
'''

#list.clear
'''
origList=[1,2,3,4,5]
newList=[]
origList=newList
print(origList)
'''

#list.copy
'''
origList=[1,2,3,'12','sdf',4,[1,2]]
newList=[]
newList=origList
print(newList)
'''

#list.count

#list.extend
'''
origList=[1,2,3,4,5]
newList=[6,7,8]
Len=len(origList)
LenList=len(newList)
i=0
result=[]
result=[0 for i in range(Len+LenList)]
indexOrig=0
indexInsert=0
while i<len(result):
    if i<Len:
        result[i]=origList[indexOrig]
        indexOrig=indexOrig+1
    if i>=Len and i<len(result):
        result[i]=newList[indexInsert]
        indexInsert=indexInsert+1
    i=i+1
print(result)
'''

#list.insert
'''
origList=[1,2,3,4,5,6]
insert=[2]
a=int(input("please input a num:"))
newList1=origList[:a]
newList2=origList[a:]
newList=newList1+insert+newList2
print(newList)
'''

#list.pop
'''
origList=[1,2,3,4,5,8]
a=len(origList)-1
print(origList[a])
'''

#list.remove
'''
listOrig=[1,2,3,4,5,6,7]
rm=[2]
i=0
while i<len(listOrig) :
    if listOrig[i]==rm[0]:
        newList1=listOrig[:i+1]
        newList2=listOrig[i+1:]
        a=newList1.pop()
        print(newList1+newList2)
        break
    i=i+1
'''

#list.reverse
'''
origList=[2,5,4,7,8,9,3]
newList=origList[: :-1]
print(newList)
'''

#str.endswith
'''
strOrig="asdfghjkxcvbnmwerty"
strTarget="jk"
beginIndex=0
endIndex=8
result=False
newStr=strOrig[beginIndex:endIndex]
i=len(strTarget)-1
index=len(newStr)-1
while i>=0:
    if strTarget[i]==newStr[index]:
        result=True
    else:
        result=False
        break
    i=i-1
    index=index-1
print(result)
'''

#str.find
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
            print(i)
            break
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
'''

#str.strip
'''
originalStr="      234456  bnmvbn      "
resultStr=''
beginIndex=0
endIndex=len(originalStr)-1
i=0
while i<=len(originalStr):
    if originalStr[i]!=' ':
        beginIndex=i
        break
    i=i+1
j=0
while j>=0:
    if originalStr[j]!=' ':
        endIndex=j
        break
    j=j-1
resultStr=originalStr[beginIndex:endIndex+1]
print(resultStr)
'''
