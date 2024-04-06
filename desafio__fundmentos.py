from colorama import Fore, Style

# Função para realizar um depósito
def depositar(saldo, extrato):
    try:
        valor = float(input(Fore.GREEN + "💰 Informe o valor do depósito: " + Style.RESET_ALL))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(Fore.GREEN + "💰 Depósito realizado com sucesso." + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ Operação falhou! O valor informado é inválido." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "❌ Operação falhou! Valor inválido." + Style.RESET_ALL)
    return saldo, extrato

# Função para realizar um saque
def sacar(*, saldo, extrato, numero_saques, limite):
    try:
        valor = float(input(Fore.GREEN + "💸 Informe o valor do saque: " + Style.RESET_ALL))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite

        if excedeu_saldo:
            print(Fore.RED + "❌ Operação falhou! Você não tem saldo suficiente." + Style.RESET_ALL)
        elif excedeu_limite:
            print(Fore.RED + "❌ Operação falhou! O valor do saque excede o limite." + Style.RESET_ALL)
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(Fore.GREEN + "💸 Saque realizado com sucesso." + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ Operação falhou! O valor informado é inválido." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "❌ Operação falhou! Valor inválido." + Style.RESET_ALL)
    return saldo, extrato, numero_saques

# Função para exibir o extrato
def exibir_extrato(saldo, *, extrato):
    print(Fore.YELLOW + "\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================" + Style.RESET_ALL)

# Função para cadastrar usuário
def cadastrar_usuario(usuarios):
    nome = input(Fore.BLUE + "👤 Informe o nome do usuário: " + Style.RESET_ALL)
    data_nascimento = input(Fore.BLUE + "📅 Informe a data de nascimento (DD/MM/AAAA): " + Style.RESET_ALL)
    cpf = input(Fore.BLUE + "🔢 Informe o CPF do usuário: " + Style.RESET_ALL)

    # Validar CPF
    if not cpf.isdigit() or len(cpf) != 11:
        print(Fore.RED + "❌ CPF inválido." + Style.RESET_ALL)
        return

    # Verificar se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print(Fore.RED + "❌ CPF já cadastrado. Não é permitido cadastrar dois usuários com o mesmo CPF." + Style.RESET_ALL)
            return

    endereco = input(Fore.BLUE + "🏠 Informe o endereço (logradouro, numero - bairro - cidade/estado): " + Style.RESET_ALL)

    # Adicionar usuário à lista de usuários
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco, 'contas': []})
    print(Fore.GREEN + "👤 Usuário cadastrado com sucesso." + Style.RESET_ALL)

# Função para buscar usuário por CPF
def buscar_usuario_por_cpf(usuarios, cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

# Função para cadastrar conta bancária
def cadastrar_conta_bancaria(usuarios, numero_conta):
    cpf = input(Fore.BLUE + "🔢 Informe o CPF do usuário para vincular a conta bancária: " + Style.RESET_ALL)

    # Buscar usuário na lista de usuários
    usuario = buscar_usuario_por_cpf(usuarios, cpf)

    if usuario:
        tipo_conta = input(Fore.BLUE + "💼 Informe o tipo da conta bancária (corrente/poupança): " + Style.RESET_ALL).lower()
        while tipo_conta not in ['corrente', 'poupança']:
            print(Fore.RED + "❌ Tipo de conta inválido. Por favor, informe corrente ou poupança." + Style.RESET_ALL)
            tipo_conta = input(Fore.BLUE + "💼 Informe o tipo da conta bancária (corrente/poupança): " + Style.RESET_ALL).lower()
        # Adicionar nova conta bancária à lista de contas do usuário
        usuario['contas'].append({'agencia': '0001', 'numero_conta': numero_conta, 'tipo_conta': tipo_conta})
        print(Fore.GREEN + f"💼 Conta bancária do usuário {usuario['nome']} cadastrada com sucesso." + Style.RESET_ALL)
    else:
        print(Fore.RED + "❌ CPF não encontrado. Por favor, cadastre o usuário antes de vincular a conta bancária." + Style.RESET_ALL)

# Lista para armazenar usuários e contas
usuarios = []
contas = []
numero_conta = 1  # Inicializar o número da conta

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    menu = Fore.YELLOW + """
    ╔═════════════════════════════════╗
    ║          MENU PRINCIPAL         ║
    ╠═════════════════════════════════╣
    ║ [d] 💰 Depositar                ║
    ║ [s] 💸 Sacar                    ║
    ║ [e] 📄 Extrato                  ║
    ║ [u] 👤 Cadastrar Usuário        ║
    ║ [c] 📋 Cadastrar Conta Bancária ║
    ║ [q] 🚪 Sair                     ║
    ╚═════════════════════════════════╝
    """ + Style.RESET_ALL

    print(menu)

    opcao = input("Selecione uma opção: ")

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=limite)
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == "u":
        cadastrar_usuario(usuarios)
    elif opcao == "c":
        cadastrar_conta_bancaria(usuarios, numero_conta)
        numero_conta += 1  # Incrementar o número da conta
    elif opcao == "q":
        break
    else:
        print(Fore.RED + "❌ Opção inválida, por favor selecione novamente." + Style.RESET_ALL)
