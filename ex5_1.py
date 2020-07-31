smallestnum=None
largestnum=0
while True:
    sval=input('Enter a number: ')
    if sval=='done':
        break
    try:
        fval=int(sval)
        if smallestnum is None:
            smallestnum=fval
            if fval>=largestnum:
                largestnum=fval
            else:
                largestnum=largestnum
        elif fval<smallestnum:
            smallestnum=fval
            if fval>=largestnum:
                largestnum=fval
            else:
                largestnum=largestnum
        else:
            smallestnum=smallestnum
            if fval>=largestnum:
                largestnum=fval
            else:
                largestnum=largestnum

    except:
        print('Invalid input')
        continue

print('Maximum is',largestnum,'\nMinimum is',smallestnum)
