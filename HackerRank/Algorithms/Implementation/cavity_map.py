n = int(input())

m = [0 for k in range(0, n)]
for i in range(0, n):
    line = input()
    inner = [int(x) for x in line]
    m[i] = inner

for i in range(0, n):
    s = ""
    for j in range(0, n):
        if i > 0 and i < (n-1) and j > 0 and j < (n-1):
            num = m[i][j]
            if num > m[i-1][j] and num > m[i+1][j] and num > m[i][j+1] and num > m[i][j-1]:
                s += 'X'
            else:
                s += str(m[i][j])
        else:
            s += str(m[i][j])
    print(s)
