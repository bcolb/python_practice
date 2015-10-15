n = int(raw_input())
str = raw_input()
parts = str.split(' ')
sum = 0
for i in range(0, len(parts)):
    sum += int(parts[i])
print sum 
