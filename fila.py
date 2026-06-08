import sys

# 0. NÓ 

class No:
    def __init__(self, valor=None, proximo=None):
        self.valor = valor     
        self.proximo = proximo 

    def __str__(self):
        return str(self.valor)

class Ocorrencia:
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
