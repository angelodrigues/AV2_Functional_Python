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

    criar_conta = lambda self, nome, senha: (print(f"\nConta criada com sucesso! Seu número de conta é: {len(self.usuarios) + 1} \n") or self.usuarios.update({len(self.usuarios) + 1: Conta(nome, senha, len(self.usuarios) + 1)}))
    entrar = lambda self, numero_conta, senha: (self.usuarios[numero_conta].senha == senha and self.usuarios[numero_conta]) or (print("Falha no login. Verifique seu número de conta e senha."), None)

#CONCLUSÕES#
fechar_transacao = lambda: (print("Transação fechada.\n"), print("Saindo do Sistema"), exit())
completar_transacao = lambda conta: (print("Transação Completa \n"),mostrar_informacoes_e_aprovar_pagamento(conta))
#CONCLUSÕES#

mostrar_informacoes_e_aprovar_pagamento = lambda conta: (
    (print(f"Usuário: {conta.nome}"),
    print(f"Número da conta: {conta.numero_conta}"),
    print(f"Saldo: {conta.saldo}"),
    print("\nPagamento aprovado com sucesso!\n"),
    fechar_transacao())
)
mostrar_informacoes_e_aprovar_pagamento_credit = lambda conta,saldo: (
    (print(f"\nUsuário: {conta.nome}"),
    print(f"Número da conta: {conta.numero_conta}"),
    print(f"Saldo: {saldo}"),
    print("\nPagamento aprovado com sucesso!\n"),
    fechar_transacao())
)
#MENU#
menu_principal = lambda: int(input("\n1. Entrar\n2. Criar Conta\n3. Sair\n\nEscolha uma opção: "))
menu_usuario = lambda: int(input("\n1. Cash\n2. Fund Transfer\n3. Credit\n\nEscolha uma opção: "))
menu_credit_and_fund = lambda: int(input("1. Solicitar Confirmação ao Banco\n2. Cancelar Transação\n\nEscolha uma opção: "))
menu_parcelas = lambda: int(input("\n1. 12 Meses\n2. 24 Meses\n3. 48 Meses\n\nEscolha uma opção: "))
#MENU#

#OPERAÇÕES#
operacao_cash = lambda conta: (
    (lambda valor: (
        (setattr(conta, 'saldo', conta.saldo - valor),
         print(f"\nSaque realizado com sucesso! Seu novo saldo é: {conta.saldo}\n"),
         reciboCash(conta))
        if valor <= conta.saldo else (
            print("\nSaldo insuficiente para realizar o saque."),
            operacao_deposito(conta)
        )
    ))
)(float(input("\nInforme o valor para saque: ")))

def operacao_credit(conta):
    valor = lambda: float(input("\nInforme o valor para credit: ")) 
    valor = valor()   
    opcoes_de_parcelas = lambda: menu_parcelas()
    opcoes_de_parcelas = opcoes_de_parcelas()
    numeroDeParcelas = lambda opcoes_de_parcelas: 12 if opcoes_de_parcelas == 1 else 24 if opcoes_de_parcelas == 2 else 48 if opcoes_de_parcelas == 3 else None
    totalComJuros = lambda valor: valor + (valor * 0.10)
    parcelas = lambda: (totalComJuros(valor) / numeroDeParcelas(opcoes_de_parcelas))

    print(f"\nSolicitação realizada com sucesso ! Dados da solicitação de crédito: \n")

    opcao = lambda: menu_credit_and_fund()
    opcao = opcao()

    saldo = conta.saldo = conta.saldo + valor
    condicional = lambda opcao, conta, saldo: (reciboCredito(conta, valor, totalComJuros(valor), round(parcelas(), 2)),mostrar_informacoes_e_aprovar_pagamento_credit(conta,saldo)) if opcao == 1 else fechar_transacao() if opcao == 2 else None
    condicional(opcao,conta,saldo)

    

operacao_deposito = lambda conta: (
    (lambda valor: (
        (print("\nValor inválido para depósito.") if valor <= 0 else (
            setattr(conta, 'saldo', conta.saldo + valor),
            print(f"\nDepósito realizado com sucesso! Seu novo saldo é: {conta.saldo}\n")
        ))
    ))
)(float(input("\nInforme o valor para depósito: ")))

def operacao_fund_transfer(conta_origem,sistema):
    numero_conta_destino = lambda: int(input("\nInforme o número da conta de destino: "))
    numero_conta_destino = numero_conta_destino()
    verifica_conta = lambda: print("Conta de destino não encontrada.") if numero_conta_destino not in sistema.usuarios else None
    verifica_conta()
    conta_destino = lambda: sistema.usuarios[numero_conta_destino]
    conta_destino = conta_destino()
    opcao_fund = lambda: menu_credit_and_fund()
    condicional = lambda valor,opcao_fund,conta_origem,conta_destino: reciboFund(conta_origem, conta_destino, valor) if opcao_fund == 1 else fechar_transacao()
    transferencia = lambda conta_origem, conta_destino: (
    (lambda valor: (
        (setattr(conta_origem, 'saldo', conta_origem.saldo - valor),
            setattr(conta_destino, 'saldo', conta_destino.saldo + valor),
            print(f"\nTransferência realizada com sucesso! Seu novo saldo é: {conta_origem.saldo}\n"),            
            condicional(valor,opcao_fund(),conta_origem,conta_destino))
            if valor <= conta_origem.saldo else (
                print("\nSaldo insuficiente para realizar a transferência."),
                operacao_deposito(conta_origem)
            )
        ))
    )(float(input("\nInforme o valor para transferência: ")))
    transferencia(conta_origem,conta_destino)
#OPERAÇÕES#

#RECIBOS#
reciboCash = lambda conta: (
    print("----RECIBO-CASH----"),
    print(f"Usuário: {conta.nome}"),
    print(f"Número da conta: {conta.numero_conta}"),
    print(f"Saldo: {conta.saldo}"),
    print("----RECIBO-CASH----\n"),
    completar_transacao(conta)
)
reciboFund = lambda conta_origem, conta_destino, valor: (
    print("----RECIBO-FUND----"),
    print(f"Transferência de {valor} realizada com sucesso."),
    print(f"Conta de origem: {conta_origem.nome}, Número: {conta_origem.numero_conta}, Saldo: {conta_origem.saldo}"),
    print(f"Conta de destino: {conta_destino.nome}, Número: {conta_destino.numero_conta}, Saldo: {conta_destino.saldo}"),
    print("----RECIBO-FUND----"),
    completar_transacao(conta_origem)
)
reciboCredito = lambda conta, valor_solicitado, total_com_juros, valor_parcela: (
    print("----RECIBO DE CRÉDITO----"),
    print(f"Solicitação de crédito de {valor_solicitado}."),
    print(f"Nome do usuário: {conta.nome}, Número da conta: {conta.numero_conta}, Saldo Atual: {conta.saldo}"),
    print(f"Valor total com juros: {total_com_juros}, Valor da parcela: {valor_parcela}"),
    print("----RECIBO DE CRÉDITO----\n"),
    completar_transacao(conta)
)
#RECIBOS#
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
                    opcao_usuario = menu_usuario()
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
            print("\nSaindo do sistema.")
            exit()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()