#!/bin/bash
 
echo 'Content-type: text/html'
echo
read query
query="$query&"
url_encoded="${query//+/ }"
query=`printf '%b' "${url_encoded//%/\\x}"`
table=`echo "$query" |grep -E -o "table=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c7-| grep -E -o "(filter|nat|mangle|raw|all)"|head -1`
type=`echo "$query" |grep -E -o "type=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-| grep -E -o "(A|D|R|I|Custom)"|head -1`
num=`echo "$query" |grep -E -o "num=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c5-| grep -E -o "[0-9]{1,}"|head -1`
rule=`echo "$query" |grep -E -o "rule=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-|head -1| sed "s/[|,;&$]/ /g"`
chain=`echo "$query" |grep -E -o "chain=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c7-| grep -E -o "(INPUT|OUTPUT|FORWARD|POSTROUTING|PREROUTING)"|head -1`
protocol=`echo "$query" |grep -E -o "protocol=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c10-| grep -E -o "(IPV4|IPV6)"|head -1`
enablenum=`echo "$query" |grep -E -o "enablenum=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c11- |grep -E -o "1{1}" |head -1`
# html头
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><title>防火墙规则设置</title><head><body>"
# 防后退时重新执行命令
echo "<script type=\"text/javascript\">
	function addUrl() {
		var state = {
			title: \"title\",
			url: \"#\"
		};
		window.history.pushState(state, \"title\", \"#\");
	}
	
	addUrl();addUrl();addUrl();addUrl();

	window.addEventListener(\"popstate\", function(e) {
		window.location.href = \"./menu.cgi?form=firewall\";
	}, false);
</script>"

# 表单输出
echo '<h2>防火墙规则设置</h2>
<form name="firewall" action="./fw.cgi" method="post">
<table>
<tr>
<td>协议</td>
<td>
<input type="radio" name="protocol" value="IPV4" checked>IPV4
<input type="radio" name="protocol" value="IPV6">IPV6
</td>
</tr>
<tr>
<td>操作</td>
<td>
<input type="radio" name="type" value="A">增加
<input type="radio" name="type" value="D">删除
<input type="radio" name="type" value="I">插入
<input type="radio" name="type" value="R">替换
<input type="radio" name="type" value="Custom" checked>运行自定义规则
</td>
</tr>
<tr>
<td>表(自定义规则本行无效)</td>
<td>
<input type="radio" name="table" value="filter" checked>filter
<input type="radio" name="table" value="nat">nat
<input type="radio" name="table" value="raw">raw
<input type="radio" name="table" value="mangle">mangle
</td>
</tr>
</tr>
<td>链(自定义规则本行无效)</td>
<td>
<input type="radio" name="chain" value="INPUT" checked>INPUT
<input type="radio" name="chain" value="OUTPUT">OUTPUT
<input type="radio" name="chain" value="FORWARD">FORWARD
<input type="radio" name="chain" value="PREROUTING">PREROUTING
<input type="radio" name="chain" value="POSTROUTING">POSTROUTING

</td>
</tr>
<tr>
<td>序号</td>
<td>
<input type="number" name="num" value="1"> <input type="checkbox" name="enablenum" value="1">启用本行
</td>
</tr>
<tr>
<td>规则</td>
<td>
<input type="text" name="rule">
</td>
</tr>
</table>
<input type="submit" value="提交">
<input type="reset" value="重置">
</form>
'






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
echo "<p>输入</p><pre>"
case "$type" in
	A)
	echo "$command -t $table -$type $chain $rule"
	echo "</pre><p>$command 输出</p><pre>"
	echo ""
    sudo $command -t $table -$type $chain $rule 2>&1
	;;
	R|I)
if [ "$enablenum" = "1" ]
			then
				echo "$command -t $table -$type $chain $num $rule"
				echo "</pre><p>$command 输出</p><pre>"
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
				echo "</pre><p>$command 输出</p><pre>"
				echo ""
				sudo $command -t $table -$type $chain $num 2>&1
			else
			    echo "$command -t $table -$type $chain $rule"
				echo "</pre><p>$command 输出</p><pre>"
				echo ""
			    sudo $command -t $table -$type $chain $rule 2>&1
			fi
	;;
Custom)
    echo "$command $rule"
	echo "</pre><p>$command 输出</p><pre>"
	echo ""
	sudo $command $rule 2>&1
	;;
*)
	echo "</pre><p>输出</p><pre>CGI: Failed to generate command! Wrong or empty input!"
	;;
	esac
	echo "</pre></body><html>"
