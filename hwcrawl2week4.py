import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

p=list()
url = input('Enter - ')
cnt=input('Enter count:')
count=int(cnt)
ps=input('Enter position:')
pos=int(ps)


while count>0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a',limit=pos)
    for tag in tags:
        i=tag.get('href', None)

    url=i
    print('Retrieving:' ,url)
    print(count)
    count=count-1
