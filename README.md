# python-sock5-client

## sock5服务器
安装3proxy作为sock5的服务端

```shell
yum install -y 3proxy

extip=`ip route get 8.8.8.8|cut -d" " -f8`
socks -d -i0.0.0.0 -e$extip -p1080
```

## 依赖
* Requests
  2.10.0 新版功能

  除了基本的 HTTP 代理，Request 还支持 SOCKS 协议的代理。这是一个可选功能，若要使用， 你需要安装第三方库。
  你可以用 pip 获取依赖:

  ```shell
  $ pip install requests[socks]
  ```

## 用法
返回值为0表示成功，返回值为1表示失败
```shell
$ ./sock5.py 172.28.32.101 1080 http://httpbin.org/ip
{
  "origin": "1.2.3.4"
}

echo $?
```
