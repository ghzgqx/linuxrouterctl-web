#!/bin/bash
hostname=`hostname`
cpunumber=`cat /proc/cpuinfo |grep "model name" |wc -l`
cpumodel=`cat /proc/cpuinfo |grep "model name" |cut -c14-|head -1`
uptime=`uptime -p|cut -c3- |sed 's/^[ \t]*//g'|head -1`
loadave=`uptime |grep -E -o "average:.{1,}"|cut -c9-|sed 's/^[ \t]*//g'|head -1`
memtotal=`cat /proc/meminfo |grep MemTotal |cut -c10-|sed 's/^[ \t]*//g'`
memfree=`cat /proc/meminfo |grep MemFree |cut -c9-|sed 's/^[ \t]*//g'`
sysname=`cat /etc/os-release |grep -E "^PRETTY_NAME=[[:graph:] ]{1,}"|cut -c13-|sed "s/\"//g"`
kernel=`uname -r -p`
diskinfo=`df -h`
localipv4=`ip addr|grep inet|grep -v inet6|awk '{print $2}'|grep -E -v  "^(127.0.0.1)"|sed 's/$/<br>/'`
localipv6=`ip addr|grep inet6|awk '{print $2}'|grep -E -v  "^(::1/128)"|sed 's/$/<br>/'`
traffic=`sudo  cat /proc/net/dev | grep -v "|" | awk '{split($1,b,":");print "<tr><td>"b[1]"</td><td>"$2"</td><td>"$10"</td></tr>" }'`
session=`sudo cat /proc/net/nf_conntrack |wc -l`
conntrackmax=`sysctl -n net.netfilter.nf_conntrack_max`
ipfwd=`sysctl -n net.ipv4.ip_forward`
ip6fwd=`sysctl -n net.ipv6.conf.all.forwarding`
pct=`printf '%06d' $((($session*100000)/$conntrackmax))`
 echo "<p>状态</p>"
echo "<table>
<tr>
<td>主机名</td>
<td>
$hostname
</td>
</tr>
<tr>
<td>CPU</td>
<td>
$cpumodel ~$cpunumber CPU 
</td>
</tr>

<tr>
<td>系统版本</td>
<td>
$sysname
</td>
</tr>

<tr>
<td>内核版本</td>
<td>
$kernel
</td>
</tr>

<tr>
<td>全局IP转发</td>
<td>
IPv4 $ipfwd IPv6 $ip6fwd
</td>
</tr>
<tr>
<td>活动连接数</td>
<td>
当前 $session 上限 $conntrackmax &nbsp;&nbsp;&nbsp;&nbsp;${pct:0:3}.${pct:3}%
</td>
</tr>
<tr>
<td>内存</td>
<td>
总量 $memtotal 空闲 $memfree
</td>
</tr>
<tr>
<td>负载</td>
<td>
$loadave
</td>
</tr>
<tr>
<td>运行时间</td>
<td>
$uptime
</td>
</tr>
<tr>
<td>接口/流量</td>
<td>
<table>
<tr><th>Interface</th><th>RX(Byte)</th><th>TX(Byte)</th></tr>
$traffic
</table>
</td>
</tr>
<tr>
<td>IPv4</td>
<td>
$localipv4
</td>
</tr>
<tr>
<td>IPv6</td>
<td>
$localipv6
</td>
</tr>
<tr>
<td>磁盘信息</td>
<td>
<pre>
$diskinfo
</pre>
</td>
</tr>


</table>"
