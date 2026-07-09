# Sum of all prime numbers between 1 to n.

def prime_no():
    sum = 0
    start = int(input("enter the start point:"))
    stop = int(input("enter the stop point:"))
    for no in range(start,stop):
        for i in range(2,no):
            if(no % i ==0):
                break
            else:
                print(no)
prime_no()
        
  
