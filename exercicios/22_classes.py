from datetime import datetime

class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'{self.titular} tem R$ {self.saldo.replace('.', ',')} de saldo na conta.'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return f'{self._saldo:.2f}'
    
    @property
    def ativo(self):
        return 'ativa' if self._ativo else 'inativa'
        


class ClienteBanco:
    def __init__(self, nome, data_nasc, endereco, telefone, profissao):
        self.nome = nome
        self.data_nasc = data_nasc
        self.telefone = telefone
        self.endereco = endereco
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}.'
        
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta

    @property
    def idade(self):
        data_atual = datetime.now()
        data_nasc = datetime.strptime(self.data_nasc, '%Y-%m-%d')
        
        return  (data_atual - data_nasc).days // 365


# Cria instâncias da Conta Bancária
conta1 = ContaBancaria(titular='George', saldo=100)
conta2 = ContaBancaria(titular='Rita', saldo=550.45)


# Imprime mensagem com informações da conta
print(conta1)
print(conta2)
print()


# Ativa a conta
print(f'Conta de {conta1.titular} está ativa? (antes) {conta1.ativo}')
ContaBancaria.ativar_conta(conta1)
print(f'Conta de {conta1.titular} está ativa? (depois) {conta1.ativo}')
print()


# Imprime o valor da propriedade Titular
print(f'Titular da conta 1: {conta1.titular}')
print()


# Cria instâncias para os Clientes
cliente1 = ClienteBanco(nome='Harry', data_nasc='1980-07-31', telefone=55556666, endereco='4, Privet Drive', profissao='Auror')
cliente2 = ClienteBanco(nome='Hermione', data_nasc='1979-09-19', telefone=88884444, endereco='9, Heathgate Street', profissao='Ministra da Magia')


# Mostra informações do cliente
print(f'Informações do cliente: {cliente1}')
print()


# Usando método da classe
conta_cliente1 = ClienteBanco.criar_conta('Harry', 100)
print(f'Conta de {conta_cliente1.titular} criada com saldo de R$ {conta_cliente1.saldo.replace('.', ',')}.')
