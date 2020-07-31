scr=input('Enter Score:')
try:
    scre=float(scr)
    if scre>=0.0 and scre<=1.0: #is this the only way to check range, try int function
        if scre>=0.9:
            print('A')
        elif scre>=0.8:
            print('B')
        elif scre>=0.7:
            print('C')
        elif scre>=0.6:
            print('D')
        else:
            print('F')
    else:
        print('Error:Entered value out of range')
except:
    print('Please enter a number')
