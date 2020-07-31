han=open('mbox-short.txt')
counts=dict()
sndr=list()
for line in han:
    line=line.rstrip()
    #print(line)
    wds=line.split()
    #print(wds)
    if len(wds) > 3 and wds[0]=='From':
        sndr.append(wds[1])
        #print(wds[1])
        continue
#print(sndr)
for eid in sndr:
    counts[eid]=counts.get(eid,0)+1
#print(counts)
bigcount=None
bigWord=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
