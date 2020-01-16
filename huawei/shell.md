## 变量

### 本地变量

```shell
#!/bin/sh
a="hello world"
echo $a
```

**花括号**避免变量名与其他文字混淆

```shell
num=2
echo "this is the ${num}nd"
```

shell的默认赋值是字符串赋值。

```shell
var=1
var=$var+1
echo var
# 1+1 
```

```shell
var=1
let "var+=1"
echo $var
# 2
```

```shell
var=1
var=$[$var+1]
echo $var
# 2
```

```shell
var=1
var=`expr $var+1`
# 1+1
```

```shell
var=1
var=`expr $var + 1`  # 加号两边加空格，否则还是字符串方式赋值
# 2
```

```shell
# 显示本地变量
set
```

```shell
# 清除本地变量
unset variable-name
```

> `let`表示数学运算
>
> `expr`用于整数值运算，*每一项用空格隔开*
>
> `$[]`将中括号内的表达式作为数学运算计算，然后输出。



### 环境变量

> `export`   由export关键字处理过的变量叫环境变量

```shell
# 定义环境变量
export DOMAIN="chinaitlab.com"
```

```shell
# 显示环境变量
env
```

### 位置变量

> `$0`  shell script 文件名
>
> `$1`  第一个参数
>
> `$2`  第二个参数
>
> ...

> `shift`命令左移. 如: shift 3 表示$4->$1,$5->$2, $1 $2 $3 丢弃 (有啥用？)

### 只读变量

### 特殊变量

> `$?` 最后一个命令的退出状态. 0正常
>
> `$#` 传递到脚本的参数个数

## 字符串

单引号

> 类似于python中的r'string'

双引号

```shell
your_name="wangsy"
# 拼接字符串
a="hello, ${your_name} !"
string="abcdefghijk"
# 获取字符串长度
len=${#string}
# 字符切片
echo ${string:1:4}  # 从索引为1开始，取4个字符
```

数组

```shell
# 定义数组
array=(1 2 3)  # 用空格分开

# 单独定义数组的各个分量，不需要连续
a[1]=1
a[5]=5

# 取索引为1的值
value1=${array[1]}

# 获取数组所有元素
echo ${array[@]}  # @ or *
echo ${array[*]}

# 数组长度
len=${#array[@]}
len=${#array[*]}

# 数组单个元素的长度
len1=${#array[1]}  # 索引为1的元素的长度
```

## 运算符和表达式

```shell
var=1+1
echo ${var}
# 1+1

var=1
var=$var+1
echo ${var}
# 1+1
```

> let    (())  使用方法相同
>
> ```shell
> var=1
> let "var+=1"  # 参数不用加${}, 直接访问
> echo ${var}
> # 2
> 
> let "var=2**2"
> echo ${var}
> # 4
> 
> let "var=4*4"
> echo ${var}
> #16
> ```
>
> $[]
>
> ```shell
> var=1
> var=$[$var+1]
> echo ${var}
> # 2
> ```
>
> expr
>
> ```shell
> var=1
> var=`expr $var + 1` # 表达式符号间要用空格分开
> ```
>
> bc
>
> awk(研究一下，用这个吧)

运算符

> 算术运算符 (+  -  *  /)
>
> 按位运算符 (~  <<  >>  &  |  ^)
>
> 逻辑运算符 (&&  ||  >  ==  <  !=)
>
> 赋值运算符 (=  +=  -=  *=  /=  %=  &=  |=  ^=  <<=  >>=)

表达式



## 流程控制

### if

```shell
if ...; then
  ...
elif ...; then
  ...
else
  ...
fi
```



### 条件测试 ( test或[ )

> 命令`test`或`[]`可以测试一个条件是否成立
>
> 结果为`真`，该命令的`Exit Status`为`0`
>
> 结果为`假`，该命令的`Exit Status`为`1`

```shell
var=2
test $var -gt 1
echo $?
# 0

test $var -gt 3
# 1

[ $var -gt 3 ]
# 1
```

```shell
!               # 与
EXPR1 -o EXPR2  # 或
EXPR1 -a EXPR2  # 且
```



``` shell
-e filename  # filename存在，则为真
-d filename  # filename为目录，则为真
-f filename  # filename为文件，则为真
-L filename  # filename为符号链接，则为真
-r filename  # filename可读，则为真
-w filename  # filename可写，则为真
-x filename  # filename可执行，则为真
-s filename  # filename size不为零，则为真
f1 -nt f2    # f1比f2新，则为真(new then)
f1 -ot f2    # f1比f2旧，则为真(old then)

-n "$var"    # 判断是否有值
-z "$var"    # 判断是否为空
"$a" = "$b"  # 判断$a和$b是否相等

-gt          # 大于
-lt          # 小于
-gte         # 大于等于
-lte         # 小于等于
```

### && 和 ||

```shell
[ -f "/etc/shadow" ] && echo "This computer users shadow passwords."
# This computer users shadow passwords.
```

```shell
mailfolder="/var/spool/mail/james"
[ -r ${mailfolder} ] || { echo "Can not read ${mailfolder}"; exit 1; }
echo "${mailfolder} has mail from:"
grep "^From " ${mailfolder}
```



### case

```shell
case ... in
...) 
do something
;;
...)
do something
;;
esac
```

```shell
#!/bin/sh
ftype=`file "$1"`
case "${ftype}" in
"$1: Zip archive"*)
  unzip "$1"
;;
"$1: gzip compressed"*)
  gunzip "$1"
;;
"$1: bzip2 compressed"*)
  bunzip2 "$1"
;;
*)
  error "File $1 can not be uncompressed with smartzip"  # 类似于raise?
;;
esac
```

### while

```shell
while ...; do
  ...
done
```



### for

```shell
for var in ...; do
  ...
done
```

> 字符串用空格分开

```shell
for var in A B C; do
  echo ${var}
done
```

> `$*`: 包含所有输入的命令行参数值

```shell
# showrpm /cdrom/RedHat/RPMS/*.rpm
for rpmpackage in $*; do
  if [ -r "${rpmpackage}" ]; then
    ehco "======= $rpmpackage ======"
    rpm -qi -p ${rpmpackage}
  else
    echo "ERROR: cannot read file ${rpmpackage}"
  fi
done
```

### until

> 和while刚好相反

```shell
until ...; do
  ...
done
```

```shell
#!/bin/sh

i=0

until [[ i -gt 5 ]]; do
  echo ${i};
  let "i++"
done
```



### break

### continue

### select

```shell
#!/bin/sh
echo "What is your favourite OS?"
select var in "Linux" "Gnu Hurd" "Free BSD" "Other"; do
  break
done
echo "You have selected ${var}"
```

## 特殊字符

> `单引号`  忽略所有特殊字符
>
> `双引号`  防止通配符扩展，允许变量扩展
>
> `反引号`  
>
> `反斜杠`
>
> `单括号`   $() 等同于``;  $(...)格式受到POSIX标准支持，也利于嵌套。 
>
> `双括号`   $((...))等同于`expr ...`

```shell
#!/bin/sh
echo *.jpg
# a.jpg b.jpg
echo "*.jpg"
# *.jpg
echo '*.jpg'
# *.jpg

var='hello'
echo $var
# hello
echo "$var"
# hello
echo '$var'
# $var
```

```shell
#!/bin/sh
a=$(date +%F)
echo $a
# 2019-12-27
b=`date +%F`
echo $b
# 2019-12-27

c=$((1+2))
echo $c
# 3
d=`expr 1 + 2`
echo $d
# 3
```

## 函数

```shell
function 函数名() {
    command1
    command2
    [ return value ]
}
```

```shell
#!/bin/sh
help() {
    cat <<HELP
xtitlebar -- change the name of an xterm, gnome-terminal or kde konsole
USAGE: xtitlebar [-h] "string_for_titelbar"
OPTIONS: -h help text
EXAMPLE: xtitlebar "cvs"
HELP
    exit 0
}

[ -z "$1" ] && help
[ "$1" = "-h" ] && help
echo -e "33]0;$107"
```

## Shell嵌入命令

|        |                                  |
| :------- | --------------------------------- |
| :        | 空永远返回true(这啥？没见过啊?)   |
| .        | 从当前shell中执行                 |
| break    | 退出for/while/until/case语句      |
| cd       | change directory                  |
| pwd      | 显示当前目录                      |
| export   | 导出变量，使当前shell可利用它     |
| unset    | 从shell内存中删除变量或函数       |
| read     | 从标准输入读取一行文本            |
| readonly | 使变量只读                        |
| continue | 跳过当次循环                      |
| echo     | 标准输出                          |
| eval     | 读取参数，执行结果命令            |
| exec     | 执行命令，但不在当前shell         |
| exit     | 退出（系统调用级别， 进程退出）   |
| return   | 退出（语言级别， 堆栈的返回）     |
| set      | 控制各种参数到标准输出的显示      |
| shift    | 命令行参数向左偏移一个            |
| test     | 评估条件表达式                    |
| times    | 显示shell运行过程的用户和系统时间 |
| trap     | 当捕获信号时运行指定命令          |
| ulimit   | 显示或设置shell资源               |
| umask    | 显示或设置缺省文件创建模式        |
| wait     | 等待知道子进程运行完毕，报告终止  |

```shell
read -p "Input something: "
echo -e "test\ntest"
# test
# test
echo -n "xx"          # 不换行
```

## 常用命令

```shell
echo "text"
echo -n ""   #不换行，光标停留在行尾
ls
wc -l file   # 计算文件行数
wc -w file   # 计算文件中的单词数
wc -c file   # 计算文件中的字符数
cp src dst
mv oldfile newfile
rm file
cut -b5-7 file  # 输出每行5-7列的字符
cat file.txt
file aa.txt     # 得到文件类型
read var        # 提示用户输入，并将输入赋值给变量
sort file.txt   # 对file.txt行排序
uniq            # 删除文本文件中重复出现的行列
```

```shell
cat happybirthday.txt
# Happy Birthday to You!
# Happy Birthday to You!
# Happy Birthday Dear Tux!
# Happy Birthday to You!

sort happybirthday.txt
# Happy Birthday Dear Tux!
# Happy Birthday to You!
# Happy Birthday to You!
# Happy Birthday to You!

sort happybirthday.txt | uniq
# Happy Birthday Dear Tux!
# Happy Birthday to You!

sort happybirthday.txt | uniq -u   # -u 只显示不重复的行
# Happy Birthday Dear Tux!

sort happybirthday.txt | uniq -d   # -u 只显示重复的行
# Happy Birthday to You!

sort happybirthday.txt | uniq -uc  # -c 包含统计信息
# 1 Happy Birthday Dear Tux!

sort happybirthday.txt | uniq -dc
# 3 Happy Birthday to You!
```

> `tee`
>
> `basename file`
>
> `dirname file`
>
> `head file`
>
> `tail file`
>
> `find`
>
> `grep`
>
> `sed`
>
> `awk`
>
> `split`

### 管道

> `|`   将一个命令的输出作为另一个命令的输入
>
> ```shell
> grep "hello" file.txt | wc -l  # 搜索file.txt中含有'hello'的行并计算行数
> ```

### 重定向(< 和 >)

> `0`   标准输入
>
> `1`   标准输出
>
> `2`   标准错误信息输出
>
> `/dev/null` 
>
> `>`   写入文件并覆盖旧文件
>
> `>>`  写入文件尾部，保留旧文件内容

```shell
2>a.txt   # 错误信息输出到文件a.txt
2>1       # 标准错误输出重定向到文件1中
2>&1      # 将标准错误输出重定向到标准输出
```

```shell
# 标准输出和错误信息都不显示
ls 1>/dev/null 2>/dev/null
ls >/dev/null 2>&1
```

## 其他

###  BASE_SOURCE
```shell
BASE_SOURCE[0]
BASE_SOURCE
# 取得当前执行的shell文件所在的路径及文件名
# 相当于python中的__FILE__
```

### readlink

> 输出符号链接值或者权威文件名 (print value of a symbolic link or canonical file name)

### dirname

> 获取文件所在的绝对路径

```shell
dirname /usr/bin
# /usr
```

### chage

> 用于密码实效管理，修改账号和密码的有效期限。
>
> The chage command changes the number of days between password changes and the date of the last password change. This information is used by the system to determine when a user must change his/her password 

> -d
>
> -E
>
> -h
>
> -l
>
> -I
>
> -m
>
> -M
>
> -W



