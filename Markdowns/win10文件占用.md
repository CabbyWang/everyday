# Windows(10)文件夹或文件被占用解决办法

由于我使用的是win10系统, 所以这里介绍win10出现文件夹被占用时的解决办法(如果其他系统用到在做更新^ _ ^)

问题描述(如图):
![image1](http://upload-images.jianshu.io/upload_images/11567478-de5132c5e97c97a8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

通过查资料, 我发现了这个东西`资源监视器`, 亲测还是比较好用的
打开方式: 右键`开始菜单` - `搜索` - 输入`资源监视器`
![资源监视器1](http://upload-images.jianshu.io/upload_images/11567478-bdea48dd6abd9749.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

在红框画出的`关联的句柄`处直接输入会自动查找, 比如我这里输入`ClinicSystem`
![资源监视器2](http://upload-images.jianshu.io/upload_images/11567478-2ead24c12475e6bf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这里很明显, `clinicSystem`文件夹被`sqlserver.exe`占用了

解决办法:

找到了问题所在, 然后就是解决他了.
- 这里我们需要注意画圈部分的`PID`(port ID端口id, 每个端口都有一个id, 可以理解成人的身份证id一样, 独一无二的), 这里的`PID`是`14984`
- 打开`任务管理器` - `详细信息` - 找到相应`PID` - 干掉他(右键结束任务, 这个得确保结束了对自己现有东西不会有影响)
![任务管理器](http://upload-images.jianshu.io/upload_images/11567478-dac1c6bff95d1a0e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 占用解决了, 然后就可以开开心心的操作了
