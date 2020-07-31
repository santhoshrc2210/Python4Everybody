fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line=line.rstrip()
    uline=line.upper()
    print(uline)
