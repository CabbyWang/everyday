拷贝文件

```shell
# 将test.txt拷贝到ip地址为10.10.110.110机器上的/root/目录下
scp test.txt root@10.10.110.110:/root/
```

拷贝文件夹

```shell
# 将test文件夹拷贝到ip地址为10.10.110.110机器上的/root/目录下
scp -r test root@10.10.110.110:/root/
```

