***
#### github多账号配置
##### 1. 生成ssh密钥
~~~~
 ssh-keygen -t rsa -C "xxx@163.com"             # -C后面为注释内容
~~~~
~~~~
 ssh-add ~/.ssh/id_rsa_xx         # 让SSH识别新的私钥
~~~~
 出现 `Could not open a connection to your authentication agent` 错误
~~~~
 ssh-agent bash             # 类似刷新操作？
 ssh-add ~/.ssh/id_rsa_xx   # 添加文件到ssh
~~~~


##### 2. 修改.gitconfig文件
~~~~python
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
~~~~
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
git branch -a           # -a 为all
git branch -d <dev>     # 删除dev分支
git checkout -b <dev>   # 创建+切换到分支dev, 相当于下两句
git branch <dev>
git checkout <dev>


````
````
git log                     # 查看提交记录
git log --pretty=oneline    # 显示为一行
````
