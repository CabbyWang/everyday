***
# docker 安装 mysql

```shell
docker pull mysql
docker run --name mysql \
    --restart always \
    -e MYSQL_ROOT_PASSWORD=password \
    -v "E:/mysql/mysql":"/var/lib/mysql" \
    -v "E:/mysql/config":"/etc/mysql/conf.d" \
    -v "E:/mysql/log":"/var/log/mysql" \
    -p 3307:3306 -d mysql:latest
```

**mysql8 之前的版本中加密规则是mysql_native_password,而在mysql8之后,加密规则是*caching_sha2_password*

解决办法:
```shell
# 进入docker控制台
# 进入mysql控制台
mysql -uroot -p
> alter user 'root'@'localhost'  identified with mysql_native_password by 'password';
```