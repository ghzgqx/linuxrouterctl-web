#!/bin/bash
 
echo 'Content-type: text/html'
echo
query=`echo "$QUERY_STRING&"`
type=`echo "$query" |grep -E -o "type=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-| grep -E -o "(log|ip|brd|inet4|inet6|dhcp|dhcp6|radvd)"|head -1`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body>"
case "$type" in
log)
name="系统日志"
;;
ip)
name="接口及IP地址"
;;
brd)
name="网桥"
;;
inet4)
name="路由表 IPv4"
;;
inet6)
name="路由表 IPv6"
;;
dhcp)
name="DHCP分配记录"
;;
dhcp6)
name="DHCPv6分配记录"
;;
radvd)
name="RADVD日志"
;;
*)
name=""
;;
esac
case "$type" in
log|ip|brd|dhcp|dhcp6|radvd)
echo "<h2>$name</h2><br><pre>"
sudo r-web dis $type 2>&1
;;
inet4|inet6)
echo "<h2>$name</h2><br><pre>"
sudo r-web dis route $type 2>&1
;;
*)
echo "Wrong get vars"
;;
esac
echo "</pre></body></html>"