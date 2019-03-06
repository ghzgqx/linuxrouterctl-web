#!/bin/bash
 
echo 'Content-type: text/html'
echo
query=`echo "$QUERY_STRING&"| sed "s/%3A/:/g"`
domain=`echo "$query" |grep -E -o "domain=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c8-| grep -E -o "([a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?|([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})"|head -1`
t=`echo "$query" |grep -E -o "t=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c3-| grep -E -o "[1-5]{1}"|head -1`
 echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><title>traceroute</title><head><body><h2>traceroute</h2><pre>"
besttrace -q $t -g en $domain
echo "</pre></body></html>"