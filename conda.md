***
查看conda版本
  `conda --version(conda -V)`
  
升级conda
  ````
  conda udpdate conda
  conda update --all
  ````
  
  
查看当前的配置信息(platform,conda version, conda-env version, default enviroment, channel URLs ...)
  `conda info`
  
查看当前环境(列出所有环境)
  `conda info --envs(conda info -e)`


管理环境(env)
````
  conda create --name snowflake biopython
  conda create -n snakes python=3 (snake为环境的名字，用来切换环境)
````

切换环境(activate/deactivate)
````
  Linux，OS X: source activate snowflakes
  Windows：activate snowflakes
  deactivate(从当前工作环境的路径切换到系统根目录)
````

复制环境(clone)
`conda create -n flowers --clone snowflakes`
  
移除环境(remove)
  `conda remove -n flowers --all`

国内镜像源作为默认镜像
````
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  conda config --set show_channel_urls yes(此行不知道具体意思...)
  此时在用户目录下会生成配置文件.condarc(估计是conda resource的意思)
  删除默认的镜像(- default)
````

安装工具包
````
conda install scrapy(安装爬虫工具包)
conda install pyqt=4
conda install pyqt=4.11
````

有时不能找到Package
[https://superuser.com/questions/988505/how-to-search-and-install-package-in-anaconda-conda](https://superuser.com/questions/988505/how-to-search-and-install-package-in-anaconda-conda)

````python
anaconda search pyqt5
anaconda search -t conda pyqt5  # -t 应该是制表的意思，以表格的形式展示
conda install -c http://conda.anaconda.org/bpentz pyqt5  # 后面是Name, '/'改为' '(空格)
````
***
