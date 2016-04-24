t = int(input())

for i in range(0, t):
    count = 0
    num = input()
    n = int(num)
    l = len(num)
    for j in range(0, l):
        curr_num = int(num[j])
        if (curr_num) and (n % curr_num == 0):
            count += 1
    print(count)
