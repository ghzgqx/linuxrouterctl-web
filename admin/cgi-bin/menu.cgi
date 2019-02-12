#!/bin/bash
 
echo 'Content-type: text/html'
echo
query="$QUERY_STRING&"
url_encoded="${query//+/ }"
query=`printf '%b' "${url_encoded//%/\\x}"`
form=`echo "$query" |grep -E -o "form=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c6-|grep -E -o "[a-zA-Z0-9]{1,}"|head -1`
loadtime=`date "+%Y-%m-%d %H:%M:%S"`
sysname=`cat /etc/os-release |grep -E "^PRETTY_NAME=[[:graph:] ]{1,}"|cut -c13-|sed "s/\"//g"`
echo "<html><head><meta charset=\"utf-8\">
<meta http-equiv=\"Content-Style-Type\" content=\"text/css\" />
<link rel=\"stylesheet\" href=\"./md.css\" type=\"text/css\" /><head><body>"
echo "<table border=\"1\" width=\"100%\">
	<tr>
	<td width=\"20%\"><a href=\"./menu.cgi\">系统状态<a>&nbsp;&nbsp;&nbsp;&nbsp;<a href=\"../..\">首页</a></td>
	<td width=\"80%\" >系统版本: $sysname</td>
	</tr>
	<tr>
		<td>菜单</td>
		<td rowspan=\"23\" width=\"80%\" valign=\"top\">"
		
		if [ "$form" = "" ]
			then
				./about.cgi
			else
			    cat /var/www/ssl/admin/form/$form.form 2>&1
			fi
	

echo "</td>
	</tr>
	<tr>
		<td>▶防火墙设置</td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=displayrules\">-规则查看</a></td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=firewallconfig\">-配置文件</a></td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=firewall\">-在线规则修改</a></td>
	</tr>
	<tr>
		<td>▶NAT</td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=natrules\">-运行规则查看</a></td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=portforward\">-端口映射</a></td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=masquerade\">-IP共享设置</a></td>
	</tr>
	<tr>
		<td>▶网络设置</td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=networkmanager\">-接口/IP/路由表设置</a></td>
	</tr>
	<tr>
		<td>▶系统服务</td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=servicestatus\">-服务状态查询</a></td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=servicerestart\">-服务重启</a></td>
	</tr>
	<tr>
		<td>▶系统日志</td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=systemlog\">-信息和日志查询</a></td>
	</tr>
	<tr>
		<td>▶网络测试</td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=ping\">-PING</a></td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=traceroute\">-路由跟踪</a></td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=dig\">-DNS</a></td>
	</tr>
	<tr>
		<td>▶命令行和高级设置</td>
	</tr>
	<tr>
		<td><a href=\"./menu.cgi?form=ssh\">-SSH</a></td>
	</tr>
	<tr>
		<td>页面生成时间</td>
	</tr>
	<tr><td colspan=\"2\">$loadtime </td></tr>
</table>
"
	
	
	
echo "</body></html>"