def long_factorial(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return num * long_factorial(num-1)

n = int(input())
print(long_factorial(n))
