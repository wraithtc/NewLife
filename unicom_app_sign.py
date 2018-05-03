import pycurl,io,urllib,smtplib
import re
import time
from datetime import datetime, timezone, timedelta

head=['Cookie: Hm_lvt_9208c8c641bfb0560ce7884c36938d9d=1519436096; clientid=36|360; CaptchaCode=RoHCkep1fO0WDHbKNvRj3D6ZNZq4Z5Mzt4YQS57ijBQ=; SHOP_PROV_CITY=; WT_FPC=id=2ff4038c69360e72cdf1508132053769:lv=1524028443393:ss=1524028257673; city=031|310; MUT_S=android8.0.0; _uop_id=npfauth_wc5rxfhh5e1f137b4703ac2a8f37c429ee1cd89efgj2kkoe; MUT_V=android%405.72; currentid4udp=t9PkTzteCiZrxhIph3/aOQ==; _n3fa_cid=1b42e78684a8493b937673f741f451cd; _n3fa_ext=ft=1508132051; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1523002854,1524100906; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1524100906; route5=18425ae75b38e4825b3a0408432b2d1d; SigninApp=z85dhqvYMQrryXQWkyWXj1cC5Rdnf4QGqRQwydNzzMxRhKcJQB2z!-1405711477','Accept-Language: zh-CN,en-US;q=0.9', 'Accept-Encoding: gzip, deflate', 'Referer: https://act.10010.com/SigninApp/signin/querySigninActivity.htm?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE1MjU5MTgyNjgsInRva2VuIjp7ImxvZ2luVXNlciI6IjE4NjAyMTMxMDkyIiwicmFuZG9tU3RyIjoieWh0M0ZsSDExNTI1MzEzNDY4ODAwIn0sImlhdCI6MTUyNTMxMzQ2OH0.QrDvGSuy080Nmu5ozNDYBkNwvcAtakJdihWkZD8kg7roN3qXb3xv7b7XuA698W8lTOpYIpVUVJvLkP_8nebhMQ', 'User-Agent: Mozilla/5.0 (Linux; Android 8.0.0; MIX 2 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36; unicom{version:android@5.72,desmobile:18602131092};devicetype{deviceBrand:Xiaomi,deviceModel:MIX 2}',
'Content-Type: application/x-www-form-urlencoded;charset=UTF-8', 'X-Requested-With: XMLHttpRequest', 'Origin: https://act.10010.com', 'Accept: */*']
buf = io.BytesIO()

c=pycurl.Curl()
c.setopt(pycurl.CONNECTTIMEOUT, 8)
c.setopt(pycurl.WRITEFUNCTION, buf.write)
c.setopt(pycurl.HTTPHEADER, head)
c.setopt(pycurl.URL, 'act.10010.com/SigninApp/signin/daySign.do')
poststr='className=btnPouplePost'
c.setopt(pycurl.POSTFIELDS, poststr.encode())
c.perform()
#fp = open('result.html', 'w')
#fp.write(buf.getvalue().decode('unicode-escape'))
print(buf.getvalue().decode())
c.close()

print(int(time.time()))

