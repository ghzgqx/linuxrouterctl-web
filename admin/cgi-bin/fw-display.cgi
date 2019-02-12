#!/bin/bash
 
echo 'Content-type: text/html'
echo
query=`echo "$QUERY_STRING&"`
table=`echo "$query" |grep -E -o "table=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c7-| grep -E -o "(filter|nat|mangle|raw|all)"|head -1`
type=`echo "$query" |grep -E -o "type=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-| grep -E -o "(IPV4|IPV6)"|head -1`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body><h2>防火墙规则查看</h2>"
case "$type" in
IPV6|ipv6|IPv6)
echo "<p>协议:IPv6 表:$table</p><br /><pre>"
sudo r-web dis fw6 $table
;;
IPV4|ipv4|IPv4)
echo "<p>协议:IPv4 表:$table</p><br /><pre>"
sudo r-web dis fw $table
;;
*)
echo "<p>协议:IPv4 表:$table</p><br /><pre>"
sudo r-web dis fw $table
;;
esac
echo "</pre></body></html>"