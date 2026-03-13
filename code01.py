

#----Wednesday-------


def print_hello_world(n):
    for _ in range(n):
        print("Hello, World!")

def random_nums_list(n):
    import random
    nums = []
    for _ in range(n):
        nums.append(random.randint(1, 100))
    return nums

def check_prime(x):
    for i in range(2,x):
        if x%i == 0:
            return f"{x} is Not Prime"
            break
    else:
        return f"{x} is Prime"


#----Friday-------

def print_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

