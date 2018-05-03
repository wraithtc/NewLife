import pycurl,io,urllib,certifi,smtplib
import re
import time
from datetime import datetime, timezone, timedelta
c=pycurl.Curl()

c.setopt(pycurl.CONNECTTIMEOUT, 8)
head=['Accept-Encoding: gzip','User-Agent: Dalvik/2.1.0 (Linux; U; Android 8.0.0; MIX 2 MIUI/V9.5.5.0.ODECNFA)',\
        'Cookie: cUserId=VcDVRCr8TOh9fiojlfKy78eaolw;serviceToken=dg5GsxJs6MPEIdUCYUR8k4BCveDwfYSl1dlGGYOM5a0fkWgr7CH89WgElbzX9Whg3btOy4hR%2BlBaJAQ9M6pQgje7IXlvstRfqsvxqjIAIVRQh0BA%2FZXHKDBZtVV6G2xs5KcNivjGtFOrJxF0jvpPEg9yxdRahsUAkpjQ1Y887Fc%3D,4Wusn801KF8vozRO6gm6zA==','X-MIUI-VersionType: stable','X-Device: chiron','X-Imei: e13e45d3557cca212dee3718b1e96dbc',\
        'Accept-Language: zh-CN','X-Model: MIX 2','X-MIUI-VersionName: V9', 'X-App-Version: 3.0.4', 'X-MIUI-VersionIncremental: V9.5.5.0.ODECNFA']

buf = io.BytesIO()
#c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(pycurl.WRITEFUNCTION, buf.write)
c.setopt(pycurl.HTTPHEADER, head)
c.setopt(pycurl.URL, 'api.bbs.miui.com/app/user/syncSubscribes')

poststr='subscribes=topic-0%2Ctopic-6%2Ctopic-7%2Ctopic-8%2Ctopic-1%2Ctopic-2%2Ctopic-3%2Ctopic-4%2Ctopic-5&timestamp='+str(int(time.time()))+'&'
c.setopt(pycurl.POSTFIELDS, str.encode(poststr))
c.perform()
#fp = open('result.html', 'w')
#fp.write(buf.getvalue().decode('gbk')) 
print(buf.getvalue())
c.close()
