###CENTOS下安装Python

####生成requirement.txt文件
```
pip freeze>requirements.txt
type requirements.txt   # print the content of requirements.txt
```
####安装依赖，Python
1.更新yum源
```
yum update   # 更新yum源
```
2.参照Python安装说明https://devguide.python.org/setup/#build-dependencies 
```
yum install yum-utils
yum-builddep python3
```
如果提升权限不足，命令如下
```
sudo yum install yum-utils
sudo yum-builddep python3
```
安装完后，需要在~目录下建立.pip文件夹，创建pip.conf文件，设置[list]format=columns， 否则pip3会提示

```
mkdir ~/.pip/
cd ~/.pip
touch pip.conf
vi pip.conf

在pip.conf文件中添加：
[list]
format=columns
```
3. 在<em>主Python环境</em>中安装virtualenvwrapper, 创建Python虚拟环境
>安装virtualenvwrapper
```
pip3 install virtualenvwrapper
```
>查看python3的文件和virtualenvwrapper.sh的路径
```
which python3
/usr/bin/python3

find / -name virtualenvwrapper.sh
/usr/local/bin/virtualenvwrapper.sh
```
>修改当前用户的配置文件~/.bashrc ，设置完需要重新登录，让其生效
```
ls -a
vi .bashrc

末尾添加 (=两边不能有空格，否则.bashrc报错)
export WORKON_HOME=#HOME/Envs    #设置virtualenv的统一管理目录，以后创建的虚拟环境都放在这
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'    #添加virtualenvwrapper的参数，生成干净隔绝的环境 
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3             #指定python解释器的本体 
source /usr/local/bin/virtualenvwrapper.sh      #执行virtualenvwrapper安装脚本
```

#### virtualenv: error: unrecognized arguments: --no-site-packages错误
使用virtualenv --version，看到自己的版本大于20，就可以在.bashrc中将如下这段删除：
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'

运行.bashrc，使设定生效
source .bashrc


####virtualenvwrapper使用
#####在物理环境下操作
# 创建并激活虚拟环境
mkvirtualenv 虚拟环境名

# 切换虚拟环境
workon 虚拟环境名

# 退出虚拟环境
deactivate

# 删除虚拟环境
rmvirtualenv 虚拟环境名

# 查看所有的虚拟环境
lsvirtualenv


####在虚拟环境下操作
# 切换到虚拟环境的目录
cdvirtualenv

# 切换到虚拟环境的site-packages目录
cdsitepackages

# 查看虚拟环境site-packages目录的文件
lssitepackages


####以下为virtualenv的使用可不看
```
virtualenv <env_name>  #执行后，在当前目录生成一个env_name的路径(文件夹)

#如果系统中不止一个版本的Python，--Python参数指定Python版本
virtualenv --Python=/usr/bin/pyton3 <env_name>  #执行后，在当前目录生成一个env_name的文件夹,版本与/usr/bin/pyton3版本相同

#在env_name路径启动虚拟环境
source bin/activate
#退出虚拟环境
deactivate 
```

