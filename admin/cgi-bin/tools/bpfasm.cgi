#!/bin/bash
 
echo 'Content-type: text/html'
echo
read query
query=`echo "$query" | ./query_getenv_decode.sh text`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body><h2>BPF编译工具</h2>
<form name=\"bpfcomiler\" action=\"./bpfasm.cgi\" method=\"post\">
<table border=\"1\" width=\"100%\">

<tr>
<td width=\"20%\">Code</td>
<td width=\"80%\">
<textarea name=\"text\"  rows=\"10\" style=\"width:100%; height:100%; word-break: break-all;\">
</textarea>
</td>
</tr>
</table>
<input type=\"submit\" value=\"提交\">
<input type=\"reset\" value=\"重置\"><br><br><br>
"

echo "</pre>输出 </p><pre>"
if [[ $CONTENT_LENGTH -lt 1  ]]
then
echo -e "!!!NO INPUT!!!\n\nDocument:\n\n"
cat ./filter.txt
else
CONTENT_LENGTH=$(($CONTENT_LENGTH-5))
echo "INFO: CONTENT_LENGTH = $CONTENT_LENGTH"
echo -e "Run bpf_asm-x86_64\n"
echo "$query" | tr -d '\r'|./bpf_asm-x86_64.bin 2>&1
fi
echo "</pre></body></html>"