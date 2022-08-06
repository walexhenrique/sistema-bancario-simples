from conta import Conta, ContaCorrente, ContaPoupanca
from typing import Type


class Pessoa:
    def __init__(self, nome: str, cpf: int, idade: int) -> None:
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str) -> None:
        if not isinstance(valor, str):
            raise TypeError('Tipo de dado inválido! Utilize um (str)')

        self._nome = valor

    @property
    def cpf(self) -> int:
        return self._cpf

    @cpf.setter
    def cpf(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise TypeError('Tipo de dado inválido! Utilize um (int)')

        self._cpf = valor

    def mostrar_detalhes(self) -> None:
        """
        Método que apresenta os detalhes do Cliente.

        :return: None
        :rtype: None
        """

        print(f'Nome: {self.nome} '
              f'Cpf: {self.cpf} '
              f'Idade: {self.idade}')


class Cliente(Pessoa):
    """
    Cria um objeto Cliente para ser possível gerenciar o mesmo.

    Atributos:
        nome (str): Nome do cliente.
        cpf (int): Número do cpf do cliente. (cadastrar apenas números)
        idade (int): Idade do cliente.
        conta (ContaPoupanca or ContaCorrente): Conta bancária do cliente.
    """

    def __init__(self, nome: str, cpf: int, idade: int, conta: Type[Conta] = None):
        super().__init__(nome, cpf, idade)
        self.conta = conta

    @property
    def conta(self) -> Type[Conta]:
        return self._conta

    @conta.setter
    def conta(self, valor: Type[Conta]) -> None:
        if not isinstance(valor, (ContaPoupanca, ContaCorrente)) and valor is not None:
            raise TypeError('Isso não é um objeto do Tipo (Conta)')

        self._conta = valor

    def adicionar_conta(self, account: Type[Conta]) -> None:
        """
        Método para cadastrar uma Conta ao cliente.

        :param account: Conta a ser cadastrada, podendo ser do tipo poupança ou corrente.
        :type account: ContaPoupanca or ContaCorrente

        :return: None
        :rtype: None
        """
        self.conta = account
        print(f'Conta adicionada com sucesso! ao cliente {self.nome}')
