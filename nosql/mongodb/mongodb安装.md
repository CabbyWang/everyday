# # mac安装mongodb

1. 下载mongodb的tgz包。 [MongoDB Download Center](https://www.mongodb.com/download-center/community?jmp=docs)

2. 解压

   ```shell
   # 我的电脑默认下载到Downloads目录下
   cd ~/Downloads
   tar -zxvf mongodb-macos-x86_64-4.2.3
   mv mongodb-macos-x86_64-4.2.3 /usr/local/Cellar
   cd /usr/local/Cellar
   ```

3. 创建软链接

   将bin目录下的文件链接到环境目录/usr/local/bin下，也可以cp过去，我比较偏向使用软链接

   ```shell
   sudo ln -s /usr/local/Cellar/mongodb-macos-x86_64-4.2.3/bin/* /usr/local/bin
   ```

   ```shell
   # 也可以cp
   sudo cp /usr/local/Cellar/mongodb-macos-x86_64-4.2.3/bin/* /usr/local/bin
   ```

4. 创建data和log目录

   ```shell
   # 创建数据目录
   sudo mkdir -p /usr/local/var/mongodb
   # 创建日志目录
   sudo mkidr -p /usr/local/var/log/mongodb
   ```

5. 确保使用mongodb的用户拥有data和log目录权限

   使用自己的用户来进行操作，默认就会拥有权限，如果没有的话，可以进行chown操作

   ```shell
   sudo chown my_mongodb_user /usr/local/var/mongodb
   sudo chown my_mongodb_user /usr/local/var/log/mongodb
   ```

6. 运行mongodb

   1. 通过命令行启动

      ```shell
      mongod --dbpath /usr/local/var/mongodb --logpath /usr/local/var/log/mongodb/mongo.log --fork
      ```

      > --dbpath  指定数据目录
      >
      > --logpath 指定日志目录
      >
      > --fork      在后台运行

   2. 通过配置文件启动

      ```shell
      # 指定mongodb以配置文件启动
      mongod --config /usr/local/etc/mongod.conf
      ```

      [官方配置文件选项地址](https://docs.mongodb.com/manual/reference/configuration-options/)

7. 查看mongodb是否启动

   ```shell
   ps aux | grep -v grep | grep mongod
   ```

8. 使用mongodb

   ```shell
   mongo
   ```

> 参考资料

[官方文档](https://docs.mongodb.com/manual/reference/configuration-options/)