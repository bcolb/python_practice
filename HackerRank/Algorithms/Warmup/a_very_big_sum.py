n = long(raw_input())
sum = 0
parts = raw_input().split(' ')
for i in range(0, len(parts)):
    sum += long(parts[i])
print sum
