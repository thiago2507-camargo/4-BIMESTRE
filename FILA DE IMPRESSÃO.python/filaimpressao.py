class FilaDeImpressao:
    def __init__(self):
        self.fila = []

    def adicionar_trabalho(self, trabalho):
        self.fila.append(trabalho)
        print(f"Trabalho '{trabalho}' adicionado à fila de impressão.")

    def processar_trabalho(self):
        if not self.esta_vazia():
            trabalho = self.fila.pop(0)
            print(f"O trabalho '{trabalho}' está sendo processado...")
        else:
            print("A fila está vazia!")

    def mostrar_fila(self):
        if self.esta_vazia():
            print("A fila está vazia!")
        else:
            print("Fila atual de impressão:")
            for trabalho in self.fila:
                print(f"- {trabalho}")

    def esta_vazia(self):
        return len(self.fila) == 0


def menu():
    fila_impressao = FilaDeImpressao()
    
    while True:
        print("\nOpções:")
        print("1. Adicionar um trabalho na fila de impressão")
        print("2. Imprimir o próximo trabalho da fila")
        print("3. Mostrar a fila de impressão")
        print("4. Sair")
        
        escolha = input("Escolha uma opção de 1-4: ")

        if escolha == "1":
            trabalho = input("Digite o nome do trabalho a ser impresso: ")
            fila_impressao.adicionar_trabalho(trabalho)
        elif escolha == "2":
            fila_impressao.processar_trabalho()
        elif escolha == "3":
            fila_impressao.mostrar_fila()
        elif escolha == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção Inválida.")


# Executando o menu
menu()
