a = int(input("Seconds: "))

hour = int(a / 3600)
if len(str(hour))==1: h = '0' + str(hour)
else: h = hour

minute = int((a - hour*3600) / 60)
if len(str(minute))==1: m = '0' + str(minute)
else: m = minute

second = a - hour*3600 - minute*60
if len(str(second))==1: s = '0' + str(second)
else: s = second

print(h,end=':')
print(m,end=':')
print(s)