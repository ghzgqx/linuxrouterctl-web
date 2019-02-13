#!/bin/bash
 
echo 'Content-type: text/html'
echo
query=`echo "$QUERY_STRING&"`
do=`echo "$query" |grep -E -o "do=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c4-| grep -E -o "(disable|enable)"|head -1`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body><h2>Web Shell</h2><pre>"
cd a9e019e247226249ddae4694d8f8f2d7b456caba
case "$do" in
enable)
echo "Enable web shell"
echo "cat ./enablewebshell.form > ./a9e019e247226249ddae4694d8f8f2d7b456caba.cgi" |sudo bash
echo "已启用 返回上一页并点击按钮打开Web Shell"
;;
disable)
echo "Disable web shell"
echo "sudo cat ./disablewebshell.form > ./a9e019e247226249ddae4694d8f8f2d7b456caba.cgi" |sudo bash 
echo "已禁用"
;;
*)
echo "Wrong get vars"
;;
esac
echo "</pre></body></html>"