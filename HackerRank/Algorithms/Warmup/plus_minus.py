def print_ratio(t, c):
    num = 0
    if c > 0:
        num = c / float(t)
    print "%.6f" % num

total = int(raw_input())
parts = raw_input().split(' ')
positive_count = 0
zero_count = 0
negative_count = 0
for i in range(0, len(parts)):
    n = int(parts[i])
    if n > 0:
        positive_count += 1
    elif n == 0:
        zero_count += 1
    else:
        negative_count += 1
print_ratio(total, positive_count)
print_ratio(total, negative_count)
print_ratio(total, zero_count)
