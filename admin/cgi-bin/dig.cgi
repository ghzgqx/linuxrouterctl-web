#!/bin/bash
 
echo 'Content-type: text/html'
echo
query="$QUERY_STRING&"
domain=`echo "$query" |grep -E -o "domain=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c8-| grep -E -o "([a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?|([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})"|head -1`
dns=`echo "$query" |grep -E -o "dns=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c5-| grep -E -o "([a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?|([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4})"|head -1`
type=`echo "$query" |grep -E -o "type=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-|grep -o -E "[a-zA-Z0-9]{0,}"|head -1`
 echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><title>dig</title><head><body><h2>dig</h2><pre>"
if [ "$dns" = "" ]
then
dig $domain $type
else
dig $domain $type @$dns
fi
echo "</pre></body></html>"