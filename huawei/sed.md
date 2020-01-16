删除: `d`

```shell
sed '2d' test.txt       # 删除test.txt文件的第二行
sed '2,$d' test.txt     # 删除test.txt文件的第2行到最后一行
sed '$d' test.txt       # 删除最后一行
sed '/test/'d test.txt  # 删除包含test的所有行
```

替换

```shell
sed -i 's/test/g' test.txt
```

