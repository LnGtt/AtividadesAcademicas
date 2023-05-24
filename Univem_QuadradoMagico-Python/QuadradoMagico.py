n=int(input('Valor da lateral do quadrado mágico: '))
s=(n+n**3)/2
a=[0]*n
c=[0]*n
t=True
dp=0
di=0
if n>2:
    for i in range(n):
        a[i]=[0]*n
    for i in range(n):
        l=0
        for j in range(n):
            a[i][j]=int(input('Valor: '))
            l+=a[i][j]
            if n-j==1:
                if l!=s:
                    t=False
            if i==j:
                dp+=a[i][j]
            if i+j==n-1:
                di+=a[i][j]
    for i in range(n):
        for j in range(n):
            c[i]+=a[j][i]
        if c[i]!=s:
            t=False
    if dp!=s or di!=s:
        t=False
    if t==False:
        print("Não é um quadrado mágico!")
    else:
        print("É um quadrado mágico!")
else:
    print('O valor da lateral precisa ser maior que 2.')