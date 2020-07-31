from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum=0
tags=soup('span')
for tag in tags:
    i=tag.get_text() #why did it give only num for text
    #print(i)
    num=int(i)
    sum=num+sum
print(sum)
