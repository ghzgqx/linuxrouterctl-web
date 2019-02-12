#!/bin/bash
 
echo 'Content-type: text/html'
echo
query=`echo "$QUERY_STRING&"|sed "s/%0[aAdD]//g"`
url_encoded="${query//+/ }"
query=`printf '%b' "${url_encoded//%/\\x}"`
rule=`echo "$query" |grep -E -o "rule=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-|head -1| sed "s/[|,;&$]/ /g"`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body><h2>nmcli</h2><p>输出</p><pre>"
sudo nmcli $rule 2>&1
echo "</pre></body></html>"