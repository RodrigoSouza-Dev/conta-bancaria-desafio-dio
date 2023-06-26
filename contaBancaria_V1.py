saldo = 0
saques_realizados = 0
saques_total = 0
SAQUES_TOTAL = 1500
historico = []

def deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
        historico.append(f"Depósito de R${valor:.2f} realizado.")
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido. O valor do depósito deve ser positivo.")

def saque(valor):
    global saldo, saques_realizados, saques_total
    if valor > 0:
        if saques_realizados < 3 and saques_total + valor <= SAQUES_TOTAL and valor <= 500:
            if saldo >= valor:
                saldo -= valor
                saques_realizados += 1
                saques_total += valor
                historico.append(f"Saque de R${valor:.2f} realizado.")
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            if valor > 500:
                print("\n------------------Valor máximo por saque é de R$500.00!------------------\n")
            else:
                print("\n------------------Limite diário de saques atingido.------------------\n")
    else:
        print("Valor inválido. O valor do saque deve ser positivo.")

def extrato():
    print(f"Saldo atual: R${saldo:.2f}")
    print("Histórico de transações:")
    for transacao in historico:
        print(transacao)

while True:
    print("\nOpções de acesso:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("0 - Sair \n")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor = float(input("Digite o valor do depósito: "))
        deposito(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor do saque: "))
        saque(valor)
    elif opcao == '3':
        extrato()
    elif opcao == '0':
        break
    else:
        print("\n>>>>>>>>>>>>>>>>>>>>Opção inválida! Escolha: 1 - Depósito, 2 - Saque, 3 - Extrato, 0 - Sair.")
