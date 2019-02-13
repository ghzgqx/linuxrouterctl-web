#!/bin/bash
 

query=`echo "$QUERY_STRING&"`
service=`echo "$query" |grep -E -o "service=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c9-| grep -E -o "(fw|fw6|dhcp|dnsmasq|radvd)"|head -1`
case "$service" in
fw|fw6|dhcp|dnsmasq|radvd)
echo "Content-Disposition:attachment;filename=$service.conf.txt"
echo
sudo r-web dis conf $service
;;
*)
echo 'Content-type: text/plain'
echo
echo 'Wrong get vars'
;;
esac