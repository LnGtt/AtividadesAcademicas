x=int(input("Número: "))
if x>0:
    while x !=1:
        if x%2==0:
            collatz=x/2
            x=collatz
        else:
            collatz=3*x+1
            x=collatz
        print(x)
else:
    print("O número precisa ser positivo.")