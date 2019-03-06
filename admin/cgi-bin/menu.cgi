#!/bin/bash
 
echo 'Content-type: text/html'
echo
query="$QUERY_STRING&"
url_encoded="${query//+/ }"
query=`printf '%b' "${url_encoded//%/\\x}"`
form=`echo "$query" |grep -E -o "form=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-|grep -E -o "[a-zA-Z0-9]{1,}"|head -1`
loadtime=`date "+%Y-%m-%d %H:%M:%S"`
sysname=`cat /etc/os-release |grep -E "^PRETTY_NAME=[[:graph:] ]{1,}"|cut -c13-|sed "s/\"//g"`
linenumber=`cat /var/www/ssl/admin/form/menu.form|grep -v -E "^([\s]| ){0,}$"|wc -l`
echo "<html>
<!-- CGI OUTPUT HTTP HEAD -->
<head><meta charset=\"utf-8\"><title>管理页</title><meta http-equiv=\"Content-Style-Type\" content=\"text/css\" /><link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body>"
echo "<!-- CGI OUTPUT HTTP BODY TABLE HEAD -->
<table  width=\"100%\">
<tr>
<td width=\"20%\" bgcolor=\"#88CCFF\"><a href=\"./menu.cgi\" style=\"color:#FFFFFF;text-decoration:none;\">[系统状态]</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href=\"../..\" style=\"color:#FFFFFF;text-decoration:none;\">[首页]</a></td>
<td width=\"80%\" bgcolor=\"#88CCFF\" ><font color=\"black\">系统版本: $sysname</p></td>
</tr>
<tr><td bgcolor=\"#88CCFF\">菜单</td><td rowspan=\"$linenumber\" width=\"80%\" valign=\"top\">"
		
		if [ "$form" = "" ]
			then
			    echo "<!-- CGI OUTPUT run about.cgi -->"
				./about.cgi
			else
			    echo "<!-- CGI OUTPUT cat $form.form -->"
			    cat /var/www/ssl/admin/form/$form.form 2>&1
			fi
	echo "<!-- CGI OUTPUT MAIN MENU -->"
	cat /var/www/ssl/admin/form/menu.form
	echo "<!-- CGI OUTPUT GENERATE TIME -->
	<tr><td bgcolor=\"#88CCFF\"><font color=\"#FFFFF\">页面生成时间</font></td></tr><tr><td colspan=\"2\" bgcolor=\"#88CCFF\"><font color=\"#FFFFF\">$loadtime</font></td></tr></table>"
	echo "</body></html>"