Elabore um algoritmo (implemente em Python) que comece com uma lista vazia:

A = [ ]

E, ao inserir os valores, estes devem sempre permanecerem em ordem crescente. Para isto, use o método insert... Veja:

A.insert(pos, valor) -> este métdo insere o valor na posição pos.

Assim, antes de realizar a inserção, você deverá procurar a posição onde o valor deve ser inserido.

Algoritmo Geral:

· Se a lista estiver vazia ou se o valor a ser inserido é menor do que o primeiro valor da lista, então a posição dever ser 0 (o valor será o primeiro da lista)

· Caso a lista tenha valores e o valor a ser inserido é maior do que o último então, o valor deverá ser inserido no fim da lista (posição será o tamanho da lista à pesquise como usar o método len()).

· Caso tenha valores, poderá ocorrer que o valor a ser inserido fique em algum lugar no meio da lista (entre dois valores) . Neste caso, procure qual dever ser a posição correta para a inserção.

Veja alguns exemplos:

A = [ ] -> valor a inserir == 10

A = [10] -> valor a inserir == 5

A = [5, 10] -> valor a inserir == 40

A = [5, 10, 40] -> valor a inserir == 30

A = [5, 10, 30, 40 ] -> valor a inserir == 15

A = [5, 10, 15, 30, 40 ] e assim por diante....