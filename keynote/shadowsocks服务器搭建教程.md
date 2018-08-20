# Shadowsocks服务器搭建

1. yum install epel-release
2. yum install python-pip
3. pip search shadow;pip install shadowsocks
4. 写配置文件
```
{
"server":"0.0.0.0",
"server_port":8038,
"local_address":"127.0.0.1",
"local_port":1080,
"password":"root",
"method":"rc4-md5",
"udp_timeout":60,
"fast_open":false
}
``` 
5. ssserver -c ss/config.json -d start
6. ssserver -c ss/config.json -d stop
7. log日志位置：/var/log/shadowsocks.log
8. 服务自启动
9. PC和安卓apk地址：  
**windows**:<https://blog.csdn.net/junbujianwpl/article/details/78639247>  
**android**:<https://github.com/shadowsocks/shadowsocks-android/releases>
10.ios,需要美区apple id登录app store，下载wingy

## 附录：
* <http://hostdare.com/>
* <https://www.zhujiceping.com/>
* <http://www.vpsdx.com/>

## 参考：
* <https://www.cnblogs.com/zhangqiuchi/p/8454241.html>
* <https://www.jianshu.com/p/824912d9afda>
* <https://segmentfault.com/a/1190000012910949>
* <https://blog.csdn.net/sjtu_mc/article/details/79207427>
* <https://blog.csdn.net/asdfg6541/article/details/78956480>
* <https://blog.csdn.net/junbujianwpl/article/details/78639247>



