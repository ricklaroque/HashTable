# nomes = [
#     "Ana", "Anna", "Aná", "Ana Paula", "Paula",
#     "Rafael", "Rafaela", "Rafaello",
#     "Érica", "Erica", "Erika",
#     "Luiz", "Luíz", "Luis", "Luís", "Luiz Felipe",
#     "Lúcia", "Lucia", "Luciana", "Lucas", "Lucaas",
#     "Gabriel", "Gabriela", "Gabriele",
#     "Pedro", "Pédro", "Pedro Henrique",
#     "Henri", "Henrique", "Henry",
#     "Sofia", "Sophia", "Sofía",
#     "Mariana", "Mariane", "Mariano",
#     "Joana", "João", "Joao", "João Pedro",
#     "Carlos", "Carl", "Carlo"
# ]
nomes = ["João", "João Silva", "Ana Clara", "Ana Cláudia", "Andressa", "André", "Roberta", "Roberto", "Carla", "Karl", "Marcos", "Marcus", "Pablo", "Pabllo", "Henrique", "José", "Jacinto", "Jocemar", "Josemar", "João"]
class HashTable():
    def __init__(self, size=10) -> None:
        self.size = size
        self.tabela = [[] for _ in range (size)]
        self.primos = [17, 43, 97]

        self.colisoes = 0

    def _hash(self, key):
        soma = 0
        for i in range(len(key)):
            if i < len(self.primos):
                soma += self.primos[i] * ord(key[i])
            else:
                soma += ord(key[i])
        return soma % self.size

    def inserir(self, key, string):
        posicao = self._hash(key)
        tabela = self.tabela[posicao]

        if self.tabela[posicao] != []:
            self.colisoes += 1

        for i, (k, v) in enumerate(tabela):
            if k == key:
                tabela[i] = (key, string)
                return

        tabela.append((key, string))

hash_table = HashTable()

for nome in nomes:
    hash_table.inserir(nome, len(nome))

for i, v in enumerate(hash_table.tabela):
    print(f"{i+1}: {v}")

print(f"\nQuantidade de colisões: {hash_table.colisoes}")