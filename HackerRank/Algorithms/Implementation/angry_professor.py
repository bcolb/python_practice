t = int(input())
for i in range(0, t):
    line1 = input()
    parts1 = line1.split(' ')
    n = int(parts1[0])
    k = int(parts1[1])
    line2 = input()
    parts2 = line2.split(' ')
    count = 0
    for j in range(0, len(parts2)):
        if int(parts2[j]) <= 0:
            count += 1
    if count >= k:
        print("NO")
    else:
        print("YES")
