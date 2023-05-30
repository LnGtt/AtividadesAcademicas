t1 = float(input('Temperatura do primeiro dia em °C: '))
t2 = float(input('Temperatura do segundo dia em °C: '))
t3 = float(input('Temperatura do terceiro dia em °C: '))

if t1>t2:
    if t2<=t3:
        print(':)')
    elif t2>t3 and (t3-t2)>(t2-t1):
        print(':)')
    elif t2>t3 and (t3-t2)<=(t2-t1):
        print(':(')
elif t1<t2:
    if t2>=t3:
        print(':(')
    elif t2<t3 and (t3-t2)<(t2-t1):
        print(':(')
    elif t2<t3 and (t3-t2)>=(t2-t1):
        print(':)')
else:
    if t2>t3:
        print(':(')
    else:
        print(':)')