# 중첩 if
x = 15

if x >= 0:
    print('양수')
    if(x>=10):
        print('10보다 큼')
    else:
        print('under 10')
elif x == 0:
    print('0')
else:
    print('음수')