#!/bin/bash
 
echo 'Content-type: text/html'
echo
query=`echo "$QUERY_STRING&"`
do=`echo "$query" |grep -E -o "do=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c4-| grep -E -o "(display|save|reload)"|head -1`
type=`echo "$query" |grep -E -o "type=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-| grep -E -o "(IPV4|IPV6)"|head -1`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body>"
case "$do" in
reload)
str=" - 加载"
;;
save)
str=" - 保存"
;;
*)
str=""
;;
esac





case "$type" in
	IPV6|ipv6|IPv6)
		case "$do" in
		display)
		echo "<h2>ip6tables配置文件</h2><pre>"
		sudo r-web display conf fw6
		;;
		*)
		echo "<h2>ip6tables配置文件$str</h2><pre>"
		sudo r-web fw6 $do
		;;
		esac
;;
	IPV4|ipv4|IPv4)
		case "$do" in
		display)
		echo "<h2>iptables配置文件</h2><pre>"
		sudo r-web display conf fw
		;;
		*)
		echo "<h2>iptables配置文件$str</h2><pre>"
		sudo r-web fw $do
	;;
		esac
;;
	*)
		case "$do" in
		display)
		echo "<h2>iptables配置文件</h2><pre>"
		sudo r-web display conf fw
		;;
		*)
		echo "<h2>iptables配置文件$str</h2><pre>"
		sudo r-web fw $do
		;;
		esac
;;
esac

echo "</pre></body></html>"