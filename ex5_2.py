smallestnum=None
largestnum=0
while True:
    sval=input('Enter a number: ')
    if sval=='done':
        break
    try:
        fval=int(sval)
        if fval>=largestnum:
            largestnum=fval
            if smallestnum is None:
                smallestnum=fval
            elif fval<smallestnum:
                smallestnum=fval
            else:
                smallestnum=smallestnum
        else:
            largestnum=largestnum
            if smallestnum is None:
                smallestnum=fval
            elif fval<smallestnum:
                    smallestnum=fval
            else:
                smallestnum=smallestnum

    except:
        print('Invalid input')
        continue

print('Maximum is',largestnum,'\nMinimum is',smallestnum)
