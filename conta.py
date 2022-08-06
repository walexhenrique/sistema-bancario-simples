from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, numero_conta: int, saldo: float = 100):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    @property
    def agencia(self) -> int:
        return self._agencia

    def transferir(self, conta_destinatario, quantia: float) -> None:
        """
        Método que realiza a transferência de dinheiro para outra conta.

        :param conta_destinatario: Conta a receber o dinheiro.
        :type conta_destinatario: ContaPoupanca or ContaCorrente
        :param quantia: Quantia de dinheiro a ser transferida para a outra conta.
        :type quantia: float or int

        :return: None
        :rtype: None
        """

        if not isinstance(conta_destinatario, (ContaPoupanca, ContaCorrente)):
            raise TypeError('Isso não é um objeto do Tipo (conta)')

        if quantia > self.saldo:
            print(f'Não é possível transferir a quantia de R${quantia}')
            return

        self.saldo -= quantia
        conta_destinatario.saldo += quantia
        print(
            f'O valor de R${quantia} foi transferido com sucesso para a conta de número: {conta_destinatario.numero_conta}')

    @agencia.setter
    def agencia(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError('Isso não é um objeto do Tipo (int)')

        self._agencia = valor

    @property
    def numero_conta(self) -> int:
        return self._numero_conta

    @numero_conta.setter
    def numero_conta(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError('Isso não é um objeto do Tipo (int)')

        self._numero_conta = valor

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float) -> None:
        if not isinstance(valor, (float, int)):
            raise TypeError('Isso não é um número')

        self._saldo = valor

    def depositar(self, quantia: float) -> None:
        """
        Método para depositar quantia de dinheiro na conta do Cliente.

        :param quantia: A quantia de dinheiro a ser depositada.
        :type quantia: float or int

        :return: None
        :rtype: None
        """

        if quantia <= 0:
            print(f'O valor de R${quantia} não pode ser depositado')
            return

        self.saldo += quantia
        print(f'Quantia de R${quantia} depositado com sucesso na conta')

    @abstractmethod
    def sacar(self, quantia: float) -> None:
        pass

    @abstractmethod
    def mostrar_detalhes(self) -> None:
        pass


class ContaPoupanca(Conta):
    """
        Cria um objeto ContaPoupanca para gerenciar as contas poupança dos clientes.

        Atributos:
            agencia (int): Agência responsável pela conta do cliente.
            numero_conta (int): Número da conta do cliente.
            saldo (float): Quantia de dinheiro armazenada na conta do cliente.
    """

    def sacar(self, quantia: float) -> None:
        """
        Método que realiza o saque da conta caso tenha saldo suficiente em conta.

        :param quantia: Valor a ser sacado.
        :type quantia: float or int

        :return: None
        :rtype: None
        """

        if quantia > self.saldo:
            print(f'Não é possível sacar a quantia de R${quantia}')
            return

        self.saldo += quantia
        print(f'A quantia de R${quantia} foi sacada com sucesso')

    def mostrar_detalhes(self) -> None:
        """
        Método que apresenta todos os detalhes da conta do cliente.

        :return: None
        :rtype: None
        """
        print(f'Agência: {self.agencia} '
              f'Número Conta: {self.numero_conta} '
              f'Saldo: R${self.saldo} '
              f'Tipo de conta: Poupança')


class ContaCorrente(Conta):
    """
    Cria um objeto ContaCorrente para gerenciar as Contas Corrente dos Clientes.

    Atributos:
        agencia (int): Agência responsável pela conta do cliente.
        numero_conta (int): Número da conta do cliente.
        saldo (float): Quantia de dinheiro armazenada na conta do cliente.
        limite (float): Quantia de dinheiro para entrar no cheque especial.
    """

    def __init__(self, agencia: int, numero_conta: int, saldo: float = 100, limite: float = 100):
        super().__init__(agencia, numero_conta, saldo)
        self.limite = limite

    @property
    def limite(self) -> float:
        return self._limite

    @limite.setter
    def limite(self, valor: float) -> None:
        if not isinstance(valor, (float, int)):
            raise TypeError('Isso não é um objeto do Tipo (float)')

        self._limite = valor

    def sacar(self, quantia: float) -> None:
        """
        Método que realiza o saque da conta caso tenha saldo e limite suficiente em conta.
        :param quantia: Valor a ser sacado.
        :type quantia: float or int

        :return: None
        :rtype: None
        """
        if (self.saldo + self.limite) < quantia:
            print(f'Não é possivel sacar a quantia de R${quantia}')
            return

        self.saldo -= quantia
        print(f'A quantia de R${quantia} foi sacada com sucesso')

    def mostrar_detalhes(self) -> None:
        """
        Método que apresenta todos os detalhes da conta do cliente.

        :return: None
        :rtype: None
        """
        print(f'Agência: {self.agencia} '
              f'Número Conta: {self.numero_conta} '
              f'Saldo: R${self.saldo} '
              f'Tipo de conta: Corrente '
              f'Limite: R${self.limite}')
