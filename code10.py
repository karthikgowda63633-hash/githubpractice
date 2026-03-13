

def check_prime(x):
    for i in range(2,x):
        if x%i == 0:
            return f"{x} is Not Prime"
            break
    else:
        return f"{x} is Prime"


import sys

n  = int(sys.argv[1])

print(check_prime(n))


def check_odd_even(x):
    if x%2 == 0:
        return f"{x} is Even"
    else:
        return f"{x} is Odd"
    
print(check_odd_even(n))


def check_palindrome(x):
    if str(x) == str(x)[::-1]:
        return f"{x} is Palindrome"
    else:
        return f"{x} is Not Palindrome"
    
print(check_palindrome(n))

