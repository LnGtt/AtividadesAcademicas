a=[]
x=int(input('Quantidade de números: '))
for c in range(x):
    n=int(input('Digite um número: '))
    if c==0 or n<a[0]:
        a.insert(0,n)
    elif n>a[len(a)-1]:
        a.append(n)
    else:
        for j in range(len(a)):
            if n<=a[j]:
                a.insert(j,n)
                break
print(a)