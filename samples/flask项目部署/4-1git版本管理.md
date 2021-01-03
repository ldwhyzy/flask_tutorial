###在本地开发机器上的准备工作

*1.导出开发环境
```
pip freeze>requirements.txt
```
*2.使用git管理代码版本，并在最终的上传到服务器，部署做准备
```
git init    #初始化，创建本地仓库
git remote add origin xxx.git   #和远端仓库建立连接（远端被命名为origin）
git add .  # 本地代码文件添加到暂存区
git commit -m '操作说明' #将暂存区内容添加到本地仓库
git pull origin master --allow-unrelated-histories  # 将远程仓库master中的信息同步到本地仓库master中,需要--allow-unrelated-histories参数，否则会合并失败
git push origin master   # 将本地仓库推送到远端
```

#### 关于git push
git push的一般形式为 git push <远程主机名> <本地分支名> <远程分支名> ，例如 git push origin master：refs/for/master ，即是将本地的master分支推送到远程主机origin上的对应master分支， origin 是远程主机名。第一个master是本地分支名，第二个master是远程分支名。

git push origin master
如果远程分支被省略，如上则表示将本地分支推送到与之存在追踪关系的远程分支（通常两者同名），如果该远程分支不存在，则会被新建
git push origin ：refs/for/master
如果省略本地分支名，则表示删除指定的远程分支，因为这等同于推送一个空的本地分支到远程分支，等同于 git push origin –delete master
git push origin
如果当前分支与远程分支存在追踪关系，则本地分支和远程分支都可以省略，将当前分支推送到origin主机的对应分支
git push
如果当前分支只有一个远程分支，那么主机名都可以省略，形如 git push，可以使用git branch -r ，查看远程的分支名
关于 refs/for：
refs/for 的意义在于我们提交代码到服务器之后是需要经过code review 之后才能进行merge的，而refs/heads 不需要

git push -u origin master
使用一次后，以后可直接用git push 代替git push origin master



###关于gitignore无效
如果某些文件已经被纳入了版本管理中，就算是在.gitignore中已经声明了忽略路径也是不起作用的，这时候我们就应该先把本地缓存删除，然后再进行git的push，这样就不会出现忽略的文件了。git清除本地缓存命令如下：
```
git rm -r --cached .  
git add .
git commit -m "update gitignore"
```


###关于删除分支信息
```
　1.切换到新的分支

git checkout --orphan latest_branch
　　2.缓存所有文件（除了.gitignore中声明排除的）

 git add -A
　　3.提交跟踪过的文件（Commit the changes）

 git commit -am "commit message"
　　4.删除master分支（Delete the branch）

git branch -D master
　　5.重命名当前分支为master（Rename the current branch to master）

 git branch -m master
　　6.提交到远程master分支 （Finally, force update your repository）

 git push -f origin master
```