def convert(oldTime):
    hr = int(oldTime[0: 2])
    PM = True if oldTime[8:] == "PM" else False
    if (PM and hr < 12):
        time = str(hr + 12) + oldTime[2:8]
        return time
    if (PM):
        time = oldTime[0:8]
        return time
    if (hr == 12):
        time = '00' + oldTime[2:8]
        return time
        
    time = oldTime[0:8]
    return time

print(convert('12:00:00AM'), 'should be 00:00:00')
print(convert('12:00:00PM'), 'should be 12:00:00')
print(convert('02:00:00AM'), 'should be 02:00:00')
print(convert('02:00:00PM'), 'should be 14:00:00')
print(convert('11:00:00AM'), 'should be 11:00:00')
print(convert('11:00:00PM'), 'should be 23:00:00')
