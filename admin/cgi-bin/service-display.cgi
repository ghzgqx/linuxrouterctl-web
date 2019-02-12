#!/bin/bash
 
echo 'Content-type: text/html'
echo
query=`echo "$QUERY_STRING&"`
service=`echo "$query" |grep -E -o "service=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c9-| grep -E -o "(fw|fw6|dhcp|dnsmasq|radvd|network|nm)"|head -1`
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
network)
name="network"
;;
nm)
name="NetworkManager"
;;
*)
name=""
;;
esac
case "$service" in
fw|fw6|dhcp|dnsmasq|radvd|network|nm)
echo "<h2>服务状态:$name</h2><br><pre>"
sudo r-web status $service 2>&1
;;
*)
echo "Wrong get vars"
;;
esac
echo "</pre></body></html>"