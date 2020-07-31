# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
tot=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count=count+1
        numpos=line.find('0')
        numstr=line[numpos:]
        num=float(numstr)
        tot=tot+num
print("Average spam confidence:", tot/count)
