***
# 1. 在Docker Hub上搜索镜像
Docker Store[https://store.docker.com/](https://store.docker.com/)  
可以搜索镜像, 点击下载会有详细的Usage, 这里就不详细赘述了.

# 2. 配置加速器
在下载镜像的过程中, 发现速度是相当的慢, 所以搜索了一下有没有像`conda`之类的有下载源的东西, 然后找到了[https://blog.csdn.net/shenzhen_zsw/article/details/74277518](https://blog.csdn.net/shenzhen_zsw/article/details/74277518)   
<br>
这里用到了[DaoCloud](https://www.daocloud.io/)中的加速器, 详细文档地址[http://guide.daocloud.io/dcs/docker-9153151.html](http://guide.daocloud.io/dcs/docker-9153151.html)  
加速地址可以通过[注册](https://account.daocloud.io/signin)以后, 点击右上方的加速标志来获取一个[Docker Hub Mirror](https://www.daocloud.io/mirror#accelerator-doc)

# 3. 用命令去运行镜像
在`Docker Hub`中搜索镜像即可获取相应镜像的`Usage`, 操作简单, 此处忽略...
```bash
docker images    # 查看本地存在的镜像
docker image ls
```
***

# 创建自己的docker镜像
[http://www.cnblogs.com/linjj/p/5606911.html](http://www.cnblogs.com/linjj/p/5606911.html)
自己操作时出了问题, 而且速度特别慢...不想研究了,等有了mac继续更新- -
