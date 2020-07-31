fh = open('romeo.txt')
lst = list()
for line in fh:
    line=line.rstrip()
    words=line.split()
    for i in words:
        if i not in lst:
            lst.append(i)
        continue
lst.sort()
print(lst)
