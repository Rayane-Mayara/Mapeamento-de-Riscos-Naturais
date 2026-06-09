class ElementoHash:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.baldes = [None] * tamanho

    def _funcao_hash(self, chave):
        soma_ascii = sum(ord(caractere) for caractere in str(chave))
        return soma_ascii % self.tamanho

    def inserir(self, chave, valor):
        indice = self._funcao_hash(chave)
        novo_elemento = ElementoHash(chave, valor)

        if self.baldes[indice] is None:
            self.baldes[indice] = novo_elemento
            return

        atual = self.baldes[indice]

        while atual:
            if atual.chave == chave:
                atual.valor = valor
                return

            if atual.proximo is None:
                break

            atual = atual.proximo

        atual.proximo = novo_elemento

    def buscar(self, chave):
        indice = self._funcao_hash(chave)
        atual = self.baldes[indice]

        while atual:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo

        return "Rua não cadastrada"


mapa_risco = TabelaHash()

mapa_risco.inserir("Rua da Aurora", "Crítico")
mapa_risco.inserir("Centro", "Baixo")
mapa_risco.inserir("Vila Primavera", "Alto")

print(mapa_risco.buscar("Rua da Aurora"))
print(mapa_risco.buscar("Centro"))
print(mapa_risco.buscar("Vila Primavera"))
print(mapa_risco.buscar("Rua Nova"))