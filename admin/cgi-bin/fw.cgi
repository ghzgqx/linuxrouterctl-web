#!/bin/bash
 
echo 'Content-type: text/html'
echo
query="$QUERY_STRING&"
url_encoded="${query//+/ }"
query=`printf '%b' "${url_encoded//%/\\x}"`
table=`echo "$query" |grep -E -o "table=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c7-| grep -E -o "(filter|nat|mangle|raw|all)"|head -1`
type=`echo "$query" |grep -E -o "type=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-| grep -E -o "(A|D|R|I|Custom)"|head -1`
num=`echo "$query" |grep -E -o "num=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c5-| grep -E -o "[0-9]{1,}"|head -1`
rule=`echo "$query" |grep -E -o "rule=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-|head -1| sed "s/[|,;&$]/ /g"`
chain=`echo "$query" |grep -E -o "chain=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c7-| grep -E -o "(INPUT|OUTPUT|FORWARD|POSTROUTING|PREROUTING)"|head -1`
protocol=`echo "$query" |grep -E -o "protocol=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c7-| grep -E -o "(IPV4|IPV6)"|head -1`
enablenum=`echo "$query" |grep -E -o "enablenum=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c11- |grep -E -o "1{1}" |head -1`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body>"
if [ "$enablenum" != "1" ]
			then
			#	enablenum="1"
		#	else
			    enablenum="0"
			fi


case "$protocol" in 

IPV6|ipv6|IPv6)
command="ip6tables"
;;
IPV4|ipv4|IPv4)
command="iptables"
;;
*)
command="iptables"
;;
esac
echo "<h2>$command</h2><p>输出</p><pre>"
echo "Generating command..."
case "$type" in
	A)
	echo "$command -t $table -$type $chain $rule"
	echo "Execute..."
	echo ""
    sudo $command -t $table -$type $chain $rule 2>&1
	;;
	R|I)
if [ "$enablenum" = "1" ]
			then
				echo "$command -t $table -$type $chain $num $rule"
				echo "Execute..."
				echo ""
				sudo $command -t $table -$type $chain $num $rule 2>&1
			else
			    echo "Must enable line number!"
			fi
	;;
	D)
if [ "$enablenum" = "1" ]
			then
			    echo "$command -t $table -$type $chain $num"
				echo "Execute..."
				echo ""
				sudo $command -t $table -$type $chain $num 2>&1
			else
			    echo "$command -t $table -$type $chain $rule"
				echo "Execute..."
				echo ""
			    sudo $command -t $table -$type $chain $rule 2>&1
			fi
	;;
Custom)
    echo "$command $rule"
	echo "Execute..."
	echo ""
	sudo $command $rule 2>&1
	;;
*)
	echo "Wrong get vars"
	;;
	esac
    echo ""
	echo "Done."
	echo "</pre></body><html>"