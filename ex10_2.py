han=open('mbox-short.txt')
counts=dict()
sndr=list()
for line in han:
    line=line.rstrip()
    wds=line.split()
    if len(wds) > 3 and wds[0]=='From':
        tm=wds[5].split(':')
        sndr.append(tm[0])
    continue
#print(sndr)
for hr in sndr:
    counts[hr]=counts.get(hr,0)+1
#print(counts)
for k,v in sorted(counts.items()):
    print(k,v)
