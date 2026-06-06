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



class SistemaDefesaCivil:
    def __init__(self):
        self.arquivo_laudos = ArvoreLaudos()
        self._inicializar_dados_demo()

    def _inicializar_dados_demo(self):
        self.arquivo_laudos.inserir(202601, "Laudo 202601: Encosta monitorada na Vila Primavera. Solo saturado.")
        self.arquivo_laudos.inserir(202599, "Laudo 202599: Área do Centro estável, bueiros limpos.")

    def menu(self):
        while True:
            print("\n" + "="*50)
            print("     DEFESA CIVIL DE PENEDO - MÓDULO ÁRVORE (BST)     ")
            print("="*50)
            print("1. Cadastrar Novo Laudo Técnico")
            print("2. Consultar Arquivo de Laudos Técnicos")
            print("0. Sair do Módulo")
            print("="*50)
            
            opcao = input("Escolha uma opção operacional: ").strip()
            print("-"*50)

            if opcao == "1":
                try:
                    protocolo = int(input("Digite o número do protocolo (Ex: 202602): "))
                    texto = input("Digite o parecer técnico do laudo: ")
                    self.arquivo_laudos.inserir(protocolo, texto)
                    print(f" Laudo #{protocolo} arquivado com sucesso!")
                except ValueError:
                    print("Erro: O protocolo precisa ser um número inteiro.")

            elif opcao == "2":
                try:
                    protocolo = int(input("Digite o número do protocolo do laudo para consulta: "))
                    no_laudo = self.arquivo_laudos.buscar(protocolo)
                    if no_laudo:
                        print(f"\n Documento Localizado:\n{no_laudo.valor}")
                    else:
                        print(" Protocolo não encontrado no arquivo digital.")
                except ValueError:
                    print("Erro: O protocolo deve ser um número inteiro.")

            elif opcao == "0":
                print("Encerrando o Módulo Árvore.")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    sistema = SistemaDefesaCivil()
    sistema.menu()

