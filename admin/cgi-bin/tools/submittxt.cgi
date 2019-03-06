#!/bin/bash
 
echo 'Content-type: text/html'
echo
read query
query=`echo "$query" | ./query_getenv_decode.sh text`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body><h2>文本文件提交工具</h2>
<form name=\"webshell\" action=\"./submittxt.cgi\" method=\"post\">
<table border=\"1\" width=\"100%\">

<tr>
<td width=\"20%\">Text</td>
<td width=\"80%\">
<textarea name=\"text\"  rows=\"5\" style=\"width:100%; height:100%; word-break: break-all;\">
</textarea>
</td>
</tr> 
</table>
<input type=\"submit\" value=\"提交\">
<input type=\"reset\" value=\"重置\">"


echo "</pre>输出 </p><pre>" 

if [[ $CONTENT_LENGTH -lt 1  ]]
then
echo "ERROR:  CONTENT_LENGTH =  $CONTENT_LENGTH"
else
echo "INFO: CONTENT_LENGTH = $CONTENT_LENGTH"
echo "当前文件内容:"
echo "echo \"$query\" > ./temp.txt" |bash 
cat ./temp.txt |sed 's/</\&lt;/g' |sed 's/>/\&gt;/g'
fi
echo "</pre></body></html>"