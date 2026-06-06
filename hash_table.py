class HashTable:

    def __init__(self):
        self.tabela = [[] for _ in range(10)]

    def hash(self, rua):
        soma = 0

        for letra in rua:
            soma += ord(letra)

        return soma % 10

    def inserir(self, rua, risco):

        indice = self.hash(rua)

        self.tabela[indice].append(
            [rua, risco]
        )

    def buscar(self, rua):

        indice = self.hash(rua)

        for item in self.tabela[indice]:

            if item[0] == rua:
                return item[1]

        return "Rua não encontrada"

    def mostrar(self):

        for i in range(10):
            print(i, "->", self.tabela[i])


areas = HashTable()


areas.inserir("Rua A", "Alto")
areas.inserir("Rua B", "Baixo")
areas.inserir("Rua C", "Medio")
areas.inserir("Rua D", "Alto")


print(areas.buscar("Rua B"))

areas.mostrar()