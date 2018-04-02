***
# Install for Windows
由于我暂时用的电脑是window是10 家庭中文版,
所以在安装的过程中出现了些许问题,这里记录一下,方便之后查阅.   
(查看Windows版本可以使用命令`winver`)  
这是docker的官方介绍[https://docs.docker.com/docker-for-windows/install/](https://docs.docker.com/docker-for-windows/install/)

**如果windows版本足够的话,可以直接安装docker,不然需要安装docker-ToolBox**

下面是官方给出的安装docker-ToolBox的文档,非常详细   [https://docs.docker.com/toolbox/toolbox_install_windows/#what-you-get-and-how-it-works](https://docs.docker.com/toolbox/toolbox_install_windows/#what-you-get-and-how-it-works)

按照步骤安装(感觉比较简单,一路next即可,就不赘述了)   

下面是遇到的一个问题
```bash
Running pre-create checks…
(default)No default Boot2Docker ISO found locally, downloading the latest release…
Error with pre-create check:
xxxxxxxxxx(比较多...)
Looks like something went wrong in step ‘Checking if machine default exists’…
Press any key to continue…
```

## DockerToolbox

解决办法[https://forums.docker.com/t/pre-create-check-failed-when-first-time-launch-docker-quickstart-terminal/9977](https://forums.docker.com/t/pre-create-check-failed-when-first-time-launch-docker-quickstart-terminal/9977)    
将boot2docker.iso文件放到~/.docker\machine\cache目录下, 问题解决   


## 镜像仓库的配置
- 先执行这个命令（镜像地址可以自行替换）`docker-machine ssh default "echo 'EXTRA_ARGS=\"--registry-mirror=https://xks740zc.mirror.aliyuncs.com\"' | sudo tee -a /var/lib/boot2docker/profile"`  
- 再执行这个命令 `docker-machine restart default`   
会重启Docker虚拟机
- 然后执行命令`docker-machine ssh default` 即可进入docker命令行环境了


*参考:*   [https://www.jianshu.com/p/490884917c4d](https://www.jianshu.com/p/490884917c4d)  
[http://www.shuijingwanwq.com/2017/10/11/1958/](http://www.shuijingwanwq.com/2017/10/11/1958/)
***