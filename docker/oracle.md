***

# docker 安装oracle

1.拉取镜像
```shell
docker pull registry.cn-hangzhou.aliyuncs.com/helowin/oracle_11g
```

```shell
docker run -it -d -p 1521:1521 -v "E:/oracle":"/data/oracle" --name oracle11 registry.cn-hangzhou.aliyuncs.com/helowin/oracle_11g
```

