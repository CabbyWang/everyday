***
#### github多账号配置
##### 1. 生成ssh密钥
````
 ssh-keygen -t rsa -C "xxx@163.com"             # -C后面为注释内容
````
````
 ssh-add ~/.ssh/id_rsa_xx         # 让SSH识别新的私钥
````
 出现 `Could not open a connection to your authentication agent` 错误
````
 ssh-agent bash             # 类似刷新操作？
 ssh-add ~/.ssh/id_rsa_xx   # 添加文件到ssh
````


##### 2. 修改.gitconfig文件
````python
 touch config         # 创建config文件

# user1
 Host git1                # 用来区分和替换Host名
    HostName github.com      # 服务器域名
    User git 
    IdentityFile ~/.ssh/id_rsa_xx

# user2
 Host git2                # 用来区分和替换Host名
    HostName github.com       # 服务器域名
    User git 
    IdentityFile ~/.ssh/id_rsa_yy
````
 ![test](https://cl.ly/3L39123U2K2h)


##### 3. 将各自生成的pub文件内容复制到github或gitlab中的ssh密钥中

##### 4. 测试
~ssh -T git@对应的服务器地址
~~~~
ssh -T git@git1
ssh -T git@git2
~~~~
出现`Hi username. You've successfully autenticated...`成功

**其他**
~~~~python
git config --global unset user.name 
git config --global unset user.email   # 可以通过修改~/.gitconfig文件实现

git config [--global] user.name "my_name"
git config [--global] user.email "my_email"
~~~~
***

#### git基本操作
##### 1. git命令行
````
mkdir   # 创建目录
cd ..   # 返回上一级
pwd     # 显示当前目录
vi      # 退出时（shift z z 或 : x）
````

##### 2. 常用操作
直接将远程库克隆到本地
````
git clone <git@github...>       # 克隆
````
创建本地库，然后与远程库关联
````
git init                     # 将目录变成可以管理的仓库
git remote add origin(远程库,默认叫法) <git@github...>  # 本地关联远程库
git add <xx.txt>             # 添加暂存区
git commit -m "xxx"          # 提交到本地仓库(引号为注释)
git push                     # 推送到远程分支
````
创建本地库，然后推送到远程分支
````
git push -u origin <master>  # 本地库推送到远程库
````

分支(branch)
````
git branch
git branch -a           # -a 为all
git branch <dev>
git branch -D <dev>     # 强制删除dev分支
git branch -d <dev>     # 删除dev分支
git checkout -b <dev>   # 创建+切换到分支dev, 相当于下两句
git checkout <dev>
git checkout <file>     # 还原文件,丢弃修改

````
````
git log                     # 查看提交记录
git log --pretty=oneline    # 显示为一行
git relog                   # 查看命令记录
````

````python
git rm xxx
git diff
git diff --cached         # index中的diff
git cherry-pick commitID  # 把commitID提交当前分支上面(最好用merge)
git revert                # 还原一个版本的修改(必须提供一个具体的git版本号)
git reset                 # 将当前的工作目录完全回滚到指定的版本号
git rebase
````

````
git stash                           # 将当前未提交的工作存入Git工作栈中
git stash list                      # 查看暂存
git stash apply stash@{1}/stash pop
git stash clear
````
````
git tag      # 查看tag
git tag -a v1.0.0 -m "release- 1.0.0发布"
git checkout tagname
git tag -d v1.0.0  # 删除tag
git push origin v1.0.0  # 发布tag
git push origin -tags  # 发布所有tag
Git push origin :refs/tags/tagname   # 删除远程tag
git tag -a v1.0.0 commitID  # 制定commitID生成tag
````

```
git fetch       # 从远程获取最新版本到本地，并创建一个分支，不会自动merge
git merge       # git fetch + git merge
````

commit后发现遗漏文件解决办法(--amend)<br>[https://www.atlassian.com/git/tutorials/rewriting-history](https://www.atlassian.com/git/tutorials/rewriting-history)
```python
git add xx
git commit -m 'aa'
git add yy
git commit --amend -m 'aa and bb'  # commit注释从'aa'变为'aa and bb'
git commit --amend --no-edit       # 不修改
```

##### 3.工作流

##### 4.git hook
