def find_widest_vehicle(lane, lentry, lexit):
    if lentry > lexit:
        return 0
    narrowest = 3
    for j in range(lentry, lexit+1):
        if lane[j] < narrowest:
            narrowest = lane[j]
    return narrowest

line1 = input()
parts1 = line1.split(' ')
n = int(parts1[0])
t = int(parts1[1])
line2 = input()
parts2 = line2.split(' ')
lane = [int(s) for s in parts2]

for i in range(0, t):
    line = input()
    parts = line.split(' ')
    lentry = int(parts[0])
    lexit = int(parts[1])
    print(find_widest_vehicle(lane, lentry, lexit))
