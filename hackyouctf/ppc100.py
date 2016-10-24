import requests
from requests import Session, Request
import re
import base64

s= Session()

s.get('http://hackyou-captcha.ctf.su/')
#r=Request('POST','http://hackyou-captcha.ctf.su/',data={}, headers={})
r = s.get('http://hackyou-captcha.ctf.su/')

print(r.text)
p2=re.compile('<code>[a-zA-Z0-9=]*</code>',re.IGNORECASE)

t=p2.findall(r.text)

print(t[0][6:len(t[0])-7:1])
ans=base64.b64decode(t[0][6:len(t[0])-7:1]).decode('ISO-8859-1')

print(ans)

r2=s.post('http://hackyou-captcha.ctf.su/',data={'answer':ans})

print (r2.text)

