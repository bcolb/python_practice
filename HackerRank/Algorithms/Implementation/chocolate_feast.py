t = int(input())

for i in range(0, t):
    line = input()
    n,c,m = [int(x) for x in line.split(' ')]
    chocolates = n // c
    wrappers = chocolates
    while wrappers >= m:
        new_chocolates = wrappers // m
        wrappers = wrappers % m + new_chocolates
        chocolates += new_chocolates
    print(chocolates)
