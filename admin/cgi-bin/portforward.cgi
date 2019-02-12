#!/bin/bash
 
echo 'Content-type: text/html'
echo
query="$QUERY_STRING&"
url_encoded="${query//+/ }"
query=`printf '%b' "${url_encoded//%/\\x}"`
type=`echo "$query" |grep -E -o "type=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-| grep -E -o "(add|del)"|head -1`
protocol=`echo "$query" |grep -E -o "protocol=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c10-| grep -E -o "(IPV4|IPV6)"|head -1`
lanip=`echo "$query" |grep -E -o "lanip=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c7-| sed "s/[;|$&]/ /g" |grep -o -E "[[:graph:]]{1,}"|head -1`
wanif=`echo "$query" |grep -E -o "wanif=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c7-| sed "s/[;|$&]/ /g"|grep -o -E "[[:graph:]]{1,}"|head -1`
lanport=`echo "$query" |grep -E -o "lanport=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c9-| sed "s/[;|$&]/ /g" |grep -o -E "[[:graph:]]{1,}"|head -1`
wanport=`echo "$query" |grep -E -o "wanport=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c9-| sed "s/[;|$&]/ /g"|grep -o -E "[[:graph:]]{1,}"|head -1`
protocol4=`echo "$query" |grep -E -o "protocol4=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c11-| grep -E -o "(tcp|udp)"|head -1`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body><h2>nat port forward</h2><p>输出</p><pre>"
echo "$protocol type=$type lanip=$lanip  lanport=$lanport wanif=$wanif wanport=$wanport protocol=$protocol4 "

case "$protocol" in 
IPV6|ipv6|IPv6)
command="nat6"
;;
IPV4|ipv4|IPv4)
command="nat"
;;
*)
echo "Must specify IP protocol versiom"
echo "</pre></body></html>"
exit
;;
esac

case "$type" in
	add|del)
	echo "Generating command..."
	echo "$command $type pf $protocol4 $lanip $lanport $wanif $wanport"
	echo "Execute..."
    sudo $command $type pf $protocol4 $lanip $lanport $wanif $wanport 2>&1
	;;
*)
	echo "Wrong get vars"
	echo "</pre></body></html>"
	exit
	;;
	esac
    echo ""
	echo "Done."
	echo "</pre></body></html>"