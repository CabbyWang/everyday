# centerOS搭建Hexo

1. 安装Nginx(服务器配置)
```bash
yum install -y git nginx
```
配置
```bash
server{
	listen       80 default_server;
	listen       [::]:80 default_server;   # 默认监听端口
	server_name  wangsiyong.cc     # 填写个人域名
	root         /cabbyw/hexo      # 外网默认访问路径(hexo根目录)
}
```
2. 安装node.js
```bash
yum install -y nodejs
```
3. 安装git
```bashe
yum install git
```
4. Hexo
```bash
npm install hexo-cli -g
```
使用淘宝源
```bash
npm install -g cnpm --registry=https://registry.npm.taobao.org
cnpm install hexo-cli -g
```
