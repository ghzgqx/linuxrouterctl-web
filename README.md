 # linuxrouterctl-web
(自用备份) https://github.com/ghzgqx/linuxrouterctl 的网页版 基于bash+CGI
 
 nat.sh nat6.sh都可以直接用 
 
 r.sh因为其中含有less/more命令因此需要改 全部改成cat
  
 
 在这已放上名为r-web.sh
 
 网络测试部分的traceroute默认使用besttrace linux版 需要增加SUID权限 4755
 
 
 # 注意
 
 注意 这只是个半成品 如果用于生产环境一切后果由使用者自负 使用前必须仔细阅读所有代码 我也不知道这东西有没有BUG
 
 使用本程序需要给apache授权免密码sudo 对此产生的安全问题概不负责 尽量不要与其他网站一起混着跑

 admin/cgi-bin/tools 文件夹内为webshell等测试功能 安全问题不保证 非必须环境下建议删除

 使用这些测试功能时 必须注意安全 请勿用于执行rm等危险操作

 部分功能需要依赖https://github.com/ghzgqx/linuxrouterctl的nat和nat6两个脚本
 
 程序自身没有授权管理 建议使用SSL+服务器自带的htpasswd
 
 # 关于
admin@ghzgqx.com 
2019.1

版权没有 盗版不究 随便用随便改 如果有BUG别找我反馈自己修 需要加啥功能也别找我 自己改
