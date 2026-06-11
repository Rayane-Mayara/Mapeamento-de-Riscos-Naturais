# ==============================================================================
# SISTEMA DE COMANDO E MONITORAMENTO TÁTICO: PENEDO
# Disciplina: Programação 2
# Integrantes: Guilherme dos Santos, José Vadson, Rayane Mayara, 
#              Saulo Martins, Thaissa Aparecida
# ==============================================================================



class No:
    """Nó base utilizado para a construção de estruturas encadeadas."""
    def __init__(self, valor=None, proximo=None):
        self.valor = valor     
        self.proximo = proximo 

    def __str__(self):
        return str(self.valor)


class Ocorrencia:
    """Objeto auxiliar para encapsulamento e tráfego dos dados dos chamados."""
    def __init__(self, id, logradouro, nivel_risco):
        self.id = id
        self.logradouro = logradouro
        self.nivel_risco = nivel_risco

    def __str__(self):
        return f"ID: {self.id} | Local: {self.logradouro} | Risco: {self.nivel_risco}"


# 1. FILA DE ATENDIMENTO

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def isEmpty(self):
        return (self.length == 0)

    def insert(self, valor):
        node = No(valor)
        node.proximo = None  
        
        if self.head == None:
            self.head = node
        else:
            last = self.head
            while last.proximo: 
                last = last.proximo
            last.proximo = node
            
        self.length = self.length + 1
        print(f"--> Chamado #{valor.id} inserido na fila de espera.")

    def remove(self):
        if self.isEmpty():
            return None
        valor = self.head.valor
        self.head = self.head.proximo
        self.length = self.length - 1
        return valor


# 2. HISTÓRICO DE ALTERAÇÕES 

class Stack:
    def __init__(self):
        self.items = [] 

    def push(self, item):
        self.items.append(item)
        print(f"[Log] Ação '{item}' registrada.")

    def pop(self):
        if self.isEmpty():
            print("Nenhuma ação para desfazer.")
            return None
        return self.items.pop()

    def isEmpty(self):
        return (self.items == [])


# 3. MAPEAMENTO DE RISCO 

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


# 4. BUSCA DE LAUDOS 

class NoArvore:
    def __init__(self, protocolo, laudo_texto):
        self.protocolo = protocolo  
        self.valor = laudo_texto      
        self.esquerda = None          
        self.direita = None           


class ArvoreLaudos:
    def __init__(self):
        self.raiz = None

    def inserir(self, protocolo, laudo_texto):
        if self.raiz is None:
            self.raiz = NoArvore(protocolo, laudo_texto)
        else:
            self._inserir_recursivo(self.raiz, protocolo, laudo_texto)

    def _inserir_recursivo(self, no_atual, protocolo, laudo_texto):
        if protocolo < no_atual.protocolo:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoArvore(protocolo, laudo_texto)
            else:
                self._inserir_recursivo(no_atual.esquerda, protocolo, laudo_texto)
        elif protocolo > no_atual.protocolo:
            if no_atual.direita is None:
                no_atual.direita = NoArvore(protocolo, laudo_texto)
            else:
                self._inserir_recursivo(no_atual.direita, protocolo, laudo_texto)

    def buscar(self, protocolo):
        return self._buscar_recursivo(self.raiz, protocolo)

    def _buscar_recursivo(self, no_atual, protocolo):
        if no_atual is None or no_atual.protocolo == protocolo:
            return no_atual
        if protocolo < no_atual.protocolo:
            return self._buscar_recursivo(no_atual.esquerda, protocolo)
        return self._buscar_recursivo(no_atual.direita, protocolo)


# 5. ROTAS URBANAS

class GrafoPenedo:
    def __init__(self):
        self.malha_viaria = {}

    def adicionar_local(self, local):
        if local not in self.malha_viaria:
            self.malha_viaria[local] = []

    def adicionar_rua(self, origem, destino):
        self.adicionar_local(origem)
        self.adicionar_local(destino)
        if destino not in self.malha_viaria[origem]:
            self.malha_viaria[origem].append(destino)
        if origem not in self.malha_viaria[destino]:
            self.malha_viaria[destino].append(origem)

    def bloquear_rua(self, origem, destino):
        # Correção aqui: alterado de malia_viaria para malha_viaria
        if origem in self.malha_viaria and destino in self.malha_viaria[origem]:
            self.malha_viaria[origem].remove(destino)
        if destino in self.malha_viaria and origem in self.malha_viaria[destino]:
            self.malha_viaria[destino].remove(origem)
        print(f"\n VIA INTERDITADA: Bloqueio ativo entre '{origem}' e '{destino}'.")

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


# INTERFACE DO TERMINAL 

class SistemaDefesaCivil:
    def __init__(self):
        self.fila_chamados = Queue()          
        self.historico_logs = Stack()         
        self.mapa_risco = TabelaHash(10)     
        self.arquivo_laudos = ArvoreLaudos()  
        self.malha_viaria = GrafoPenedo()       
        
        self._inicializar_dados_demo()

    def _inicializar_dados_demo(self):
        self.mapa_risco.inserir("Rua da Aurora", "Crítico")
        self.mapa_risco.inserir("Centro", "Baixo")
        self.mapa_risco.inserir("Bairro Santa Luzia", "Médio")
        self.mapa_risco.inserir("Vila Primavera", "Alto")

        self.arquivo_laudos.inserir(202601, "Laudo 202601: Encosta monitorada na Vila Primavera. Solo saturado.")
        self.arquivo_laudos.inserir(202599, "Laudo 202599: Área do Centro estável, bueiros limpos.")

        self.malha_viaria.adicionar_rua("Base Defesa Civil", "Centro")
        self.malha_viaria.adicionar_rua("Centro", "Rua da Aurora")
        self.malha_viaria.adicionar_rua("Rua da Aurora", "Vila Primavera")
        self.malha_viaria.adicionar_rua("Base Defesa Civil", "Avenida Beira Rio")
        self.malha_viaria.adicionar_rua("Avenida Beira Rio", "Vila Primavera")

    def menu(self):
        while True:
            print("\n" + "="*50)
            print("     DEFESA CIVIL DE PENEDO - MONITORAMENTO TÁTICO     ")
            print("="*50)
            print("1. Registrar Novo Chamado de Emergência")
            print("2. Consultar Nível de Risco por Logradouro")
            print("3. Cadastrar Novo Laudo Técnico")
            print("4. Consultar Arquivo de Laudos Técnicos")
            print("5. Despachar Equipe (Calcular Rota de Socorro)")
            print("6. Interditar Via (Alagamento/Desabamento)")
            print("7. Desfazer Última Ação do Operador")
            print("0. Sair do Sistema")
            print("="*50)
            
            opcao = input("Escolha uma opção operacional: ").strip()
            print("-"*50)

            if opcao == "1":
                try:
                    id_c = int(input("Número da Ocorrência (ID): "))
                    local = input("Logradouro/Bairro: ")
                    risco_auto = self.mapa_risco.buscar(local) 
                    if risco_auto == "Rua não cadastrada":
                        risco_auto = input("Rua nova. Defina o risco (Baixo/Médio/Alto/Crítico): ")
                        self.mapa_risco.inserir(local, risco_auto)
                    
                    nova_ocorrencia = Ocorrencia(id_c, local, risco_auto)
                    self.fila_chamados.insert(nova_ocorrencia) 
                    self.historico_logs.push(f"Chamado #{id_c} adicionado") 
                except ValueError:
                    print("Erro: O ID da ocorrência precisa ser um número inteiro.")

            elif opcao == "2":
                local = input("Digite o nome da rua/bairro para consulta instantânea: ")
                resultado = self.mapa_risco.buscar(local)
                print(f"Status do Logradouro '{local}': [{resultado}]")

            elif opcao == "3":
                try:
                    protocolo = int(input("Digite o número do protocolo do laudo (Ex: 202602): "))
                    texto = input("Digite o parecer técnico do laudo: ")
                    self.arquivo_laudos.inserir(protocolo, texto)
                    print(f"Laudo #{protocolo} arquivado com sucesso na Árvore!")
                    self.historico_logs.push(f"Laudo #{protocolo} cadastrado")
                except ValueError:
                    print("Erro: O protocolo deve ser um número inteiro.")

            elif opcao == "4":
                try:
                    protocolo = int(input("Digite o número do protocolo do laudo (Ex: 202601): "))
                    no_laudo = self.arquivo_laudos.buscar(protocolo)
                    if no_laudo:
                        print(f"\nDocumento Localizado na Árvore:\n{no_laudo.valor}") 
                    else:
                        print("Protocolo não encontrado no arquivo digital.")
                except ValueError:
                    print("Erro: O protocolo deve ser um número inteiro.")

            elif opcao == "5":
                chamado = self.fila_chamados.remove() 
                if chamado:
                    print(f"CHAMADO EM ATENDIMENTO: #{chamado.id} - {chamado.logradouro}")
                    print("Calculando rota segura a partir da Base...")
                    rota = self.malha_viaria.calcular_rota_bfs("Base Defesa Civil", chamado.logradouro)
                    if rota:
                        print(f"ROTA RECOMENDADA: {' -> '.join(rota)}")
                        self.historico_logs.push(f"Equipe despachada para {chamado.logradouro}")
                    else:
                        print("Alerta Máximo: Não há rotas acessíveis disponíveis! Vias obstruídas.")
                else:
                    print("Central tranquila. Nenhuma ocorrência na fila de espera.")

            elif opcao == "6":
                origem = input("Ponto de Origem do bloqueio: ")
                destino = input("Ponto de Destino do bloqueio: ")
                self.malha_viaria.bloquear_rua(origem, destino)
                self.historico_logs.push(f"Bloqueio de via entre {origem} e {destino}")

            elif opcao == "7":
                acao_desfeita = self.historico_logs.pop() 
                if acao_desfeita:
                    print(f"Revertendo com sucesso a ação: '{acao_desfeita}'")

            elif opcao == "0":
                print("Encerrando o Sistema Tático. Operação finalizada de forma segura.")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sistema = SistemaDefesaCivil()
    sistema.menu()