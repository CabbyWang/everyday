# redis应用场景

1. 缓存
2. 任务队列
3. 应用排行榜
4. 网站访问统计
5. 数据过期处理
6. 分布式集群架构中的session分离

# redis 安装

1. Mac

```shell
# 使用brew安装
brew install redis
# 启动redis服务
brew services start redis
redis-cli
# > ping
# PONG
```

2. linux

```shell
# 启动redis, 使用配置文件
./bin/redis-server ./redis.conf
# 关闭redis
.bin/redis-cli shutdown
```



# redis数据类型

1. 字符串
2. 列表
3. 有序集合
4. 散列
5. 集合



