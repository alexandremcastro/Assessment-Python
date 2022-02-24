def mostrarMenu():
    print('\n======= BANCO =======')
    print('1. Inclusao de conta')
    print('2. Alteraçao de saldo')
    print('3. Exclusao de conta')
    print('4. Relatorios gerenciais')
    print('5. Sair do programa\n')
    escolha = input('Escolha uma opcao: ')
    return escolha
    
def contaExiste(numero_conta):
    for conta in contas:
        if (conta[0] == numero_conta):
            return True
    return False

def inputNumeroConta():
    while True:
        try:
            numero_conta = int(input('Digite o número da conta: '))
        except:
            print('Numero da conta invalido!')
        else:
            if (numero_conta > 0):
                return numero_conta
            print('Numero da conta invalido!')

def inputNome():
    while True:
        nome = input('Digite o nome do correntista: ')
        try:
            if (len(nome.split()) >= 2):
                return nome
            print('Nome invalido!')
        except:
            print('Nome invalido!')

def inputSaldo():
    while True:
        try:
            saldo = float(input('Digite o saldo: '))
        except:
            print('Saldo invalido!')
        else:
            if (saldo >= 0):
                return saldo
            print('Saldo invalido!')

def criarConta():
    while True:
        numero_conta = inputNumeroConta()
        if not contaExiste(numero_conta):
            break
        print('Essa conta ja existe!')
    nome = inputNome()
    saldo = inputSaldo()
    contas.append([numero_conta, nome, saldo])

def listaVazia():
    if (len(contas) == 0):
        print('A lista de contas esta vazia!')
        return True
    return False

def menuInputOperacao():
    print('\n1. Credito')
    print('2. Debito\n')
    escolha = input('Qual operacao voce deseja? ')
    return escolha

def entradaInputOperacao():
    while True:
        escolha = menuInputOperacao()
        if (escolha == '1') or (escolha == '2'):
            break

def inputOperacao():
    entradaInputOperacao()
        
    while True:
        try:
            quantia = float(input('Digite a quantia: '))
        except:
            print('Quantia invalida!')
        else:
            if (quantia > 0):
                if (escolha == '2'):
                    quantia *= -1
                return quantia
            print('Quantia invalida!')

def encontrarConta(num):
    for conta in contas:
        if (conta[0] == num):
            return conta
        
def alterarSaldoCondicao():
    while True:
        numero_conta = inputNumeroConta()
        if contaExiste(numero_conta):
            break
        print('Essa conta nao existe!')
    quantia_operacao = inputOperacao()
    conta = encontrarConta(numero_conta)
    conta[2] += quantia_operacao
           
def alterarSaldo():
    if listaVazia():
        return
    alterarSaldoCondicao()
    
def excluirCondicaoEntrada():
    while True:
        numero_conta = inputNumeroConta()
        if contaExiste(numero_conta):
            break
        print('Essa conta nao existe!')
    return numero_conta
    
def excluirCondicao():
        numero_conta = excluirCondicaoEntrada()
        conta = encontrarConta(numero_conta)
        if (conta[2] == 0):
            contas.remove(conta)
        else:
            print('Para excluir a conta o saldo precisar ser 0.')

def excluirConta():
    if listaVazia():
        return
    excluirCondicao()

def menuRelatorios():
    print('\n1. Listar os clientes com saldo negativo')
    print('2. Listar os clientes que tem saldo acima de um determinado valor')
    print('3. Listar todas as contas\n')
    escolha = input('Qual opcao voce deseja? ')
    return escolha

def listarNegativados():
    for conta in contas:
        if (conta[2] < 0):
            print(conta[1])

def listarAcimaDe(valor):
    for conta in contas:
        if (conta[2] > valor):
            print(conta[1])

def listarTodos():
    for conta in contas:
        print("Conta: ", conta[0])
        print("    Nome: ", conta[1])
        print("    Saldo: ", conta[2])

def relatioriosCondicoes(escolha):
    if (escolha == '1'):
        listarNegativados()
    elif (escolha == '2'):
        valor = float(input('Qual valor voce deseja? '))
        listarAcimaDe(valor)
    elif (escolha == '3'):
        listarTodos()
    else:
        print('Opcao invalida!')
        return escolha
    
def entradaRelatoriosGerenciais():
    while True:
        escolha = menuRelatorios()
        relatioriosCondicoes(escolha)
        break
    
def relatoriosGerenciais():
    if listaVazia():
        return
    entradaRelatoriosGerenciais()
    
def leArquivo():
    with (open('contas.txt', 'r')) as arquivo_contas:
        for linha in arquivo_contas.readlines():
            infos = linha.strip('/n')
            infos = linha.split(';')
            infos[0] = int(infos[0])
            infos[2] = float(infos[2].replace('\n', ''))
            contas.append(infos)
            return arquivo_contas
            
def gravaArquivo():
    with open('contas.txt', 'w') as arquivo_contas:
        for conta in contas:
            arquivo_contas.write("{};{};{}\n".format(conta[0], conta[1], conta[2]))
    print('Arquivo gravado')
            
contas = []
leArquivo()
while True:
    escolha = mostrarMenu()
    if (escolha == '1'):
        criarConta()
    elif (escolha == '2'):
        alterarSaldo()
    elif (escolha == '3'):
        excluirConta()
    elif (escolha == '4'):
        relatoriosGerenciais()
    elif (escolha == '5'):
        break
    else:
        print('Opcao invalida!')
gravaArquivo()