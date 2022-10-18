# ThinkPHP 5.0.23 RCE Vulnerability

```
----------------------------------
Title: ThinkPHP 5.0.23 RCE
CVE: CVE-2018-20062
Written By: https://github.com/ChinaRan0
Modified By: https://github.com/0xRar
----------------------------------
```

## Help
```
usage: ThinkPHP5_RCE.py [-h] -d DOMAIN -p PORT

arguments:
  -h, --help  show this help message and exit
  -d DOMAIN   The target's domain
  -p PORT     The thinkphp running port

Example: python ThinkPHP5_RCE.py -d domain.com -p 8080
```

## Reference
- https://nvd.nist.gov/vuln/detail/CVE-2018-20062
- https://www.rapid7.com/db/vulnerabilities/thinkphp-cve-2018-20062/
- https://github.com/top-think/framework/commit/4a4b5e64fa4c46f851b4004005bff5f3196de003
- VulnLab: https://github.com/vulhub/vulhub/tree/master/thinkphp/5.0.23-rce
