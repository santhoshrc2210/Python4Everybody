text = "X-DSPAM-Confidence:    0.8475";
pos=text.find('0')
lpos=text.find('5')
str=text[pos:lpos+1]
fnum=float(str)
print(fnum)
