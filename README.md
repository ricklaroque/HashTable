## Trabalho Algoritmo e Estrutura de Dados 2, Hash Table.

# Além disso, você deve:
#    1.    Justificar matematicamente ou logicamente como sua função tenta distribuir os dados.
Comecei tentando apenas usando a função ord() do python, que utiliza a tabela ASCII, somando e então % de size, porém não parecia ser o suficiente, então adicionei números primos a equação, fazendo o caracter 0, 1, 2 serem multiplicados por 3 números primos (e o restante continuou apenas com a função ord() normal, sem multiplicar por números primos), e então somava tudo e fazia % de size, retornando a posição de onde a string deve ser armazenada.
#    2.    Definir como sua solução lida com colisões:
#    •    chaining (listas encadeadas)
#    •    open addressing (linear probing, quadratic probing, double hashing)
#    •    ou outro método criativo.
Acredito que esteja usando o chaining, não sei bem o termo técnico, mas a colisão é a mesma apresentada pelo professor Pablo em aula, onde acontece uma verificação em cada nome para ver se ela já existe na tabela, se existir ela não armazena. (evita nomes repetidos).
#    3.    Escolher um tamanho adequado para a tabela:
#    •    Explique por que escolheu esse valor
#    •    Comente sobre load factor (taxa de ocupação ideal)
Escolhi tamanho 10, pois é facil de enxergar qual seria o load factor (2 em cada espaço), mas mesmo assim não consegui atingir esse objetivo.
#    4.    Criar pelo menos 20 nomes de teste (nomes reais, com acentos, repetidos, semelhantes).
#    5.    Exibir:
#    •    Índice gerado para cada nome
#    •    Gráfico ou tabela com distribuição dos valores (opcional, mas recomendado)
#    •    Análise do número de colisões