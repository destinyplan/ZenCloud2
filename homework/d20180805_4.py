# 1.list.clear������ʵ�֣�
# �������壺clear() ������������б�
# list1=[1,2,3,4]
# list2=[]
# list1=list2
# print(list1)

#2.listOri.pop()
#�����б����һ��Ԫ�أ�����ɾ���б��ѵ�����Ԫ��
# list1=[1,2,3,4]
a=[1,2,3,4,5]
# len1=len(a)-1
# print(a[len1])

#3.list.sort
list1=[1,4,3,2,7,5,9,6,3]
i=0
j=0
k=[0]
while i<len(list1) :
     j=i+1
     while j<len(list1):
         if list1[i]>list1[j]:
             k[0]=list1[j]
             list1[j]=list1[i]
             list1[i]=k[0]
         j=j+1
     i=i+1
print(list1)

#4.list.reverse
#�б��е�Ԫ��˳��ת
list1=[1,2,3,4,5]
list2=list1[::-1]
print(list2)

#5.list.remove
#���������Ƴ��б���ĳ��ֵ�ĵ�һ��ƥ����
list=[1,2,3,4,5]
x = list.index(3)
del list[x]
print(list)

#6.list.insert
insert() �������ڽ�ָ����������б��ָ��λ�á�
list=[1,2,3,4,5]
x=[3]
y=2
A=list[0:2]
B=list[2:]
print(A+x+B)

#7.list.copy
#copy() �������ڸ����б�
x=[1,2,3,344,4,1.5,'aa','ab',' ',]
Len=len(x)
result=[]
i=0
result=[0 for i in range(Len)]
j=0
while i<Len:
    result[i]=x[j]
    i=i+1
    j=j+1
print(result)

#8.list.count()
#����ָ����Ԫ�����б��г����˶���
listOriginal=[1,2,3,344,'[',[1,1,4],1.5,'*','aa','ab',' ']
Len=len(listOriginal)
target='aa'
i=0
num=0
print(type(target))
while i<Len :      
    if type(target)==type(1):
        while i<Len:
            if listOriginal[i] == target:
                num+=1
            i+=1 
    elif type(target)==type([1]) :
        while i<Len:
            if listOriginal[i] == target:
                num+=1
            i+=1
    elif type(target)==type((1,2)) :
        while i<Len:
            if listOriginal[i] == target:
                num+=1
            i+=1
    elif type(target)==type(1.5) :
        while i<Len:
            if listOriginal[i] == target:
                num+=1
            i+=1
    elif type(target)==type('d') :
        while i<Len:
            if listOriginal[i] == target:
                num+=1
            i+=1               
print(num)
'''

#9.list.extend
x=[1,2,3,4]
y=[2,3,5]
len2=len(y)
i=0
while i<len2:
    x=x+[y[i]]
    i=i+1
print(x)  

#10.list.index





