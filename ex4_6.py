h=input('Enter Hours:')
hrs=float(h)
p=input('Enter rate per Hour:')
payph=float(p)
def computepay():
    if hrs<=40:
        grpay=hrs*payph
    else:
        extrhr=hrs-40
        grpay=(40*payph)+(extrhr*payph*1.5)
    return(grpay)
grsspay=computepay()
print('Pay',grsspay)
