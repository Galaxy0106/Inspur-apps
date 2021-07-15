## 安装java和scala并配置相关的环境变量
```shell
export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_281
export JRE_HOME=/usr/lib/jvm/jdk1.8.0_281/jre
export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib
export PATH=$JAVA_HOME/bin:$PATH
export SCALA_HOME=/usr/share/scala-2.12.8
```
## 配置免密登录

## 修改etc/hadoop下面的配置文件
```shell
# workers
Master
Slave
```

```shell
# hadoop_env.sh

#设置JAVA_HOME的路径，需要再次指明
export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_281
export HADOOP_HOME=/usr/local/hadoop
#运行对应结点的用户名称，因为涉及到文件夹的权限问题，一定要认真设置
export HDFS_DATANODE_USER=hadoop 
export HDFS_SECONDARYDATANODE_USER=hadoop
export HDFS_NAMENODE_USER=hadoop
export YARN_RESOURCEMANAGER_USER=hadoop
export YARN_NODEMANAGER_USER=hadoop
```

```shell
# core-site.xml

<configuration>
        <property>
                <name>fs.defaultFS</name>
                <value>hdfs://Master:9000</value>
        </property>
        <property>
                <name>hadoop.tmp.dir</name>
                <value>file:/usr/local/hadoop/tmp</value>
                <description>Abase for other temporary directories.</description>
        </property>
</configuration>
```

```shell
# hdfs-site.xml

<configuration>
    <property>
        <name>dfs.namenode.secondary.http-address</name>
        <value>Master50090</value>
    </property>
    <property>
        <name>dfs.replication</name>
        <value>2</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///data/hadoop/hdfs/nn</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///data/hadoop/hdfs/dn</value>
    </property>
</configuration>
```

```shell
# mapred-site.xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>mapreduce.jobhistory.address</name>
        <value>Master:10020</value>
    </property>
    <property>
        <name>mapreduce.jobhistory.webapp.address</name>
        <value>Master:19888</value>
    </property>
</configuration>
```

```shell
#yarn-site.xml

<configuration>
                <!-- 指定ResourceManager的地址-->
                <property>
                    <name>yarn.resourcemanager.hostname</name>
                    <value>Masterhadoop</value>
                </property>
                <!-- 指定reducer获取数据的方式-->
                <property>
                    <name>yarn.nodemanager.aux-services</name>
                    <value>mapreduce_shuffle</value>
                </property>
                <property>
                    <name>yarn.nodemanager.local-dirs</name>
                    <value>file:///data/hadoop/yarn/nm</value>
                </property>
</configuration>
```


