> `-i <interface>` 指定监听的网络接口
>
> `-t`  不显示时间戳
>
> `-c` 限制抓取数据包的个数
>
> `-s <length>` 设置捕获数据包的长度
>
> `-w <filename>` 保存文件
>
> `-vv` 指定更详细模式输出更详细的报文信息



类型限定词

> `host` 指定主机或目的地址
>
> `port` 指定端口
>
> `net` 指定某一子网



传输方向限定词

> `src` 源地址
>
> `dst` 目的地址
>
> `src port` 源端口
>
> `dst port` 目的端口



协议限定词

> `tcpdump icmp` 过滤所有ICMP协议的数据包
>
> `tcpdump tcp` 过滤所有TCP协议的数据包
>
> `tcpdump udp` 过滤所有UPD协议的数据包
