class Conta:
    def __init__(self, nome, senha, numero_conta, saldo=0):
        self.nome = nome
        self.senha = senha
        self.numero_conta = numero_conta
        self.saldo = saldo

class SistemaBancario:
    def __init__(self):
        self.usuarios = {}
        self.criar_conta("Angelo", "123")

    def criar_conta(self, nome, senha):
        numero_conta = len(self.usuarios) + 1
        nova_conta = Conta(nome, senha, numero_conta)
        self.usuarios[numero_conta] = nova_conta
        print(f"\nConta criada com sucesso! Seu número de conta é: {numero_conta} \n")

    def entrar(self, numero_conta, senha):
        if numero_conta in self.usuarios and self.usuarios[numero_conta].senha == senha:
            print(f"\nLogin realizado com sucesso! Seja bem-vindo(a): {self.usuarios[numero_conta].nome}\n")
            return self.usuarios[numero_conta]
        else:
            print("Falha no login. Verifique seu número de conta e senha.")
            return None

def fechar_transacao(conta):
    print("Transação fechada.\n")
        
    opcao_fechamento = menu_fechamento()

    if opcao_fechamento == 1:
        while True:
            opcao_usuario = menu_usuario(conta)
            if opcao_usuario == 1:
                operacao_cash(conta)
            elif opcao_usuario == 2:
                print("Operação de Fund Transfer não implementada.")
            elif opcao_usuario == 3:
                operacao_credit(conta)
            else:
                print("Opção inválida.")
    elif opcao_fechamento == 2:
            print("Saindo do Sistema")
            exit()

def mostrar_informacoes_e_aprovar_pagamento(conta):
    print(f"Usuário: {conta.nome}")
    print(f"Número da conta: {conta.numero_conta}")
    print(f"Saldo: {conta.saldo}")
    print("\nPagamento aprovado com sucesso!\n")
    
    fechar_transacao(conta)

def menu_principal():
    print("1. Entrar")
    print("2. Criar Conta")
    print("3. Sair \n")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def menu_usuario(conta):
    print("\n1. Cash")
    print("2. Fund Transfer")
    print("3. Credit\n")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def menu_fechamento():
    print("1. Nova Transação")
    print("2. Sair")
    opcao = int(input("\nEscolha uma opção: "))
    return opcao

def menu_credit_and_fund():
    print("1. Solicitar Confirmação ao Banco")
    print("2. Cancelar Transação")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def operacao_cash(conta):
    valor = float(input("\nInforme o valor para saque: "))
    if valor > conta.saldo:
        print("\nSaldo insuficiente para realizar o saque.")
        operacao_deposito(conta)
        return
    conta.saldo -= valor
    print(f"\nSaque realizado com sucesso! Seu novo saldo é: {conta.saldo}\n")
    reciboCash(conta)

def operacao_credit(conta):
    valor = float(input("\nInforme o valor para credit: "))    
    opcoes_de_parcelas = opcoes_parcelas()

    numeroDeParcelas = 0

    if opcoes_de_parcelas == 1:
        numeroDeParcelas = 12
    elif opcoes_de_parcelas == 2:
        numeroDeParcelas = 24
    elif opcoes_de_parcelas == 3:
        numeroDeParcelas = 48

    totalComJuros = valor + (valor * 0.10)
    parcelas = (totalComJuros / numeroDeParcelas)

    print(f"\nSolicitação realizada com sucesso ! Dados da solicitação de crédito: \n")

    reciboCredito(conta, valor, totalComJuros, round(parcelas, 2))

    opcao = menu_credit_and_fund()

    if opcao == 1:
        conta.saldo += valor
        mostrar_informacoes_e_aprovar_pagamento(conta)
    elif opcao == 2:
        fechar_transacao()

def opcoes_parcelas():
    print("\n1. 12 Meses")
    print("2. 24 Meses")
    print("3. 48 Meses")
    opcao = int(input("\nEscolha uma opção: "))
    return opcao

def operacao_deposito(conta):
    valor = float(input("\nInforme o valor para depósito: "))
    if valor <= 0:
        print("\nValor inválido para depósito.")
        return
    conta.saldo += valor
    print(f"\nDepósito realizado com sucesso! Seu novo saldo é: {conta.saldo}\n")

def operacao_fund_transfer(conta_origem,sistema):
    numero_conta_destino = int(input("\nInforme o número da conta de destino: "))
    if numero_conta_destino not in sistema.usuarios:
        print("Conta de destino não encontrada.")
        return
    conta_destino = sistema.usuarios[numero_conta_destino]
    valor = float(input("Informe o valor para transferência: "))
    if valor > conta_origem.saldo:
        print("\nSaldo insuficiente para realizar a transferência.")
        operacao_deposito(conta_origem)
        return
    conta_origem.saldo -= valor
    conta_destino.saldo += valor
    print(f"\nTransferência realizada com sucesso! Seu novo saldo é: {conta_origem.saldo}\n")
    opcao_fund = menu_credit_and_fund()
    if opcao_fund == 1:
        reciboFund(conta_origem, conta_destino, valor)
    else:
        sistema.fechar_transacao(conta_origem)

def reciboCash(conta):
    print("----RECIBO-CASH----")
    print(f"Usuário: {conta.nome}")
    print(f"Número da conta: {conta.numero_conta}")
    print(f"Saldo: {conta.saldo}")
    print("----RECIBO-CASH----\n")
    completar_transacao(conta)

def reciboFund(conta_origem, conta_destino, valor):
    print("----RECIBO----")
    print(f"Transferência de {valor} realizada com sucesso.")
    print(f"Conta de origem: {conta_origem.nome}, Número: {conta_origem.numero_conta}, Saldo: {conta_origem.saldo}")
    print(f"Conta de destino: {conta_destino.nome}, Número: {conta_destino.numero_conta}, Saldo: {conta_destino.saldo} \n")
    completar_transacao(conta_origem)

def reciboCredito(conta, valor_solicitado, total_com_juros, valor_parcela):
    print("----RECIBO DE CRÉDITO----")
    print(f"Solicitação de crédito de {valor_solicitado}.")
    print(f"Nome do usuário: {conta.nome}, Número da conta: {conta.numero_conta}, Saldo Atual: {conta.saldo}")
    print(f"Valor total com juros: {total_com_juros}, Valor da parcela: {valor_parcela}")
    print("----RECIBO DE CRÉDITO----\n")
    completar_transacao(conta)

def completar_transacao(conta):
    print("Transação Completa \n")
    mostrar_informacoes_e_aprovar_pagamento(conta)

def main():
    sistema = SistemaBancario()
    while True:
        opcao = menu_principal()
        if opcao == 1:
            numero_conta = int(input("\nInforme o número da conta: "))
            senha = input("Informe a senha: ")
            conta = sistema.entrar(numero_conta, senha)
            if conta:
                while True:
                    opcao_usuario = menu_usuario(conta)
                    if opcao_usuario == 1:
                        operacao_cash(conta)
                    elif opcao_usuario == 2:
                        operacao_fund_transfer(conta,sistema)
                    elif opcao_usuario == 3:
                        operacao_credit(conta)
                    else:
                        print("Opção inválida.")
        elif opcao == 2:
            nome = input("\nInforme o nome: ")
            senha = input("Informe a senha: ")
            sistema.criar_conta(nome, senha)
        elif opcao == 3:
            print("Saindo do sistema.")
            exit()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()