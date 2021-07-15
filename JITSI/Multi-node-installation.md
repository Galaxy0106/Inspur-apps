## 简介
在单结点的环境中，我们在一个结点上同时安装了Jitsi-meet、prosody、Jicofo和Jitsi-video-bridge，单结点的容错性显然是不行的，为了测试集群的高可用性，我们在这里进行多结点的安装，其中一个结点作为管理结点，安装上述的所有组件，而其余结点安装Jitsi-video-bridge，用来做负载均衡，注意Jitsi-video-bridge是真正用于视频的处理以及传输的。
## 环境准备
3台Virtualbox虚拟机，基础配置均与单结点安装的虚拟机相同  
JMS：
    Host-only IP：192.168.56.105
JVB1：
    Host-only IP：192.168.56.106
JVB2：
    Host-only IP：192.168.56.107
## 设置防火墙
JMS的防火墙除了单结点安装中的配置之外还需要开放用于和JVB通信的端口
```shell
sudo ufw allow 5222/tcp
```
另外我们还需要进行其余结点的防火墙配置
```shell
sudo ufw status
sudo ufw allow ssh
sudo ufw allow 443/tcp
sudo ufw allow 4443/tcp
sudo ufw allow 10000:20000/udp
sudo ufw enable
```
## 安装jitsi-videobridge
添加源并安装jitsi-videobridge
```shell
sudo echo 'deb https://download.jitsi.org stable/' >> /etc/apt/sources.list.d/jitsi-stable.list
wget -qO -  https://download.jitsi.org/jitsi-key.gpg.key | apt-key add -
sudo apt-get install apt-transport-https
sudo apt update
sudo apt upgrade
sudo apt -y install jitsi-videobridge
```
安装期间指定域名为JMS的IP：192.168.56.105
## 配置文件修改
将配置文件修改如下：
```shell
# JMS
org.ice4j.ice.harvest.DISABLE_AWS_HARVESTER=true
org.ice4j.ice.harvest.STUN_MAPPING_HARVESTER_ADDRESSES=meet-jit-si-turnrelay.jitsi.net:443
org.jitsi.videobridge.ENABLE_STATISTICS=true
org.jitsi.videobridge.STATISTICS_TRANSPORT=muc
org.jitsi.videobridge.xmpp.user.shard.HOSTNAME=192.168.56.105
org.jitsi.videobridge.xmpp.user.shard.DOMAIN=auth.192.168.56.105
org.jitsi.videobridge.xmpp.user.shard.USERNAME=jvb
org.jitsi.videobridge.xmpp.user.shard.PASSWORD=rxkseNDh
org.jitsi.videobridge.xmpp.user.shard.MUC_JIDS=JvbBrewery@internal.auth.192.168.56.105
org.jitsi.videobridge.xmpp.user.shard.MUC_NICKNAME=jvb
# JVB
org.ice4j.ice.harvest.DISABLE_AWS_HARVESTER=true
org.ice4j.ice.harvest.STUN_MAPPING_HARVESTER_ADDRESSES=meet-jit-si-turnrelay.jitsi.net:443
org.jitsi.videobridge.ENABLE_STATISTICS=true
org.jitsi.videobridge.STATISTICS_TRANSPORT=muc
org.jitsi.videobridge.xmpp.user.shard.HOSTNAME=192.168.56.105
org.jitsi.videobridge.xmpp.user.shard.DOMAIN=auth.192.168.56.105
org.jitsi.videobridge.xmpp.user.shard.USERNAME=jvb
org.jitsi.videobridge.xmpp.user.shard.PASSWORD=rxkseNDh
org.jitsi.videobridge.xmpp.user.shard.MUC_JIDS=JvbBrewery@internal.auth.192.168.56.105
org.jitsi.videobridge.xmpp.user.shard.MUC_NICKNAME=jvb1
org.jitsi.videobridge.xmpp.user.shard.DISABLE_CERTIFICATE_VERIFICATION=true
# 其余JVB类似
```
## 重启服务
```shell
sudo /etc/init.d/jitsi-videobridge2 restart
```
## 查看日志
```shell
# JMS
tail -f /var/log/jitsi/jvb.log 
tail -f /var/log/jitsi/jicofo.log
# jicofo的日志因该有vedio bridge添加成功的信息
# JVB
tail -f /var/log/jitsi/jvb.log
```
## 验证
```shell
# 关闭JMS上的jitsi-videobridge2服务
/etc/init.d/jitsi-videobridge2 stop
# 依然正常工作
# 如果所有结点的jitsi-videobridge2服务全部关闭，则无法正常工作
# 重新开启一个结点上的jitsi-videobridge2服务，恢复正常工作
```