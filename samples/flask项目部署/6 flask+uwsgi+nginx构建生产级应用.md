### flask + uWSGI + nginx构建运行应用的生产环境
web应用框架，web服务器，web服务器兼反向代理。Flask 的内建简单服务器不适用于生产，只能用于测试。生产环境用uWSGI网络服务器，
nginx作为web服务器,功能更强大：
反向代理， 正向代理如VPN,代理客户端向服务器发送请求。反向代理，代理服务器接收请求并返回。多服务器下是必选项。
均衡负载，多个服务器情况下，分发请求。单服务器，对静态资源的处理，同时动态资源缓存等都很优秀
运维方面也很有优势。
nginx 和uWSGI以socket通信

#### 安装uWSGI
```
如果python3-devel没有安装，需要先安装
yum install python3-devel   #for python3.x  # 注意，使用Python3，需要安装的是python3-devel
yum install python-devel   #for python2.x  

#在Python虚拟环境中安装uwsgi
workon flask_env
pip install uwsgi


#uwsgi是否成功安装，测试如下
新建test.py文件， 代码：
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
    
<flask_env>uwsgi --http :8416 --wsgi-file test.py   #port :8416需要依据实际firewall打开port，如果网页浏览器能正常显示test.py内容，安装成功    
```

#### 在flask项目代码路径新建uwsgi_config.ini,配置如下
```
#http = 0.0.0.0:8416                        # 不用nginx服务器时的配置
socket = 127.0.0.1:8418                        # 使用nginx服务器时的配置
virtualenv = /root/.virtualenv/flask_env   # 运行环境
chdir = /root/workspace/forum_app/srv      # 项目代码路径
wsgi-file = app.py                         # flask app所在文件
callable = app                             # flask app名称
processes = 2                              # 开启进程数量
threads = 2                                 # 因为GIL，疑似无用
master = true                              # uWSGI服务器重启不会断开socket连接， 丢失现有请求

# 后台运行时的日志文件,当用supervisor监测程序运行时，该配置需要注释掉！！！！！！
daemonize = %(chdir)/../tmp/forum_app_uwsgi.log  

logger = internalservererror file:%(chdir)/../tmp/forum_app_uwsgi_error.log  # 500错误日志
pidfile = %(chdir)/../tmp/forum_app_uwsgi.pid    # 存储uwsgi运行时的pid的文件
stats = 127.0.0.1:8417                        # 本机上前端显示服务器工作状态的地址
```

#### 运行uwsgi
```
uwsgi --ini uwsgi_cinfig.ini  # 不使用nginx,则uwsgi_config.ini配置使用http,不用socket 
```
#### 

#### nginx配置
nginx默认被开启了，而测试页面也不是NGINX提示，而是CENTOS说明文件
```
[uwsgi]
#http = 0.0.0.0:8416                        # 不用nginx服务器时的配置
socket = 127.0.0.1:8418                        # 使用nginx服务器时的配置
```
在路径/etc/nginx/conf.d/下新建forum_flask_app_uwsgi.conf文件并配置，该路径下配置文件会被nginx自动读取
```
touch forum_flask_app_uwsgi.conf
vim forum_flask_app_uwsgi.conf

server {                          # 每行配置以分号(;)结尾，否则会出错
    listen 8416;                 # 客户端浏览器访问的端口
    server_name 149.28.88.203;   # 外网ip,也可以是域名
    root /root/workspace/forum_app/srv;   # 项目所在主目录
    charset utf-8;
    client_max_body_size 75M;
    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8418;    # 和uWSGI通信，重要！！！
    }
    
    location /static {                                    
        alias /root/workspace/forum_app/srv/static;  #静态资源路径
    }
}
```

至此，配置完成，重启nginx
```
nginx -s reload

# nginx  #启动
# nginx -s stop  #停止
```

http://nginx.org/en/docs/ngx_core_module.html#example
https://blog.csdn.net/besmarterbestronger/article/details/99443856
https://www.jianshu.com/p/aed6b5204225  多项目应用部署


#### supervisor
supervisor是在类Unix系统上运行的，能让用户控制复数进程的C/S客户端服务器系统。
是Linux/Unix系统下的一个进程管理工具，不支持Windows系统。它可以很方便的监听、启动、停止、重启一个或多个进程。
```
在主Python3环境安装supervisor
pip3 install supervisor

#创建配置文件
在 /etc/路径下添加文件夹，放置配置文件
mkdir /etc/supervisor
echo_supervisord_conf > /etc/supervisor/supervisord.conf
```
在该路径下新建文件夹programs,用来放个人配置文件，同时修改/etc/supervisor/supervisord.conf的	include区块
```
[include]
files = ./programs/*.ini
```
```
[:/etc/supervisor]mkdir programs
cd /programs
touch forum_app_uwsgi.ini
```
配置touch forum_app_uwsgi.ini如下：
```
[program:forum-app-python]
command=/root/.virtualenvs/flask_env/bin/uwsgi --ini /root/workspace/forum_app/srv/uwsgi_config.ini

directory=/root/workspace/forum_app/srv
user=root

autostart=true
autorestart=true
startsecs=3
stdout_logifle=/root/workspace/forum_app/tmp/uwsgi_supervisor_forum_app.log
stderr_logfile=/root/workspace/forum_app/tmp/uwsgi_supervisor_forum_app.err
```

至此，配置完成，启动supervisor即可,命令如下：
```
supervisord
```
supervisor控制命令sueprvisorctl,可顾名思义，可以命令如下
```
supervisorctl
>status
>restart $program_name
>stop $program_name
```

#### celery异步任务队列
安装celery, redis, memcached

安装celery
```
workon flask_env
pip install celery
```
安装Redis，yum install redis默认安装的版本太低(本虚拟机测试时是3.2版本，于是yum remove redis卸载了)
如果要安装最新的redis，需要安装Remi的软件源，使用Remi源安装redis
```
yum install -y http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
yum --enablerepo=remi install redis

service redis start   # or systemctl start redis

rpm -qa|grep redis
rmp -ql redis  #可以查看Redis安装时创建的文件

systemctl enable redis.service  #开机自启动 or chkconfig redis on
```

开启命令如下：
```
celery -A tasks worker.celery --loglevel=info
如下命令会报错
celery -A tasks worker --loglevel=info  # 会报错celery flask object has no attribute user_options， 因为tasks.py模块里的app命名
```
####memcached安装
```
yum install memcached     # 安装完后的配置文件在/etc/sysconfig/memcached

memcached -d -u root    # -d 后台运行
memcached-tool 127.0.0.1:11211 stats   #命令查看memcached状态
```




###错误集锦

####Unlinking stale socket /tmp/supervisor.sock   #stale陈旧
直接删掉supervisor.sock即可，命令如下：
```
unlink /tmp/supervisor.sock
```

#### FATAL Exited too quickly (process log may have details) 
如果uwsgi可以正常运行起来，uwsgi配置文件uwsgi_config.ini需要注释以下文件，使用logto的配置项输出日志
```
#daemonize = %(chdir)/../tmp/forum_app_uwsgi.log  
logto = %(chdir)/../tmp/forum_app.log
```

####踩坑，无意间建了两个.virtualenvs文件夹(存放建立的虚拟环境)，结果产生混乱，重新配置.bashrc里的虚拟环境路径，删除另一个，执行source .bashrc以生效

####多个supervisord在后台运行也会报错,可查找到直接杀掉进程
```
ps -aux | grep supervisord
kill -9 $PID
```

#### uwsgi --ini config.ini, supervisor -c config.conf

####其他supervisord控制程序运行错误，可能在于开了几个supervisor程序，相互排斥，无法绑定，ps -ef|grep supervisord 查看，kill -9 pid即可



