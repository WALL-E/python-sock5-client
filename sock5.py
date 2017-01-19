#!/usr/bin/env python

import os
import sys
import requests


def main():
    if len(sys.argv) < 3:
        print "%s sock5_host sock5_port [url]" % (sys.argv[0])
        sys.exit(1)

    host = sys.argv[1]
    port = sys.argv[2]
    proxies = {
        'http': 'socks5://%s:%s' % (host, port),
        'https': 'socks5://%s:%s' % (host, port)
    }

    try:
        url = sys.argv[3]
    except IndexError:
        url = "http://httpbin.org/ip"

    response = requests.get(url, proxies=proxies)
    print "%s" % (response.text)


if __name__ == '__main__':
    main()
