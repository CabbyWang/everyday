***
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