def find_height(n):
    h = 1
    summer = False
    for i in range(0, n):
        if summer:
            h += 1
        else:
            h = h * 2
        summer = not summer
    return h

t = int(input())

for i in range(0, t):
    n = int(input())
    print(find_height(n))
