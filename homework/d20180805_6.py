#listOri.append（5）#c = a + b
#1.将两个列表同时添加到同一个列表中

listOri=[2312,23121,31231]
listInsert=[1232312323,3123]
listC=[listOri+listInsert]
print(listC,listC==listOri+listInsert)
# listOri.clear（）＃
listOri=[1,11,2,2,3,3,4,4]
list1=[]
Len=len(listOri)
listOri=list1
print(listOri)
# listOri.copy（）＃
# listOri.count（'a'）＃
# listOri.extend（[3]）
# listOri.index（3,0,8）＃看贺同学的有些没看懂；函数意思大概明白

# listOri.insert（0，[1,3]）
# listOri.pop（）
listOri=[1,2,3,4,5]
Len=len(listOri)-1
print(listOri[Len])
# listOri.remove（2）
# listOri.reverse（）#a = []
listOri=[1,2,3,4,5]
a=[listOri[::-1]]
print(a)
# listOri.sort（）＃

# strOri.center（10， '*'）
# strOri.count（ 'a'）的
# strOri.endswith（）
# strOri.find（ 'a'）的
str1="dsadsdaseaa"
str2="sd"
if str1.find(str2):
    print("Yes")
else:
    print("No")
#方法二 利用idex函数...如果找到则返回值为str2在str1中出现的位置下标，否则返回出一个异常
str1 = "jintianquweinanle !!!!"
str2 = "tian"
print (str1.index(str2))
print (str1.index(str2,3))
print (str1.index(str2,9))
# strOri.isalnum（）
# strOri.isdigit（）
# strOri.istitle（）
# strOri.isupper（）
# strOri.join（[1,2,3,4]）
# strOri.ljust（10， '^'）
# strOri.lower（）
# strOri.replace（ 'WWE'， 'NBA'，3）
# strOri.rindex（）
# strOri.split（SEP = 'Y'，maxsplit = 3）
# strOri.startswith（）
# strOri.swapcase（）
# strOri.title（）
# strOri.zfill（）

