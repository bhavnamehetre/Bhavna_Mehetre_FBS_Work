# def add(**data):
#     for key,val in data.items():
#         print(f'{key} = {val}.')
# add(id=101,name='bhavna',sal=2500,dept="computer_sci")

# def fact(n):
#     fact1 = n
#     if(n > 1):
#           return fact1 * fact(n - 1)
#     else:
#          return 1
      
# n = 5
# res = fact(n)
# print(res)


# def digit(n):
#     if(n > 0):
#       
    #     digit(n // 10)
        # print(d)
    #     print(n % 10)
# n = 121
# res = digit(n)
# print(res)

def pali(n):
    temp = n
    rev = 0
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        rev = rev * 10 + d
    sum = sum + rev
    if(sum == n):
        return True
    else:
        return False
n = 121
res = pali(n)
print(res)












