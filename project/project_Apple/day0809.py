'''
#list.apppend(object)
list2=[1,2,3]
a=5
b='ty'
c=['a','b']
#list2.append(a)#[1,2,3,5][1,2,3,'ty'][1,2,3,['a','b']]
#analysis
#1,创建一个新列表，长度为n+1，列表元素都为0
#2，把原来列表的所有元素依次赋值到新列表的对应元素 new[i]=old[i]
#3,只需要将new[-1]=a
#4,list2=new

#1
n=len(list2)+1
newlist=[0]*n
#2
i=0
while i<len(list2):
    newlist[i]=list2[i]
    i=i+1
#3
newlist[-1]=c
#4
list2=newlist
#打印结果
print(list2)
'''


#29-1 listOri.count('a') 
'''
listOri=[1,2,3,4,5,6,2,8,2,4]
num = listOri.count(2)
numNone=listOri.count(99)
#analysis:在原列表中查现的次数,要是没查到,则结果为0
#1,对原列表进行遍历 while | for
#1.1,对遍历到的元素与给定元素进行比较 if
#1.1.1 比较结果相等:次数+1
#1.1.2 不相等:忽略,继续循环
#2,打印结果

#do-something
def MyStrCount(listOld,key):
    '这是自己实现的列表的count方法,有一个参数,参数就是要查询的元素'
    resultNum=0
    for elem in listOld:
        if elem == key:
            resultNum+=1

    return resultNum

print('i am in outside1')
num2 = MyStrCount(key=2,listOld=listOri)
num99 = MyStrCount(listOri,99)
num8 = MyStrCount(listOri,8)
print('i am in outside2',num2,num99,num8)
'''

#29-2 listOri.index(1,2,3)
'''
listOri=[1,3,2,3,4,5,6,2,8,2,4]
# index2 = listOri.index(2,0,9)
# index99=listOri.index(99)
#analysis :在列表给定的范围遍历查找给定的key,若存在,返回第一个查到的值的下表,若不存在,报错ValueError
#1,定义一个结果下标值,初始值为-1
#2,遍历列表的指定范围,两种情况1,全列表.2,列表的切片
#2.1 比较每次遍历到的值，if key==值
#2.1.1  相等:直接返回该值的下标 ，结果下标值=当前下标。return 结果下标值
#2.1.2  不等:继续循环
#3.循环结束:if 结果下标值没有发生改变 打印异常ValueError

def MyStrIndex(listOld,key,Bindex,Eindex):
    resultIndex=-1
    lenListOld=len(listOld)
    listCheck=[]
    #1
    if Bindex==0 and Eindex==lenListOld-1:
        listCheck=listOld
    else:
        listCheck=listOld[Bindex:Eindex+1]
    #2
    i=0
    while i<len(listCheck):
        if listCheck[i]==key:
            resultIndex=i
            return resultIndex
        else:
            pass
        i+=1
    #3
    print("ValueError")
    raise ValueError

index2=MyStrIndex(listOri,2,0,1)
print(index2)
'''

#29-3 listOri.sort()
#analysis:对列表进行升序排列
#1.
#2.
#3.
#code...
#排序算法---冒泡排序
#1.依次对元素进行比较,每次比较相邻两个元素,交换大小位置,
# 第一循环结束后这个无序列表中最大的元素就会被扔到列表末尾
#2.对1生成的新列表的n-1个元素进行1的比较
#3，
#4
#...
#n
#coding...
listOri=[8,5,1,2,9,7,4,3,6,0]
#listOri.sort#[1,2,3,4,5,6,7,8,9]
def MyListPopSort(listOld):
    i=0
    count=0
    while i<len(listOri):
        j=0
        while j<len(listOri)-i-1:
            count+=1
            if listOri[j]>listOri[j+1]:
                #交换以下j和j+1两个位置
                temp=listOri[j]
                listOri[j]=listOri[j+1]
                listOri[j+1]=temp
            j+=1
        # print(i+1,listOri)
        i+=1
    return listOld

listNew=MyListPopSort(listOri)
print(listNew)


#29-4 strOri.center(10,'*')
'''
strOri='123'
strOri.center(10,'*')#--> '****123***'
#analysis :创建一个长度为指定长度的*字符串,将源字符替换到中间
#1,创建一个长度为给定长度的字符串,所有字符都是给定的符号'**********'
#2,找到这个字符串需要替换的位置,开始下标和结束下标
#3,从下标开始的位置遍历到下标结束的位置
#3.1 每次将遍历的到的元素改为源字符串对应位置
#4 循环结束，将新字符串打印
def MyStrCenter(strOld,length,char):
    newStr=''
    #1
    resultList=[char]*length#[*,*,*,*,*,*,*,*,*,*]
    #2
    Bindex=(length-len(strOld))//2
    Eindex=Bindex+len(strOld)
    #3
    i=Bindex
    while i<Eindex:
        resultList[i]=strOld[i-Bindex]
        i+=1
    #4
    
    newStr="".join(resultList)
    return newStr

newS=MyStrCenter(strOri,10,'+')
print(newS)
'''

#29-5 strOri.split(sep='y',maxsplit=3)
# ll = strOri.split('1',maxsplit=2)
# print(ll)
#analysis :将源字符串以指定分隔符分割指定次数,生成一个列表,列表内存储切割生成的各个元素
#1,创建一个空列表
#2,对原字符串进行遍历
#2.1,若遍历到的元素是分隔符, if
#2.1.1,是分隔符,将分隔符之前的元素当成一个字符串，追加到空列表之后，list.append(str[Bindex:Eindex])
#2.1.2,不是分隔符，记录（开始，结束）下标
#3, 循环结束，return 列表
'''
strOri='a12a234a'#'12a234a56a34'#
def MyStrSplit(strOld,key,maxSplit):
    #1
    resultList=[]
    #2
    i=0
    splitNum=0
    Bindex=0
    Eindex=0
    while i<len(strOld):
        #2.1
        if strOld[i]==key:
            if splitNum<maxSplit:
                resultList.append(strOld[Bindex:i])
                splitNum+=1
            else:
                resultList.append(strOld[Bindex:])
                return resultList
            Bindex=i+1
            Eindex=i+1
        else:
            Eindex=i
        i+=1
    #3
    return resultList

listR = MyStrSplit(strOri,'a',2)
print(listR)
'''

#29-6 strOri.title()
#analysis:将所有空格之后的第一个非空格字母大写,输出新str
#1,字符串转换成列表
#2,遍历列表
#2.1:扫描到非空格的第一个字符(当前扫描的是不是小写字母and i-1是不是空格) if
#2.1.1:满足条件:小写-》大写
#2.1.2:不满足:pass继续下次循环
#code...
'''
strOri=" this 5 is a dog 4"#"This Is A Dog"
def MyStrTitle(strOld):
    resultStr=''
    #1
    listTemp=list(strOld)
    #2
    i=0
    #a-z A-Z 空格 ord('a') chr(97)
    while i<len(listTemp):
        currentCode=ord(listTemp[i])
        preCode=0
        if i>0:
            preCode=ord(listTemp[i-1])
        else:
            preCode=32
        if (currentCode>96 and currentCode<123) and preCode==32:
            listTemp[i]=chr(currentCode-32)
        i+=1
    
    resultStr=''.join(listTemp)
    return resultStr

strTitle=MyStrTitle(strOri)
print(strTitle)
'''


#1.异常的捕获处理---程序的健壮性（鲁棒性）
#2.函数的定义