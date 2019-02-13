#!/bin/bash
read query
query="$query&"
length=${#1}
length=$(($length+2))
query=`echo "$query" |grep -E -o "$1=[^&]{1,}&"| sed  's/\(.\)\{1\}$//'|cut -c${length}- |head -1`
url_encoded="${query//+/ }"
query=`printf '%b' "${url_encoded//%/\\x}"`
echo "$query"