# 20180725作业  
## 1.mkdir:新建文件夹  
>Eg :mkdir a a/a a/a/a
## 2.touch:新建空文件  
>Eg :touch 1.txt 2.txt
## 3.echo :新建一个非空的文件  
- \> 输出重定向
- <  输入重定向
>\>一个表示覆盖内容  
>\>>两个表示添加内容  
>>Eg: echo "afaf" > 1.txt      echo "afadfaf" >> 1.txt
## 4.tree:某个文件夹以树状的形式打印出来  
## 5.rmdir :删除空文件夹  
>-p:如果目录是由多个路径组成,则从最后一个路径进行依次删除  
>-v:显示删除的过程信息  
>>rmdir -vp b/b/b
## 6.rm : 删除文件及文件夹  
>-f :强制删除  
>-i :进行确认信息  
>-r/R :递归的移除  
>-v :显示删除信息  
>>Eg : rm -rivf b/b/2.txt
## 7.cp : 复制文件及文件夹  
>-f :删除存在的目标文件  
>-i :进行确认信息  
>-r/R :递归的复制目录文件  
>-v :显示复制信息   
>>Eg:cp 1.txt b/2.txt -f
## 8.mv : 移动或者重命名文件  
>Eg:mv 1.txt ahhh/ :将1.txt 移动到ahhh下面  
>Eg:mv 1.txt 2.txt :将1.txt 改名为2.txt   
## 9.cat more less head tail top :查看文件  
- cat :输出文件的所有内容,直接显示到文件最后  
- more/less :从文件开始输出,一次显示文件的一部分  
- head/top:输出文件的开始部分  
- tail : 输出文件的末尾部分  

