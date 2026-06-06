# ==========================================
# PROJETO: Monitoramento de Áreas de Risco (Penedo)
# DISCIPLINA: Programação 2 - UFAL SI
# COMPONENTE: Mecanismo de Undo usando Pilha (LIFO)
# ==========================================

class PilhaDefesaCivil:
    def __init__(self):
        # Inicializa a lista vazia para armazenar o histórico
        self.itens = []

    def is_empty(self):
        # Retorna True se a pilha estiver vazia
        return len(self.itens) == 0

    def push(self, item):
        # Adiciona uma nova alteração de status no topo da pilha
        self.itens.append(item)

    def pop(self):
        # Remove e retorna o item do topo se a pilha não estiver vazia
        if self.is_empty():
            print("\n[Aviso] Nada para desfazer! O histórico está vazio.")
            return None
        return self.itens.pop()

    def exibir_historico(self):
        # Método extra para o operador ver o que está na pilha atual
        if self.is_empty():
            print("Nenhum alerta ativo no momento.")
        else:
            print("\n--- STATUS ATUAIS NO SISTEMA ---")
            for acao in reversed(self.itens):
                print(f"Localidade: {acao['localidade']} | Status: {acao['status']}")


# --- Menu Interativo no Terminal ---

# Criação da pilha que vai gerenciar o mecanismo de desfazer
historico_alertas = PilhaDefesaCivil()

while True:
    print("\n=============================================")
    print("      DEFESA CIVIL DE PENEDO - ALAGOAS       ")
    print("=============================================")
    print("1. Registrar Nova Alteração de Status / Alerta")
    print("2. Desfazer Última Ação (Undo)")
    print("3. Sair do Sistema")
    print("=============================================")
    
    opcao = input("Escolha uma opção (1-3): ").strip()

    if opcao == "1":
        print("\nExemplos de localidades: Barro Vermelho, Centro, Coreia, Camartelo, Oiteiro")
        localidade = input("Digite a localidade de Penedo: ").strip()
        
        print("Status: 1- Normal | 2- Atenção (Chuva Moderada) | 3- Alerta Máximo (Risco de Deslizamento)")
        status = input("Digite o novo status da área: ").strip()

        if localidade and status:
            # Cria o dicionário pedido pelo enunciado
            nova_alteracao = {
                'localidade': localidade,
                'status': status
            }
            # Empilha a ação
            historico_alertas.push(nova_alteracao)
            print(f"\n[Sucesso] Status de '{localidade}' atualizado para '{status}'!")
        else:
            print("\n[Erro] Localidade ou status inválidos. Tente novamente.")

    elif opcao == "2":
        # Desempilha a última ação
        ultima_acao = historico_alertas.pop()
        
        if ultima_acao:
            print("\n[DESFEITO] A seguinte alteração foi cancelada:")
            print(f"-> Localidade removida: {ultima_acao['localidade']}")
            print(f"-> Status cancelado: {ultima_acao['status']}")
            print("\nO sistema voltou com sucesso ao estado anterior.")

    elif opcao == "3":
        print("\nEncerrando o Sistema de Monitoramento da Defesa Civil de Penedo. Até logo!")
        break

    else:
        print("\n[Opção Inválida] Digite um número de 1 a 3.")
    
    # Exibe como o histórico ficou após a operação atual
    historico_alertas.exibir_historico()