#!/bin/bash
 
echo 'Content-type: text/html'
echo
read query
query=`echo "$query&"|sed "s/%0[aAdD]//g"`
url_encoded="${query//+/ }"
query=`printf '%b' "${url_encoded//%/\\x}"`
rule=`echo "$query" |grep -E -o "rule=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-|head -1| sed "s/[|,;&$]/ /g"`
# html头
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><title>网络设置</title><head><body><h2>nmcli</h2>"
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
		window.location.href = \"./menu.cgi?form=networkmanager\";
	}, false);
</script>"


# 表单输出
echo '<form name="nm" action="./nm.cgi" method="post">
<table style="width:100%;">

<tr>
<td width="10%">nmcli </td>
<td width="90%">
<textarea name="rule" rows="3" style="width:100%; height:100%; word-break: break-all;">'
echo "$rule"
echo '</textarea>
</td>
</tr>
</table>
<input type="submit" value="提交">
<input type="reset" value="重置">
</form>
<p>nmcli [规则]</p>'

echo "<p>输入</p><pre>"
if [[ $CONTENT_LENGTH -lt 1  ]]
then
echo "$rule"
echo "</pre><p>输出</p><pre>CGI: Empty Input</pre></body></html>"
else
echo "$rule"
echo "</pre><p>输出</p><pre>"
sudo nmcli $rule 2>&1
echo "</pre></body></html>"
fi
