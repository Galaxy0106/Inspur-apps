# 环境准备
## 备注
由于是做初步实验，因此这里采用的是Virtualbox虚拟机，公网IP暂时用Host-only网络的IP代替，相应地也没有申请域名，后续大规模测试的时候会加上这些部分  
## 安装环境
- OS：Ubuntu20.04  
- RAM：4G  
- CPU：1vcpu  
- Network：
    NAT网络用于访问外网 
    Host-only网络用于和主机通信  
# 配置防火墙
```shell
sudo ufw allow 80/tcp  
sudo ufw allow 443/tcp 
sudo ufw allow 4443/tcp
sudo ufw allow 10000/udp
sudo ufw allow OpenSSH   

sudo ufw enable
sudo ufw status
```
# 安装JITSI-meet
## 下载安装并添加密钥
```shell
wget https://download.jitsi.org/jitsi-key.gpg.key
sudo apt-key add jitsi-key.gpg.key
```
## 添加软件源
```shell
echo "deb https://download.jitsi.org stable/" > /etc/apt/sources.list.d/jitsi-stable.list
```
## 更新源并安装
```shell
sudo apt update
sudo apt -y install jitsi-meet
```
安装期间指定域名为IP地址  
默认生成SSL证书即可
# 使用
在主机浏览器上输入虚拟机Host-only的IP，新建会议进行测试