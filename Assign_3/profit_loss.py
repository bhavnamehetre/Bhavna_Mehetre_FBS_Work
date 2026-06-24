cp = int(input("enter the cost price:"))
sp = int(input("enter the selling price:"))
amt = sp - cp
if(amt == 0):
    print("No profit no loss:",amt)
elif(amt > 0):
    print("Profit:",amt)
else:
    print("Loss:",amt)