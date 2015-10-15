n = int(raw_input())
for i in range(0, n):
    str = ""
    for k in range(i, n-1):
        str += ' '
    for j in range((n-i-1), n):
        str += '#'
    print str
