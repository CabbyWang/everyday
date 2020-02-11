# git操作

### 第一次操作

初始化操作 --> 和远程仓库建立连接 --> 添加到暂存区 --> 提交 --> 提送到远程仓库
```python
git init
git remote add [git地址]
git add .
git commit -m "commit summary"
git push -u origin master
```

### 切换到某个tag

```shell
git fetch
git checkout ${tag_name}
```