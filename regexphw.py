import re
numlist=list()
sum=0
fh=open('regexp_actual.txt')
for line in fh:
    line=line.rstrip()
    y=re.findall('[0-9]+',line)
    if len(y)!=0:
        numlist=y+numlist
    continue
for i in numlist:
    sum=int(i)+sum
print(sum)
