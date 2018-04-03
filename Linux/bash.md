***
# Shell环境
`Linux`的`Shell`种类非常多, `bash`只是其中的一种, 常见的Shell种类有:
- Bourne Shell（/usr/bin/sh或/bin/sh）
- Bourne Again Shell（/bin/bash）
- C Shell（/usr/bin/csh）
- K Shell（/usr/bin/ksh）
- Shell for Root（/sbin/sh）
- ......

# 第一个Shell脚本
```shell
#!/bin/bash
echo "Hello World!"
```
这里第一行的`#!/bin/bash`是一种约定, 告诉系统用什么Shell来执行.
- 作为可执行程序执行
```bash
~$ chmod -x ./test.sh
~$ ./test.sh
```
1. 创建脚本后, 脚本没有`可执行`权限, 可以使用`chmod -x ./test.sh`使`test.sh`可执行  
2.*这里使用`./`告诉系统在当前路径下运行. 如果直接写`test.sh`, Linux系统会去`Path`中寻找有没有叫`test.sh`的, 而只有`/bin`, `/sbin`, `/usr/bin`, `/usr/sbin`等在`Path`中, 显然是找不到的*

- 作为解释器的参数  
```bash
# 不需要在第一行指定解释器信息
/bin/bash test.sh
/bin.sh test.sh
```

# Shell变量
```bash
~$ my_name='wangsiyong'      # 这里要注意的是, 变量名和等号中间不能有空格
~$ my_name="wangsiyong"
~$ echo $my_name
~$ echo ${my_name}           # {}这里是一个变量的边界
~$ for file in `ls /etc`     # 遍历/etc目录下文件名
```

```bash
~$ str = "Hello, ${my_name} !"
~$ echo $my_name $str
```
