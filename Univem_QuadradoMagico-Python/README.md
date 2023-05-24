Quadrado Mágico é uma matriz quadrada de lado N, onde a soma dos números das linhas, das colunas e das diagonais é constante, sendo que nenhum destes números se repete.
Primeiramente o programa deve pedir ao usuário o valor do “lado” do quadrado (dimensão da matriz, sendo superior a 2 – ordem N) e então calcular o valor que deverá ser a soma das linhas, colunas e diagonais.
A fórmula pode ser calculada de duas formas:

1ª Soma-se todos os dígitos a serem inseridos, exemplo para uma matriz de lado 3, serão inseridos dígitos de 1 a 9 sendo que a soma dos mesmos é igual a 45. Divide-se este número por 3, temos que a somatória deverá ser 15.

2ª Utilizando-se a fórmula S = (n + n3) / 2, sendo n o “lado” do quadrado e maior que dois.

Assim, para o quadrado (3 por 3), a somatória é obtida da seguinte forma:

S = (3 + 33) / 2 = 15

Em seguida, terá de pedir os números de 1 a 9 em 9 casas, considerando a matriz de ordem N == 3, verificando se a soma das linhas, colunas e diagonais sejam iguais a 15, no exemplo.
Imprimir a matriz seguida da mensagem: “Quadrado Mágico” ou “Não é um Quadrado Mágico”