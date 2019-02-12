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
<td>磁盘信息</td>
<td>
<pre>
$diskinfo
</pre>
</td>
</tr>


</table>"