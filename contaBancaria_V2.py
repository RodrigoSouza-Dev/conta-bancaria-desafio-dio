saldo = 0
saques_realizados = 0
saques_total = 0
usuarios = []
contas = []

def deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido. O valor do depósito deve ser positivo.")

def saque(valor):
    global saldo, saques_realizados, saques_total
    if valor > 0:
        if saques_realizados < 3 and valor <= 500 and saques_total + valor <= 1500:
            if saldo >= valor:
                saldo -= valor
                saques_realizados += 1
                saques_total += valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print(">>>>>>>>>>>>>>>Saldo insuficiente para realizar o saque.<<<<<<<<<<<<<<<")
        else:
            print(">>>>>>>>>>>>>>>Limite diário de saques atingido.<<<<<<<<<<<<<<<")
    else:
        print(">>>>>>>>>>>>>>Valor inválido. O valor do saque deve ser positivo.<<<<<<<<<<<<<<<")

def exibir_extrato():
    print("\n================ EXTRATO ================")
    if saques_realizados == 0:
        print("Não foram realizadas movimentações.")
    else:
        extrato_movimentacoes = f"Saques realizados: {saques_realizados}\nTotal de saques: R${saques_total:.2f}\n"
        print(extrato_movimentacoes)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario():
    cpf = input("Informe o CPF (somente número): ")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")

def criar_conta():
    cpf = input("Informe o CPF do titular da conta: ")
    titular = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if titular:
        numero_conta = len(contas) + 1
        contas.append({"numero_conta": numero_conta, "titular": titular})
        print(f"Conta {numero_conta} criada com sucesso!")
    else:
        print("Titular não encontrado. Não foi possível criar a conta.")

def listar_contas():
    if len(contas) > 0:
        print("=== LISTA DE CONTAS ===")
        for conta in contas:
            print(f"Conta: {conta['numero_conta']}")
            print(f"Titular: {conta['titular']['nome']}")
            print()
    else:
        print("Não há contas cadastradas.")

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepósito
    [2]\tSaque
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair
    => """
    return input(menu)

while True:
    opcao = menu()

    if opcao == '1':
        valor = float(input("Digite o valor do depósito: "))
        deposito(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor do saque: "))
        saque(valor)
    elif opcao == '3':
        exibir_extrato()
    elif opcao == '4':
        criar_conta()
    elif opcao == '5':
        listar_contas()
    elif opcao == '6':
        criar_usuario()
    elif opcao == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
