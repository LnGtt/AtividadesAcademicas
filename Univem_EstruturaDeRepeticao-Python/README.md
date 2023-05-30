A Conjectura de Collatz, conhecida também por Problema 3x+1, foi proposta pelo matemático alemão Lothar Collatz em 1937. Seu enunciado é bastante simples e requer apenas um número inteiro positivo x como entrada para o problema. Dado um número inteiro positivo x, caso x seja par, divida-o por dois. Caso contrário, multiplique-o por três e some um. O número resultante de uma dessas operações será o novo valor de x. Repita esse processo até que o valor de x seja igual a 1.

De maneira mais formal, temos que: f(x) = x/2       (se for par)
                                          3x-1      (se ímpar)
                                    
Por exemplo, suponha que x seja inicialmente igual a 11. O número 11 é ímpar, dessa forma o novo valor de x será (3*11)+1 = 34. Repetindo o processo temos que o número 34 é par, logo o novo valor de x será 34/2 = 17. Repetindo esse processo chegaremos eventualmente no número 1, quando o processo acaba. O objetivo dessa atividade prática consiste em criarmos um programa que gere a sequência de números descrita pela Conjectura de Collatz a partir de um número inteiro positivo x.

ENTRADA
Como entrada, seu programa receberá um número inteiro positivo N. Em seguida, seu programa receberá N números inteiros positivos. Para cada um dos N números inteiros positivos, seu programa deverá gerar a sequência de números seguindo a descrição apresentada pela Conjectura de Collatz. Além disso, o programa deverá ser capaz de computar a quantidade de números pares e ímpares na sequência, bem como o maior número presente na mesma.
SAÍDA
Como saída, para cada um dos N números inteiros positivos, seu programa deverá imprimir essas informações no seguinte padrão: 
Valor inicial: (X) 
Numeros Pares: (PARES) 
Numeros Impares: (IMPARES) 
Maior Numero: (MAX)

Onde (X), (PARES), (IMPARES) e (MAX) representam respectivamente o valor inicial dado como entrada, a quantidade de números pares na sequência, a quantidade de números ímpares na sequência e o maior número da sequência.