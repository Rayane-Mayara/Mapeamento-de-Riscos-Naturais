Python
# ==============================================================================
# SISTEMA DE COMANDO E MONITORAMENTO TÁTICO: PENEDO (ESTRUTURA DE GRAFO)
# Integrantes: Rayane, Thaissa, Saulo, Guilherme e Vadson
# ==============================================================================

# 0. CLASSE NÓ
class No:
    def __init__(self, valor=None, proximo=None):
        self.valor = valor       
        self.proximo = proximo   

    def __str__(self):
        return str(self.valor)

# 5. GRAFOS E ROTAS URBANAS
class GrafoCity:
    def __init__(self):
        self.malha_viaria = {}

    def adicionar_local(self, local):
        if local not in self.malha_viaria:
            self.malha_viaria[local] = []

    def adicionar_rua(self, origen, destino):
        self.adicionar_local(origen)
        self.adicionar_local(destino)
        if destino not in self.malha_viaria[origen]:
            self.malha_viaria[origen].append(destino)
        if origen not in self.malha_viaria[destino]:
            self.malha_viaria[destino].append(origen)

    def bloquear_rua(self, origen, destino):
        if origen in self.malha_viaria and destino in self.malha_viaria[origen]:
            self.malha_viaria[origen].remove(destino)
        if destino in self.malha_viaria and origen in self.malha_viaria[destino]:
            self.malha_viaria[destino].remove(origen)
        print(f"\n⚠️ VIA INTERDITADA: Bloqueio ativo entre '{origen}' e '{destino}'.")

    def calcular_rota_bfs(self, partida, destino):
        if partida not in self.malha_viaria or destino not in self.malha_viaria:
            return None
        fila_exploracao = [[partida]]
        visitados = set()
        while fila_exploracao:
            caminho_atual = fila_exploracao.pop(0)
            no_atual = caminho_atual[-1]
            if no_atual == destino:
                return caminho_atual
            if no_atual not in visitados:
                visitados.add(no_atual)
                vizinhos = self.malha_viaria.get(no_atual, [])
                for vizinho in vizinhos:
                    novo_caminho = list(caminho_atual)
                    novo_caminho.append(vizinho)
                    fila_exploracao.append(novo_caminho)
        return None

# INTERFACE DO TERMINAL INTEGRADA (Apenas funções de Grafo ativas)
class SistemaDefesaCivil:
    def __init__(self):
        self.malha_viaria = GrafoCity()       
        self.malha_viaria.adicionar_rua("Base Defesa Civil", "Centro")
        self.malha_viaria.adicionar_rua("Centro", "Rua da Aurora")
        self.malha_viaria.adicionar_rua("Rua da Aurora", "Vila Primavera")
        self.malha_viaria.adicionar_rua("Base Defesa Civil", "Avenida Beira Rio")
        self.malha_viaria.adicionar_rua("Avenida Beira Rio", "Vila Primavera")

    def menu(self):
        while True:
            print("\n" + "="*50)
            print("     DEFESA CIVIL DE PENEDO - MÓDULO GRAFOS     ")
            print("="*50)
            print("4. [Grafo] Despachar Equipe (Calcular Rota de Socorro)")
            print("5. [Grafo] Interditar Via (Alagamento/Desabamento)")
            print("0. Sair do Sistema")
            print("="*50)
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "4":
                local = input("Logradouro/Bairro de destino: ")
                rota = self.malha_viaria.calcular_rota_bfs("Base Defesa Civil", local)
                if rota:
                    print(f"➔ ROTA RECOMENDADA: {' -> '.join(rota)}")
                else:
                    print("❌ Não há rotas acessíveis disponíveis.")
            elif opcao == "5":
                origen = input("Origem do bloqueio: ")
                destino = input("Destino do bloqueio: ")
                self.malha_viaria.bloquear_rua(origen, destino)
            elif opcao == "0":
                break

if __name__ == "__main__":
    sistema = SistemaDefesaCivil()
    sistema.menu()