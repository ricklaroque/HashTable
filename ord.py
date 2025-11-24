primos = [17, 43, 97]
nomes = "Henrique"
soma = 0
size = 10
for i in range(len(nomes)):
    if i < len(primos):
        soma += primos[i] * ord(nomes[i])
    else:
        soma += ord(nomes[i])
print(f"Tamanho de {nomes}, {soma % size}")