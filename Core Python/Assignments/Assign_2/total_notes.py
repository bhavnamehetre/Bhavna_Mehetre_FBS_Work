a=int(input("enter the amount::"))
no1=a//500
r1=a%500
print("the note of 500Rs is::",no1)
no2=r1//200
r2=r1%200
print("the note of 200Rs is::",no2)
no3=r2//100
r3=r2%100
print("the note of 100Rs is::",no3)
no4=r3//50
r4=r3%50
print("the note of 50Rs is::",no4)
no5=r4//20
r5=r4%20
print("the note of 20Rs is::",no5)
no6=r5//10
r6=r5%10
print("the note of 10Rs is::",no6)
print("The total number of notes are:",no1+no2+no3+no4+no5+no6)
