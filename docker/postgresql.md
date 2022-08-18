***
# docker 安装 postgresql
1.拉取镜像

```shell
docker pull postgres
```

2.启动镜像

```shell
docker run --name mypostgres --restart always -d -p 5432:5432 -e POSTGRES_PASSWORD=123456 postgres
```

3.进入容器

```shell
docker exec -it postgres psql -U postgres -d postgres
# postgres 容器名
# -d DATABASE
```

4.使用终端连接

```shell
psql -U username -h ipaddress -d dbname
# -h HOST
# -d DATABASE
```

5.查看数据库所有表

```shell
select * from pg_tables;
```