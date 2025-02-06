def menu():
    fila_impressao= filadeimpressao()
    fila_impressao.configurar_inicial()
    while True:
        print("opções:")
        print("1. Adicionar um trabalho na fila de impressao")
        print("2. Imprimir o proximo trabalho da fila")
        print("3. Mostrar a fila de impressao")
        print("4. Sair")
        escolha = input("escolha uma opção de 1-4:")

    if escolha == "1":
        trabalho = input("Digite o nome do trabalho a ser impresso:")
        fila_impressao.adicionar_trabalho(trabalho)
    elif escolha == "2":
        fila_impressao.processar_trabalho()
    elif escolha == "3":
        fila_impressao.mostrar_fila()
    elif escolha == "4":
        print("sair do programa")
        break
    else:
        print("Opção Inválida.")