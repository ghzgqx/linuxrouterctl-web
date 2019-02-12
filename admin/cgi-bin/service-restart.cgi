#!/bin/bash
 
echo 'Content-type: text/html'
echo
query=`echo "$QUERY_STRING&"`
service=`echo "$query" |grep -E -o "service=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c9-| grep -E -o "(fw|fw6|dhcp|dnsmasq|radvd)"|head -1`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body>"
case "$service" in
fw)
name="iptables"
;;
fw6)
name="ip6tables"
;;
dhcp)
name="dhcpd"
;;
dnsmasq)
name="dnsmasq"
;;
radvd)
name="radvd"
;;
*)
name=""
;;
esac

case "$service" in
fw|fw6|dhcp|dnsmasq|radvd)
echo "<h2>服务重启:$name</h2><p>输出：</p><pre>"
echo "Restart service"
sudo r-web restart $service 2>&1
;;
*)
echo "Wrong get vars"
;;
esac
echo "</pre></body></html>"