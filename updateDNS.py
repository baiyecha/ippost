#!/usr/bin/env python
# coding=utf8
import requests, socket, re


def pars_domin(url):
    res = socket.getaddrinfo(url, None)
    return res[0][4][0]


def get_self_ip():
    res = requests.get("https://github.com/baiyecha/ippost/blob/master/ip")
    return re.search(
        r'<td id="LC1" class="blob-code blob-code-inner js-file-line">(.+?)</td>',
        res.text,
    ).group(1)


# https://support.dnspod.cn/api/5f562a49e75cf42d25bf6872/
# curl -X POST https://dnsapi.cn/Record.Modify -d 'login_token=LOGIN_TOKEN&format=json&domain_id=2317346&record_id=16894439&sub_domain=www&value=3.2.2.2&record_type=A&record_line_id=10%3D0'
def update_DNS(self_ip):
    payload = {
        "login_token": "180547,485ceda4bcb7cbdc7327fa48e54cc853",
        "format": "json",
        "domain": "huyongkang.icu",
        "record_id": "658420967",
        "value": self_ip,
        "record_type": "A",
        "sub_domain": "www",
        "record_line": "默认",
    }
    res = requests.post("https://dnsapi.cn/Record.Modify", data=payload)
    print(res.content)


if __name__ == "__main__":
    domin_ip = pars_domin("www.huyongkang.icu")
    self_ip = get_self_ip()
    if domin_ip != self_ip:
        print("self_ip:", self_ip, "domin_ip", domin_ip)
        update_DNS(self_ip)
