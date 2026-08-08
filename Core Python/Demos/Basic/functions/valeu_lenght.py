def add(*num):
    sum = 0
    for val in num:
        sum = sum + val
    return sum
res = add(10,20,30,40,50)
res = add(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9)
print(res)
