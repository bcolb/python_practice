n = int(raw_input())
sum_a = 0
sum_b = 0
for i in range(0, n):
      parts = raw_input().split(' ')
      sum_a += int(parts[i])
      sum_b += int(parts[n-i-1])
res = abs(sum_a-sum_b)
print res
