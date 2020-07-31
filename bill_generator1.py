gold_rate_tengms=42000
wgt1=input('Wieght in grams:')
wgt=float(wgt1)
labour_r1=input('Labour charge:')
labour_r=float(labour_r1)
wastge1=input('Wastage in grams:')
wastge=float(wastge1)
total=((wgt+wastge)*(gold_rate/10))+labour_r
print('Total charge:',total)
