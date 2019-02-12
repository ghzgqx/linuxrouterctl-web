#!/bin/bash
 
echo 'Content-type: text/html'
echo
query=`echo "$QUERY_STRING&"| sed "s/%3A/:/g"`
domain=`echo "$query" |grep -E -o "domain=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c8-| grep -E -o "([a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?|([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})"|head -1`
t=`echo "$query" |grep -E -o "t=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c3-| grep -E -o "[1-5]{1}"|head -1`
type=`echo "$query" |grep -E -o "type=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-| grep -E -o "(IPV4|IPV6)"|head -1`
 echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body><h2>ping</h2><pre>"
case "$type" in
IPV6|ipv6|IPv6)
ping6 -c $t  $domain
;;
IPV4|ipv4|IPv4)
ping -c $t  $domain
;;
*)
ping -c $t  $domain
;;
esac
echo "</pre></body></html>"