# Write a program to check if entered number is a palindrome or not.
def pali(num):
    temp = num
    rev = 0
    while(temp > 0):
        d = temp % 10
        rev = rev * 10 + d
        temp = temp // 10
    return rev
def palin():
    num = int(input("enter the number:"))
    if num == pali(num):
        print("numver is palindrome....!")
    else:
        print("number is not palindrome....!")
palin()