###CENTOS下安装openssh,以方便远程操作服务器
如下服务器是 实际的VPS服务器

####检查CentOS是否安装了openssh
```
yum list installed | grep openssh-server
```

####没有则安装openssh
```
yum install openssh-server
```

####如果已经安装，在/etc/ssh/目录下的sshd服务器配置文件，取消如下注释(去掉#)
```
vi /etc/ssh/sshd_config

设置如下
Port 22
PermitRootLogin yes
```
####运行sshd服务, 并检查是否开启
```
service sshd start
ps -e | grep sshd    # netstat -an | grep 22
systemctl enable sshd.service #设置开机启动
```



###开发机上使用Xshell或 WinSCP(传输文件) + PuTTY（登录到服务器）操作远端服务器

####PuTTY设置RSA验证登录，取消用户名，密码登录
#####RSA privatekey publickey生成，上传publickey到远端服务器

