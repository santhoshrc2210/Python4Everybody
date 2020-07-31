import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())

tree = ET.fromstring(data)
counts = tree.findall('.//count')
sum=0
for count in counts:
    istr=(count.text)
    i=int(istr)
    sum=i+sum
print('sum:',sum)
