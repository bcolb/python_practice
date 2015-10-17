#!/usr/bin/python3
def get_time_string(the_time):
    if the_time == '12:00:00AM':
        return '00:00:00'
    elif the_time == '12:00:00PM':
        return '12:00:00'
    else:
        parts = the_time.split(':')
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2][:2])
        am = parts[2][2:] == 'AM'
        if am and hours == 12:
            hours = 0
        elif not am and hours != 12:
            hours += 12
        res = "%02d:%02d:%02d" % (hours, minutes, seconds)
        return res

the_time = input()
print(get_time_string(the_time))
