# redis简单使用

## String(字符串)

```shell
# 存数据
set name wang
getset name siyong
# 取数据
get name
# 删除数据
del name
# 获取所有的key
keys *
```

```shell
# 将值增加1， 如果没有值，则默认0+1
incr num  # num = "1"
# 将值减1, 如果没有值，则默认0-1
decr num2  # num2 = "-1"
incrby num3 5  # num3 = "5"
decrby num4 5  # num4 = "-5"

# 在字符串后追加字符
append num 5  # num = "15"
```

## Hash(哈希)

```shell
# hset 设置键值
hset myhash username wang
hset myhash age 24

# hmset 设置多个键值
hmset myhash username wang age 24

# hget 获取值
hget myhash username

# hmget 获取多个key的值
hmget myhash username age

# hgetall 获取所有的key和value
hgetall myhash

# hdel 删除(可删除多个) 
hdel myhash username age

# del 删除hash
del myhash

# 将值增加1
hincrby myhash age 5

# 判断key是否存在
hexists myhash username

# 属性个数
hlen myhash

# 获取所有key
hkeys myhash

# 获取所有value
hvals myhash
```

## List(链表)

```shell
# 从左边尾部插入
lpush mylist a b c
lpush mylist 1 2 3
# 从右边尾部插入
rpush mylist a b c
rpush mylist 1 2 3

# 通过索引获取list
lrange mylist 0 5

# lpop 从头部弹出元素
lpop mylist
# rpop 从尾部弹出元素
rpop mylist

# list长度
llen mylist

#-------------------
# lpushx 在list存在时插入
lpushx mylist x
lpushx mylist2 x  # 不会插入

# lrem 删除(remove)
lrem mylist 2 a  # 从左到右删除2个a
lrem mylist 0 a  # 从左到右删除所有a
lrem mylist -2 a  # 从右到左删除2个a

# lset 通过索引设置值
lset mylist 3 mmm

# linsert 在元素前后插入
linsert mylist before a 11  # 在第一个a前插入11
linsert mylist after a 11  # 在第一个a后插入11

# rpoplpush 从list1的右边弹出(pop)，压入(push)list2的左边
lpoplpush list1 list2
```

## set(集合)

```shell
# 添加
sadd myset a b c

# 删除
srem myset a b

# 输出所有元素
smembers myset

# 元素是否存在
sismember myset a

# 差集
sdiff myset1 myset2

# 交集
sinter myset1 myset2

# 并集
sunion myset1 myset2

# ------------------
# scard 元素数量
scard myset

# srandmember 随机返回set中的一个成员
srandmember myset

# sdiffstore 将两个set的差集存到另一个set中
sdiffstore my myset1 myset2  # 将myset1和myset2的差集存储到my中

# sinterstore 将两个set的交集存到另一个set中
sinterstore my myset1 myset2  # 将myset1和myset2的交集存储到my中

# sunionstore 将两个set的并集存到另一个set中
sunionstore my myset1 myset2  # 将myset1和myset2的并集存储到my中
```

## sorted-set

> 每个元素都对应一个分数

```shell
# 添加
zadd mysort 70 zs 80 ls
zadd mysort 100 zs

# 获取分数
zscore mysort zs  # 100

# 获取成员数量
zcard mysort

# 删除
zrem mysort zs ls

# 通过索引获取set
zrange mysort 0 -1  # 从小到大顺序输出所有值
zrange mysort 0 -1 withscores  # 将分数也输出出来
zrevrange mysort 0 -1  # 从大到小输出所有值

# 删除
zremrangebyrank mysort 0 4  # 按照排名范围删除
zremrangebyscore mysort 80 70  # 按照分数删除

# -----------------------------------------
# 取某一个分数范围内的值
zrangebyscore mysort 0 100 withscores
zrangebyscore mysort 0 100 withscores limit 2 3  # 从第2个索引开始，取后面3个数

# 增加某个值的分数
zincrby mysort 3 zs

# 某个分数范围内值的个数
zcount mysort 20 50
```

## Keys的通用操作

```shell
# keys pattern 列出满足条件的所有key
keys *
keys my?

# 判断key是否存在
exists my1

# 重命名key
rename my1 newkey

# 设置超时时间
expire newkey 1000

# 查看剩余超时时间
ttl newkey

# 查看类型
type newkey
```

## 多数据库

> 最多16个数据库， 从0到15， 默认使用0数据库

```shell
# 切换数据库
select 1

# 将key移动到1数据库
move myset 1
```

## 事务

> multi  开始(begin)
>
> exec  执行(commit)
>
> discard  回滚(rollback)

```shell
multi
set age 11
incr age
exec

multi
set age 11
incr age
discard
```

## redis持久化

> redis的高性能是由于所有的数据都存储在内存中。防止数据丢失， 需要将内存中的数据同步到硬盘上，这个过程称为redis持久化操作。

1. RDB方式(默认)

   > 将内存中的数据集快照指定时间间隔写入到磁盘

   配置

   ```shell
   save 900 1  # 每900秒至少有1个改动时保存快照
   save 300 10  # 每300秒至少有10个改动时保存
   save 60 10000  # 每60秒至少有10000个改动时保存
   
   dbfilename dump.rdb  # rdb文件名
   ```

2. AOF方式

   > 以日志的形式记录redis服务器的每一次操作

   配置

   ```shell
   appendonly yes  # 开启aof
   
   appendfilename "appendonly.aof"  # aof文件名
   appendfsync always  # 每次操作都写入日志 更安全
   # appendfsync everysec  # 每秒
   # appendfsync no  # 不写入
   ```

3. 无持久化(用于缓存)

4. 同时使用RDB和AOF

## 其他

```shell
# 清空数据库
flushall

# 重写AOF文件
bgrewriteaof
```



