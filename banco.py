from pessoa import Cliente
from conta import Conta, ContaCorrente, ContaPoupanca
from typing import Type


class Banco:
    """
    Cria um objeto de Banco que gerencia e controla as agências, clientes e contas.

    atributos:
        contas (list): Lista de objetos do tipo Cliente.
        agencias (list): Lista de inteiros determinando as agências.
        contas (list): Lista de objetos dos tipos ContaPoupanca e ContaCorrente.
    """

    def __init__(self):
        self._contas = []
        self._agencias = []
        self._clientes = []

    def adicionar_cliente(self, cliente: Type[Cliente]) -> None:
        """
        Método para adicionar um cliente na base de dados do banco.
        :param cliente: Cliente a ser cadastrado.
        :type cliente: Cliente

        :return: None
        :rtype: None

        :raise TypeError: Se tentar adicionar algo que não seja um objeto da classe Cliente.
        """
        if not isinstance(cliente, Cliente):
            raise TypeError('Isso não é um objeto do Tipo (Cliente)')

        self._clientes.append(cliente)
        print(f'Cliente {cliente.nome} foi adicionado(a) com sucesso')

    def adicionar_agencia(self, agencia: int) -> None:
        """
        Método para adicionar uma agência na base de dados do banco.
        :param agencia: agência a ser cadastrado no banco.
        :type agencia: int

        :return: None
        :rtype: None

        :raise TypeError: Se tentar adicionar algo que não seja um inteiro.
        """
        if not isinstance(agencia, int):
            raise TypeError('Tipo de dado inválido! Utilize um (int)')

        self._agencias.append(agencia)
        print(f'Agência {agencia} foi adicionada com sucesso')

    def adicionar_conta(self, conta: Type[Conta]) -> None:
        """
        Método para adicionar uma Conta na base de dados do banco.
        :param conta: Conta a ser cadastrada.
        :type conta: ContaPoupanca or ContaCorrente

        :return: None
        :rtype: None

        :raise TypeError: Se tentar adicionar algo que não seja um objeto da classe ContaPoupanca ou ContaCorrente.
        """
        if not isinstance(conta, (ContaCorrente, ContaPoupanca)):
            raise TypeError('Tipo de dado inválido! Utilize um (int)')

        self._contas.append(conta)
        print(f'Conta de número {conta.numero_conta} foi adicionada com sucesso')

    def autenticar(self, cliente: Type[Cliente]) -> bool:
        """
        Método que permite autenticar um Cliente para a realização de depósitos.
        :param cliente: Cliente a ser autenticado.
        :type cliente: Cliente

        :return: Retorna se foi possível autenticar o cliente neste banco.
        :rtype: bool

        :raise TypeError: Caso tente autenticar algo que não seja um objeto Cliente.
        """
        if not isinstance(cliente, Cliente):
            raise TypeError('Isso não é um objeto do Tipo (Cliente)')

        if not cliente in self._clientes:
            return False

        if not cliente.conta in self._contas:
            return False

        if not cliente.conta.agencia in self._agencias:
            return False

        return True
