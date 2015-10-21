def repeat_character(c, count):
    s = ""
    for i in range(0, count):
        s += c
    return s

def decent_number(num):
    if num <= 2:
        return -1
    if num % 3 == 0:
        return repeat_character('5', num)
    for i in range(0, num):
        n = i + 1
        if (num - n) % 3 == 0 and n % 5 == 0:
            return repeat_character('5', (num-n)) + repeat_character('3', n)
    if n % 5 == 0:
        return repeat_character('3', n)
    return -1

t = int(input())
for i in range(0, t):
    num = int(input())
    print(decent_number(num))
