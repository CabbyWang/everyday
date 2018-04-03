***
# 常见命令
## ls cd
`cd: `Change Directory的简写   
`ls: `list的简写
```bash
~$                         # ~表示用户目录文件夹(home/cabby/), $表示执行
~$ cd Documents/
~/Document$ cd ..
```
```bash
~$ ls
~$ ls -a                   # 显示所有文件(包括隐藏的文件)
~$ ls -l                   # -l long的简写, 打印出文件的权限,用户名,大小,修改日期, 文件名
~$ ls -lh                  # -lh human
```
## touch, cp, mv
`touch: `新建文件
`cp: `copy
`mv: `move, move到同级目录则为重命名
```bash
~$ touch file1
~$ touch file1, file2, file3  # 创建多个文件

~$ cp file1 file1copy         # copy
~$ cp -i file1 file1copy      # -i interactive 覆盖前提示
~$ cp file1 Documents/        # copy到Documents文件夹下
~$ cp file* Documents/        # 复制多个文件(前面是file的文件)
~$ cp file1 file2 folder/     # 复制多个文件 
~$ cp -R folder1/ folder2/    # 复制文件夹(需要加上-R)

~$ mv file1 folder1/
~$ mv file1 file1copy         # 重命名
```

## mkdir, rmdir, rm
`mkdir: `make directory创建目录   
`rmdir: `remove directory  
`rm: `remove  
`-r`或`-R`(Recursively) 用来删除文件夹
```bash
~$ mkdir folder1/
~$ mkdir folder1/folder2/
~$ rmdir folder1/             # 文件夹必须是空的才能remove
~$ rm file1
~$ rm -i f1 f2 f3             # 每个要移除的文件都进行提示
~$ rm -l f1 f2 f3 f4          # 超过3个文件才进行提示
~$ rm -r folder1              # 在文件夹有文件的情况下删除文件夹
```

## nano, cat
`nano: ` 编辑
`cat: ` 查看
```bash
~$ nano t.py           # 创建p.py并编辑,  使用ctrl+x退出
~$ cat t.py            # 查看
~$ cat t.py > t1.py    # 将文件内容放到另一个文件
~$ cat t.py t1.py > t2.py  # 将多个文件打包一起放入另一个文件
~$ cat t.py >> t1.py   # 将内容添加到t1.py的末尾
```

## 文件权限
`ls -l `查看权限   
<br>
`d` 这是一个文件夹   
`-` 这是一个文件  
<br>
权限:  
`r` read   
`w` write   
`x` execute   

`g` Group, 一个Group里可能有一个或多个user   
`u` User   
`o` Others, 除了User和Group以外的人   

```bash
drwxr-xr-x       # 下面分开写,方便解析
drwx r-x r-x     # 这是一个文件夹, User有rwx(读/写/执行)权限,Group有r-x(读/执行)权限,Others有r-x权限
```

## chmod修改权限
`chmod: `change mode
```bash
# t1.py    ----rw-r--
~$ chmod [who][how] [which]   # [谁][怎么修改] [哪个文件]
~$ chmod u+r t1.py            # u+r  User+Read权限, 很形象
# -r--rw-r--
```
