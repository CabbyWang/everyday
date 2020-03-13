# 2020/02/12

1. Mobaxterm

2. FinalShell

3. netflix(奈飞)

4. Certbox安装Letsencrypt证书

   - 启用https，需要从证书机构(CA)获取证书
   - let's Encrypt就是一个CA
   - Certbox是Let's Encrypt官方推荐的获取证书的**客户端**

5. CN2(Chinatelecom Next Carrier Network)

   > 163骨干网
   >
   > CN2 GT.     CN2中的一个中端产品   202.97.x.x 
   >
   > CN2 GIA（Global Internet Access） 59.43.x.x

# 2020/02/13

1. 数据结构与算法 05数组
2. Ifttt
3. telegram
   - group
   - chanel

# 2020/02/14

1. 数据结构与算法 06
2. 安装
   - [ ] Redis desktop manager
   - [ ] VMware fusion
   - [x] 4K Live Wallpaper
   - [ ] Wireshark
   - [ ] PDF Professional
3. AWS Azure

# 2020/02/16

1. tcp/ip握手内容

   1. 应用层
   2. 表示层  编码处理 加密等
   3. 会话层  何时建立通讯连接 何时发送数据
   4. 传输层  提供端对端的接口 端口号(源端口号 目标端口号)
   5. 网络层  为数据包选择路由 ip(源ip地址 目标ip地址 协议号(tcp/upd))
   6. 数据链路层
   7. 物理层

2. 几种排序算法

   1. 冒泡排序

      遍历n次， 每次将两个元素比较，顺序错误就交换

   2. 选择排序

      每次在为排序序列中找到最小元素，存放到已排序序列的尾部

   3. 插入排序

      在未排序序列中取出第一个元素，与已排序序列一个个比较，然后找到相应位置并插入

   4. 希尔排序

   5. 归并排序

      分治思想，分成小问题内部排序，然后合并起来

   6. 快速排序

   7. 堆排序

   8. 计数排序

   9. 桶排序

   10. 基数排序

3. 简单说下mysql是什么

4. python基础

   1. (可迭代对象)可迭代的

      > 实现了iter方法

   2. 迭代器

      > 可迭代的 + 实现了next方法 = 实现了iter方法 + 实现了next方法

   3. 生成器

      > 带有yield的函数

5. 函数重载

   > python没有重载
   >
   > 1. 函数功能相同，参数类型不同
   >
   >    python是动态语言，可以接受不同类型的参数
   >
   > 2. 函数功能相同，参数个数不同
   >
   >    python有缺省参数，缺少的参数可以设置为缺省参数

6. 多态

   以继承和重写父类为前提

   是调用方法的技巧，不会影响到类的内部设计

7. 协程

   可等待对象:

   1. 协程  async

      async def 开头的是协程函数

      调用协程函数所返回的对象是协程对象

   2. 任务

      asyncio.create_task()

   3. Future

8. 闭包

   以函数为参数，返回一个函数

# 2020/02/18

1. 死锁

   多个进程循环等待它方占有的资源而无限期地僵持下去的局面。

   产生死锁的必要条件:

   1. 互斥条件
   2. 不可抢占条件
   3. 占有且申请条件
   4. 循环等待条件

   数据库死锁原因: 

   1. 事务之间对资源访问顺序的交替

      一个用户A访问表A(锁住了表A)，然后访问表B；另一个用户B访问表B(锁住了表B)，然后访问表A

      解决办法: 程序BUG，调整程序逻辑

   2. 并发修改同一内容

      解决办法：使用乐观锁或悲观锁

2. 链表反转

   循环

3. mysql索引实现方式

4. mysql引擎有哪些

# 2020/02/19

1. 极客时间
2. rss
   1. tiny tiny rss(自建服务端)
   2. rsshub(万物皆可rss)

# 2020/02/20

1. es?
2. rss?
3. Docker-compose?
4. nodejs基础?
5. 飞书?
6. [Unit test vs integration test？](https://realpython.com/python-testing/#unit-tests-vs-integration-tests)
7. [interview？]([https://github.com/taizilongxu/interview_python#1-selectpoll%E5%92%8Cepoll](https://github.com/taizilongxu/interview_python#1-selectpoll和epoll))
8. [协程?](https://docs.python.org/zh-cn/3/library/asyncio-task.html)
9. setcap?
10. set uid and gid (SUID SGID)?
11. docker-compose?
12. Serverless 微服务 FaaS？
13. 单点登录？CAS?
14. jwt？
15. 用户堆栈和系统堆栈？
16. Promise? Generater? next?

# 2020/03/01

1. cssreset
2. icomoon(处理svn)
3. viewport

# 2020/03/02

1. cli.im(草料二维码)

2. css 伪类 伪元素

3. html <p> := paragraph (段落 块级元素)

4. html <span> (行内元素)

5. position: static   默认，没有定位

   position: fixed    固定，绝对定位，相对于浏览器窗口进行定位

   position: relative   相对定位，相对其正常位置进行定位

   position: absolute 绝对定位，相对具有定位属性的父元素进行绝对定位

6. in (英寸)

   em (1em 等于当前的字体尺寸)

   px (像素)

# 2020/03/04

1. css display: block 块级元素

   ​	  display: inline 内联行内元素

   ​	  display: block-inline 内联块级元素

2. json和jsonp

   json才是目的，jsonp只是手段
   admin@sstz.me

   Happy2019

苏大

| 专业               | -      | 学院                 | 年份 | 招   | 录   |
| ------------------ | ------ | -------------------- | ---- | ---- | ---- |
| 软件工程(非全日制) | 085212 | 计算机科学与技术学院 | 2019 | 102  | 31   |
| 软件工程(全日制)   | 083500 | 计算机科学与技术学院 | 2019 | 70   | 4    |
|                    |        |                      |      |      |      |
| 软件工程(非全日制) | 085212 | 计算机科学与技术学院 | 2018 | 321  | 27   |
| 软件工程(全日制)   | 083500 | 计算机科学与技术学院 | 2018 | 59   | 3    |
|                    |        |                      |      |      |      |
| 软件工程(非全日制) | 085212 | 计算机科学与技术学院 | 2017 | 208  | 39   |
| 软件工程(全日制)   | 083500 | 计算机科学与技术学院 | 2017 | 106  | 5    |
|                    |        |                      |      |      |      |

 学院拥有一支教育理念先进，研究能力强，教学经验丰富、结构合理的师资队伍。学院现有教职工160人，其中教授28人，副教授53人，博士生导师20人，硕士生导师40余人。教师中有“国家杰出青年科学基金”获得者1人、“国家级有突出贡献的专家”2人、江苏省高校教学名师1人、多人次获得江苏省“青蓝工程”学术带头人和“333高层次人才工程”中青年科学技术带头人等称号。

> ①101 思想政治理论 ②201 英语一 ③301 数学一 ④872 数据结构与操作系统 复试：1、 Python 程序设计（上机考：选 择题+编程题，编程语言版本为 Python 3.5 及以上，编程环境可以选择 IDLE、Pycharm 或 Anaconda+Spyder 中的一种。）2、综合 （面试）

