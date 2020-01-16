# Vscode基本用法

vscode在我看来就是一个加强版的记事本，十分轻量，可个性化配置。

### 快捷键

<https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf> 

```
ctrl + k  ctrl + s
```



#### 场景

> 文件操作
>
> ```
> ctrl + k  ctrl + O   # 打开项目目录
> ctrl + N             # 新建文件
> ctrl + shift + N     # 新建项目(类似chrome的ctrl + n)
> ```
>
> 光标移动
>
> ```
> Home                 # 光标移到句首
> End                  # 光标移到句末
> Ctrl + Home          # 移到文件开头
> Ctrl + End           # 移到文件末尾
> ctrl + →             # 光标向右移动一个字符
> ctrl + ←             # 光标向左移动一个字符
> ```
>
> 行复制
>
> ```
> ctrl + c             # 复制/复制整行
> ctrl + v             # 粘贴
> shift + alt + ↑/↓    # 复制整行，向↑/↓粘贴
> ```
>
> 行移动
>
> ```
> Alt +  ↑/↓           # 整行向上/下移动
> ```
>
> 注释
>
> ```
> ctrl + /             # 行注释
> alt + shift + A      # 块注释
> ```
>
> 缩进
>
> ```
> ctrl + [             # 向左缩进
> ctrl + ]             # 向右缩进
> tab				    # 向右
> shift tab            # 向左
> ```
>
> 转到定义
>
> ```
> ctrl + 鼠标左键       # 跳转到定义
> F12                  # 同上 (Go to Definition)
> Alt + F12            # 代码定义以浮窗的形式覆盖在当前页面上 (Peek Definition)
> ```
>
> 编辑点间切换
>
> ```
> alt + →              # 切换到下一个编辑点
> alt + ←              # 切换到上一个一个编辑点
> ```
>
> 折叠代码块
>
> ```
> ctrl + shift + [     # 折叠代码块
> ctrl + shift + ]     # 打开代码块
> ctrl + K  ctrl + 0   # 折叠所有区域(能缩进的代码块全部缩进)
> ctrl + k  ctrl + 1   # 折叠当前区域外的所有区域（常用）
> ctrl + k  ctrl + 2   # 折叠所有二级子区域
> ctrl + k  ctrl + 3   # 折叠所有三级子区域
> .
> .
> .
> ctrl + k  ctrl + j   # 打开所有折叠代码块
> ```
>
> 多行编辑问题
>
> ```
> 鼠标中键 框选
> alt + shift + 鼠标左键 框选
> alt + 鼠标左键 点选
> ```
>
> 检索替换
>
> ```
> ctrl + F             # 文件内查找
> ctrl + H             # 文件内替换
> ctrl + shift + F     # 工作区内全局查找
> ctrl + shift + H     # 工作区内全局替换
> ```
>
> 界面显示
>
> ```
> ctrl + `             # 打开/关闭终端
> ctrl + shift + `     # 新建终端
> # 修改配置文件: terminal.integrated.shell.windows 修改内置终端
> 
> ctrl + b             # 打开/关闭左侧栏
> ```
>
> 比较
>
> ```
> 
> ```
>
> 调试
>
> ```
> ctrl + shift + D     # 打开调试面板
> ```

#### 个性化设置

> 编辑器主题，字体
>
> ```
> ctrl + k  ctrl + t   # 打开主题设置
> ctrl + +             # 放大编辑器字体
> ctrl + -             # 缩小编辑器字体
> ```
>
> 自定义快捷键
>
> ```
> ctrl + k  ctrl + s
> ```
>
> 自定义设置
>
> ```
> ctrl + ,
> ```
>

### 我的git提交流程

[sourceTree]()

1. clone个人remote仓库(origin)到本地

   ```
   git clone ssh://XXX
   ```

2. 增加远程主库(base)仓到本地

   ```
   git remote add base ssh://XXXX
   ```


3. 查看确认远程仓列表

   ```
   git remote -v
   ```

4. 合并base仓代码到本地，合并

   ```
   git pull base master
   ```

5. 推送代码到origin仓库

   ```
   git push origin master
   ```

6. 提交MR

### 代码片段(snippet)

```

```



### 插件

> vscode-icons            文件图标