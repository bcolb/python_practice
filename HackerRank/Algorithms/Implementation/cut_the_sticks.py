n = int(input())
text = input()
text_arr = text.split(' ')
sticks = [int(s) for s in text_arr]
while(len(sticks) > 0):
    cut_len = min(sticks)
    print(len(sticks))
    new_sticks = []
    count = 0
    for i in range(0, len(sticks)):
        if sticks[i] > cut_len:
            count += 1
            new_sticks.append(sticks[i] - cut_len)
    sticks = new_sticks
