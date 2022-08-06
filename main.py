from pessoa import Cliente
from conta import ContaCorrente, ContaPoupanca
from banco import Banco

"""
    Módulo para testar o sistema bancário
"""

if __name__ == "__main__":

    # Instanciando os clientes
    cliente1 = Cliente(nome='Raimundo', cpf=12054712302, idade=19)
    cliente2 = Cliente(nome='Breno', cpf=15045612304, idade=56)
    cliente3 = Cliente(nome='João', cpf=15044112304, idade=41)

    # Instanciando as contas dos clientes
    conta_cliente1 = ContaPoupanca(agencia=11111, numero_conta=123)
    conta_cliente2 = ContaCorrente(agencia=22222, numero_conta=124, saldo=2500)
    conta_cliente3 = ContaCorrente(agencia=100, numero_conta=101, saldo=120, limite=250)

    # Adicionando as contas aos objetos Cliente
    cliente1.adicionar_conta(conta_cliente1)
    cliente2.adicionar_conta(conta_cliente2)
    cliente3.adicionar_conta(conta_cliente3)

    # Instanciando o Banco e adicionando clientes, contas e agências ao mesmo
    banco = Banco()
    banco.adicionar_cliente(cliente1)
    banco.adicionar_cliente(cliente2)

    banco.adicionar_conta(conta_cliente1)
    banco.adicionar_conta(conta_cliente2)

    banco.adicionar_agencia(11111)
    banco.adicionar_agencia(22222)
    banco.adicionar_agencia(33333)

    cliente1.conta.mostrar_detalhes()
    cliente2.conta.mostrar_detalhes()
    cliente3.conta.mostrar_detalhes()

    # Autenticar para ser possível o cliente realizar saques, depósitos e transferências.
    if banco.autenticar(cliente1):
        cliente1.conta.depositar(120)
        cliente1.conta.transferir(conta_cliente3, 20)
