#!/bin/bash

role=`id -u`
if test $role -ne 0
then
    echo "运行脚本需要root权限"
    exit 1
fi

command pip --version 1>/dev/null 2>/dev/null
ret=$?
if test $ret -ne 0
then
    echo "需要安装pip"
    exit 1
fi

pip install requests
pip install requests[socks]
