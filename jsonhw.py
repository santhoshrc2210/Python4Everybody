import urllib.request, urllib.parse, urllib.error
import ssl
import json

url = input('Enter location: ')
uh = urllib.request.urlopen(url)
data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())

info = json.loads(data)
usflinfo=info['comments']
sum=0
for i in usflinfo:
    num=(i['count'])
    inum=int(num)
    sum=sum+inum
print('sum:',sum)    
