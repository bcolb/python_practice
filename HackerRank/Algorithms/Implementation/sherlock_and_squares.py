import math

def count_squares(start, end):
    s = math.floor(math.sqrt(start))
    count = 0
    while s*s <= end:
        if s*s >= start:
            count += 1
        s += 1
    return count

t = int(input())

for i in range(0, t):
    s = input()
    parts = s.split(' ')
    start = int(parts[0])
    end = int(parts[1])
    print(count_squares(start, end))
