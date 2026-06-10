p=int(input('Enter the value for principle::'))
r=float(input('Enter the value for rate::'))
t=float(input('Enter the value for time::'))
compound_int=p*(1+r/100)**t - p
print("compound interest is::",compound_int)

