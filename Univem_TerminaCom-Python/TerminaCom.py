a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
aa = a
bb = b
if a==b:
    print(f'{bb} é o final de {aa}.')
else:
    if b>a:
        print(f'{bb} não é o final de {aa}.')
    else:
        while b>0:
            if a%10==b%10:
                a=a//10
                b=b//10
            else:
                print(f'{bb} não é o final de {aa}.')
                break
        if b==0:
            print(f'{bb} é o final de {aa}.')