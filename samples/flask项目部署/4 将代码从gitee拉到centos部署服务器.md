###在服务器上部署代码
这里的服务器是为了区别开发机器，指最终代码在该机器上作为项目运行。将代码从gitee上拉到服务器，需要ssh公钥验证，先生成ssh key，再用git操作

#### 生成ssh key
ssh 存放位置~/.ssh/
```
ls ~/.ssh/
ssh-keygen -t rsa -b 2048 -C "emailaddress" # 用个人邮箱标识，随后会提示生成文件名和该ssh的使用密码，可默认，直接回车跳过
```

###添加ssh key到ssh-agent
```
eval `ssh-agent`  #测试是否启用
ssh-add ~/.ssh/xxx  #xxx为上面生成命令时使用的命名

如果报错 Could not open a connection to your authentication agent.执行以下：
ssh-agent bash   
再执行：
ssh-add ~/.ssh/xxx
```

###添加ssh public key到gitee
将public key文件里的key直接拷贝，粘贴到gitee相应设置即可。至此，可在服务器上使用git实现代码管理
这里我是使用WinSCP将public key文件从虚拟主机传到个人电脑，在将其拷到git设置。


####在服务器上创建仓库
```
git init
git remote add origin git@gitee.com:xxxxxxxxxx.git   #关联gitee上的git仓库
git pull git@gitee.com/xxxxxxxxxx.git    #将代码拉到本地
```


### 错误分析

#### 创建ssh key后仍出现permission denied错误，可参照本地配置多个ssh key
```
在~/.ssh目录下新建名称为config的文件（无后缀名）。用于配置多个不同的host使用不同的ssh key，举例如下：
# gitlab
Host gitlab.com
    HostName gitlab.com
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/gitlab_id-rsa
# github
Host github.com
    HostName github.com
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/github_id-rsa
  ​
# 配置文件参数
# Host : Host可以看作是一个你要识别的模式，对识别的模式，进行配置对应的的主机名和ssh文件
# HostName : 要登录主机的主机名
# User : 登录名
# IdentityFile : 指明上面User对应的identityFile路径

```

#### git pull /git clone区别
从远程服务器克隆一个一模一样的版本库到本地,复制的是整个版本库，叫做clone.（clone是将一个库复制到你的本地，是一个本地从无到有的过程）
从远程服务器获取到一个branch分支的更新到本地，并更新本地库，叫做pull.（pull是指同步一个在你本地有版本的库内容更新的部分到你的本地库）
git pull = git fetch + git merge，git fetch更安全一些


#### Git 提示fatal: remote origin already exists 错误
先删除远程 Git 仓库,再添加远程 Git 仓库
```
git remote rm origin
git remote add origin git@github.com:FBing/java-code-generator

如果执行 git remote rm origin 报错的话，我们可以手动修改gitconfig文件的内容
vi .git/config
```

#### Git 提示Please tell me who you are,提示创建email和name
```
git config --global user.email "xxxxx@xxx.com"
git config --global user.name "xxxxx"

查看用户信息
git config --global -l
```

### 在MySQL创建新数据库
```
create database forum;
CREATE DATABASE IF NOT EXISTS yourdbname DEFAULT CHARSET utf8 COLLATE utf8_general_ci; # 已配置，不用再
```

