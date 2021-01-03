###CENTOS下安装mysql


####查看centos 版本
```
cat /etc/redhat-release
```
####mysql安装
在CentOS中默认安装有MariaDB，这个是MySQL的分支，但为了需要，还是要在系统中安装MySQL，而且安装完成之后可以直接覆盖掉MariaDB
MariaDB数据库管理系统是MySQL的一个分支，主要由开源社区在维护，采用GPL授权许可。
开发这个分支的原因之一是：甲骨文公司收购了MySQL后，有将MySQL闭源的潜在风险，因此社区采用分支的方式来避开这个风险。
MariaDB的目的是完全兼容MySQL，包括API和命令行，使之能轻松成为MySQL的代替品。

### 如果打算使用MariaDB，安装如下，否则可跳过
```
yum install mariadb-server mariadb
```
mariadb数据库的相关命令是：
systemctl start mariadb  #启动MariaDB
systemctl stop mariadb  #停止MariaDB
systemctl restart mariadb  #重启MariaDB
systemctl enable mariadb  #设置开机启动

安装完成后，启动数据库,则可以正常使用MYSQL
```
systemctl start mariadb
mysql -u root -p
```

####下载安装MYSQL官方源
```
wget -i -c http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
yum -y install mysql57-community-release-el7-10.noarch.rpm
yum -y install mysql-community-server
```

####MySQL数据库设置
```
启动
systemctl start  mysqld.service

查看MySQL运行状态
systemctl status mysqld.service

MySQL正常运行，但首次进入MySQL还得先找出此时root用户的密码，通过如下命令可以在日志文件中找出密码
grep "password" /var/log/mysqld.log

mysql -uroot -p
password:

输入初始密码，此时不能做任何事情，因为MySQL默认必须修改密码之后才能操作数据库,
密码设置必须要大小写字母数字和特殊符号（*,/';:等）,不然不能配置成功,如AOOdai123*
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'new password';
```

####开启mysql的远程访问
执行以下命令开启远程访问限制（注意：下面命令开启的IP是 192.168.0.102，如要开启所有的，用%代替IP）
```
mysql> grant all privileges on *.* to 'root'@'192.168.0.102' identified by 'password' with grant option;
mysql> flush privileges; 
mysql> quit; 
```

####为Firewalls添加开放端口
firewall-cmd --zone=public --add-port=3306/tcp --permanent
firewall-cmd --reload

####更改MYSQL语言配置
登录mysql，输入status，查看配置
mysql> status; 

在/etc/my.conf中修改配置
```
vi /etc/my.conf
添加
[client]
default-character-set=utf8

[mysqld]下添加
character-set-server=urf8
collation-server=urf8_general_ci
```


链接https://blog.csdn.net/qq_36582604/article/details/80526287
https://www.cnblogs.com/starof/p/4680083.html

