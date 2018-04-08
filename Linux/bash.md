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
*1. 创建脚本后, 脚本没有`可执行`权限, 可以使用`chmod -x ./test.sh`使`test.sh`可执行*  
*2. 这里使用`./`告诉系统在当前路径下运行. 如果直接写`test.sh`, Linux系统会去`Path`中寻找有没有叫`test.sh`的, 而只有`/bin`, `/sbin`, `/usr/bin`, `/usr/sbin`等在`Path`中, 显然是找不到的*

- 作为解释器的参数  
```bash
# 不需要在第一行指定解释器信息
/bin/bash test.sh
/bin.sh test.sh
```

# Shell基础语法
## echo
```bash
~$ echo aaa                 # 输出字符串
# aaa
~$ echo 'aa\n $name "'      # 单引号,原封不动的输出引号内的字段
# aa\n $name "
~$ read name; echo "My name is $name"   #双引号可以显示变量
wangsiyong
# My name is wangsiyong
echo `date`                 # 反引号内部可以执行命令,返回执行结果
# 2018年 04月 08日 星期日 14:32:43 CST
echo "aa\nbb"
# aa\nbb
echo -e "aa\nbb"            # -e 显示换行(\c 不换行, 感觉正常用不着,记录一下)
# aa
# bb
```
## printf
- 不同于`echo`会自动添加换行符, `printf`需要手动添加换行符;
- 不同于`echo`, `printf`单双引号没有区别;
- 模仿`C`程序库中的printf(), 脚本可移植性比`echo`好

```bash
# printf format-string [arguments..]
printf 'aaa\n'
# aaa
printf '%-10s %-8s %-6s' name sex weight;    # %s中间的-表示左对齐(默认为右对齐), 数字表示宽度(10则为10个字符的宽度)
printf '%-10s %-8s %-6.2d' wang male 120;    # .2 表示保留小数点后两位
printf '%-10s %-8s %-6.2d' li female 90
# name   sex    weight
# wang   male   120.00
# li     female 90.00
printf %s aa
# aa
printf '%s %s\n' a b c d e    # 没有arguments时, %s用 NULL 代替, %d 用 0 代替
# a b
# c d
# e
```

## 变量
```bash
~$ my_name='wangsiyong'      # 这里要注意的是, 变量名和等号中间不能有空格
~$ my_name="wangsiyong"
~$ echo $my_name
~$ echo ${my_name}           # {}这里是一个变量的边界
~$ for file in `ls /etc`     # 遍历/etc目录下文件名
~$ for file in `ls /etc`; do mv ${file} xx${file}; done      # 遍历重命名
```
**注意: ***因为字符串比较符中的等于是`=`, 所以在赋值的时候中间要有空格*

```bash
~$ str = "Hello, ${my_name} !"
~$ echo $my_name $str                  # 拼接字符串
~$ string = ${str:2:3}                 # 截取字符串
~$ echo `expr index "$string" wang`    # 这里的index在有空格的时候感觉有点奇怪?
~$ echo ${#string}                     # 获取字符串长度
```

## 数组
```bash
~$ array_name=("a" "b" "c")
~$ value1=array_name[1]
~$ echo ${array_name[@]}
~$ echo ${array_name[*]}           # 获取数组中的所有元素
~$ length=${#array_name[*]}        # 获取数组的长度
~$ length_onestr=${#array_name[1]} # 获取数组单个元素的长度
```

## 参数
`$# ` 传递参数的个数  
`$* ` 返回一个单字符串,显示所有参数 "$1 $2 $3"  
`$@ ` 与`$*`一样 "$1" "$2" "$3"  
`$$ ` 脚本运行的当前进程ID号  
`$! ` 后台运行的最后一个进程的ID号  
`$? ` 返回最后命令的退出状态, `0`表示没有错误, 其他表明有错误  
`$- ` 显示Shell使用的当前选项, 与`set命令`功能相同(这里暂时还不太理解)
```bash
 #!/bin/bash

 echo "-- \$* --"
 for i in "$*"; do
     echo 1111
     echo $i
 done

 echo "-- \$@ --"
 for i in "$@"; do
     echo 2222
     echo $i
 done
 # ~$ ./test.sh 1 2 3
 # -- $* --
 # 1111
 # 1 2 3
 # -- $@ --
 # 2222
 # 1
 # 2222
 # 2
 # 2222
 # 3
```
*`$*`只打印了一次, 而`@$`打印了3次. 从打印结果看`$*`返回的是单个字符"1 2 3"; 而`$@`返回的是"1" "2" "3"*

## 运算符
*表达式和运算符之间要有空格*  
`expr`是一款表达式计算工具, 使用它可以完成表达式的求值操作.
```bash
#!/bin/bash

val=`expr 1 + 2`
echo "1 + 2 = $val"
```
*MAC中的`expr`语法是: `$((表达式))`*
### **算术运算符**
`+`加 `-`减 `*`乘 `/`除(取整) `%`除(取余) `=`赋值 `==`等于 `!=`不等于
```bash
a=10
b=20
echo "a + b = `expr $a + $b`"
echo "a - b = `expr $a - $b`"
echo "a * b = `expr $a \* $b`"  # 乘号(*)前必须加反斜杠
echo "a / b = `expr $a / $b`"
echo "a % b = `expr $a % $b`"
echo "a == b : expr $a == $b"   # a == b : 0
echo "a != b : expr $a != $b"   # a != b : 1
```
### **关系运算符**
*关系运算符只支持数字, 不支持字符串, 除非字符串的值是数字*    
`-eq` 相等返回true  
`-ne` 不相等返回true   
`-gt` 左边大于右边返回true   
`-ge` 左边大于等于右边返回true  
`-lt` 左边小于右边返回true  
`-le` 左边小于等于右边返回true
```bash
a=10
b=20
if [ $a -eq $b ]              # 其他关系运算符同样用法
then
    echo "$a -eq $b : a == b"
else
    echo "$a -eq $b : a != b"
fi
```

### **布尔运算符**
`!`非 `-o`或(or) `-a`与(and)
```bash
if [ $a le $b -a $ a -gt $b ]
then
    echo 1111
fi
```
### **逻辑运算符**
```bash
if [[ $a -eq 10 || $b le a ]]; then echo "true"; fi     # 这里似乎只能使用两个[], 不然会报错, 具体原因之后再研究
# true
```

### **字符串运算符**
顾名思义, 字符串运算符用于字符串的比较  
`=` 相等  
`!=` 不相等  
`-z` 长度为0返回true  
`-n` 长度不为0返回true  
`str` 字符串是否为空, 不为空返回true  
在测试中, 发现个很奇怪的现象, 先记录一下
```bash
a='abc'
b=''
if [ -n $a ]; echo 111; else echo 222; fi
if [ -n $b ]; echo 111; else echo 222; fi
# 输出都为111
```

### **文件测试运算符**
`-e` (exist)文件是否存在  
`-s` (str)文件是否为空(文件大小是否大于0), 不为空返回true   
`-d` (directory)是否是目录  
`-f` (file)是否是文件  
`-r` (read)是否可读  
`-w` (write)是否可写  
`-x` (execute)  
`-p` (pipe)是否是有名管道  
`-b` (block)检测文件是否是块设备文件  
`-c` 检测文件是否是字符设备文件  
`-g` 检测文件是否设置了SGID位  
`-k` 检测文件是否设置了粘着位  
`-u` 检测文件是否设置了SUID位  
```bash
touch aa
aa='aa'
if [ -s $aa ]; then echo 11; else echo 22; fi
# 22
if [ -e $aa ]; then echo 11; else echo 22; fi
# 11
```



**输出当前文件夹中的所有以`.py`结尾的文件**
```bash
for file in `find . -name '*.py'`; do echo $file; done
```