# day2 之Linux命令  
## 1.clear  清屏（清当前屏幕，历史中还存在）  
## 2.id     查看当前用户的用户id和组id  
   >### id -a  输出所有不同的id信息 
   >### id -u  只显示用户id
   >### id -g  只显示组id  
## 3.su   切换用户  
   >### su root切换成root用户，需要密码  
   >### su 用户名 切换成普通用户  
## 4.man 查看linux中的命令帮助  
>man+命令 可查看到该命令的不同参数的含义，比--help更全面  
## 5.pwd显示当前路径   
>分为相对路径和绝对路径
>绝对路径是以/打头的路径
>相对路径是相对当前的路径
## 6.history查看历史操作过的所有命令    
## 7.ls 显示目标列表  
> * -a  列出所有文件，包括以 "." 开头的隐含文件    
> * -l 除文件名外，增加显示文件类型、权限、硬链接数、所
              有者名、组名、大小、及时间信息,即长格式
## 8.cd   用来切换目录  
>cd ~切换到家目录
>cd ..返回到上级目录
## 9.ll   列出用户的所有信息
>相当于ls -l

   

