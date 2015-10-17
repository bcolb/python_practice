#!/usr/bin/python3
def get_date_ints(d):
    parts = d.split(' ')
    res = {}
    res['day'] = int(parts[0])
    res['month'] = int(parts[1])
    res['year'] = int(parts[2])
    return res

def get_fine(d1, d2):
    actual = get_date_ints(d1)
    expected = get_date_ints(d2)
    if actual['year'] == expected['year']:
        if actual['month'] == expected['month']:
            if actual['day'] <= expected['day']:
                return 0
            else:
                return 15 * (actual['day'] - expected['day'])
        elif actual['month'] > expected['month']:
            return 500 * (actual['month'] - expected['month'])
        else:
            return 0
    elif actual['year'] > expected['year']:
        return 10000
    else:
        return 0

d1 = input()
d2 = input()
print(get_fine(d1,d2))
