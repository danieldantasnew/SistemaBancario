class Conta:
    def __init__(self, numero_conta, usuario):
        self.agencia: str = "0001"
        self.numero_conta = numero_conta
        self.usuario_conta = usuario

    def mostrar_conta(self):
        return f"Agência: {self.agencia} Conta: {self.numero_conta}"

class Usuario:
    def __init__(self) -> None:
        self.nome:str = ''
        self.data_de_nascimento:str = ''
        self.cpf:str = ''
        self.endereco:str = ''
        self.conta: Conta|None = None


class Banco:
    def __init__(self, nome_banco: str) -> None:
        self.numero_de_contas = 0
        self.nome_banco = nome_banco
        self.saldo: float = 0
        self.extrato: str = ''
        self.numero_saques_realizados: int = 0
        self.LIMITE_DE_SAQUES: int = 3
        self.limite_por_saque: float = 500
        self.contas = []
        self.usuarios = []

    def nome_do_banco(self):
        return self.nome_banco

    def depositar(self):
        print("=== DEPÓSITO ===")
        while True:
            try:           
                valor = float(input('Digite o valor que deseja depositar: ')) 
                
                if valor <= 0:
                    raise ValueError(f"Valor inválido para depósito, apenas valores positivos são permitidos.")
                
                self.saldo += valor
                self.extrato += f"Usuário depositou {valor} em sua conta\n"
                print(f"Depósito de {valor} realizado com sucesso!")
                self.consultar_saldo()
                break

            except ValueError as erro:
                print(f"Erro: {erro}")

    def sacar(self):
        print("=== SAQUE ===")
        while True:
            try:           
                valor = float(input('Digite o valor que deseja sacar: ')) 
                
                if valor > self.saldo :
                    print(f"O valor para saque é maior que o disponível no seu saldo")
                
                elif(self.numero_saques_realizados >= self.LIMITE_DE_SAQUES):
                    print(f"Número de saques excedidos, o número máximo é de {self.LIMITE_DE_SAQUES}.")

                elif(valor > self.limite_por_saque):
                    print(f"O limite máximo por saque é de R${self.limite_por_saque}, tente novamente.")
                
                else:
                    self.numero_saques_realizados+=1
                    self.saldo -= valor
                    self.extrato += f"Usuário sacou {valor} em sua conta\n"
                    print(f"Saque de {valor} realizado com sucesso!")
                
                self.consultar_saldo()
                break

            except ValueError as erro:
                print(f"Erro: {erro}")

    def consultar_extrato(self):
        print(f"=== EXTRATO BANCÁRIO ===")
        
        if(len(self.extrato) == 0):
            print("Não existe histórico de movimentações")
        
        else:
            print(self.extrato)
        
        self.consultar_saldo()

    def consultar_saldo(self):
        print(f"SALDO ATUAL: {self.saldo}")

    def ja_existe_cpf(self, cpf):
        return any(cpf == usuario.cpf for usuario in self.usuarios)
    
    def existe_usuario(self, nome_usuario):
        return any(nome_usuario == usuario.nome for usuario in self.usuarios)
    
    def criar_usuario(self):
        usuario = Usuario()
        usuario.nome = input("Digite o nome do usuário: ").strip()
        usuario.cpf = input("Digite o seu CPF: ").strip()
        while self.ja_existe_cpf(usuario.cpf):
            print('Já existe um usuário cadastrado com este CPF.')
            usuario.cpf = input("Digite o seu CPF: ").strip()

        usuario.data_de_nascimento = input("Digite a sua data de nascimento: ").strip()
        usuario.endereco = input("Digite o seu endereço completo: ").strip()
        self.numero_de_contas+=1
        usuario.conta = Conta(self.numero_de_contas, usuario.nome)
        self.usuarios.append(usuario)
        self.contas.append(usuario.conta)
        print(f"Usuário {usuario.nome} | {usuario.conta.mostrar_conta()} | criado com sucesso!")

    def criar_nova_conta(self):
        usuario = input("Digite o seu usuário: ").strip()
        while not self.existe_usuario(usuario):
            print("Digite um usuário existente!")
            usuario = input("Digite o seu usuário: ").strip()
        self.numero_de_contas+=1
        nova_conta = Conta(self.numero_de_contas, usuario)
        self.contas.append(nova_conta)
        print(f"Conta: {nova_conta.numero_conta} | Agência: {nova_conta.agencia} criados com sucesso para o usuário {usuario}")
        

    def listar_contas(self):
        for conta in self.contas:
            print(f"\nAgência: {conta.agencia} Conta: {conta.numero_conta}")
    
    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"\n Usuário: {usuario.nome} CPF: {usuario.cpf} Conta: {usuario.conta.numero_conta}")
    


def menu(nome_banco: str): 
    return f"""
        BEM-VINDO AO {nome_banco}
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Consultar Saldo
        [5] Criar Usuário/Conta
        [6] Criar Nova Conta
        [7] Listar Contas
        [8] Listar Usuarios
        [0] Sair
    """


tesla_bank = Banco('Tesla Bank')

while True:
    opcao = input(menu(tesla_bank.nome_do_banco()))

    if(opcao == '1'):
        tesla_bank.depositar()
    
    elif(opcao == '2'):
        tesla_bank.sacar()
    
    elif(opcao == '3'):
        tesla_bank.consultar_extrato()
    
    elif(opcao == '4'):
        tesla_bank.consultar_saldo()

    elif(opcao == '5'):
        tesla_bank.criar_usuario()

    elif(opcao == '6'):
        tesla_bank.criar_nova_conta()
        
    elif(opcao == '7'):
        tesla_bank.listar_contas()
    
    elif(opcao == '8'):
        tesla_bank.listar_usuarios()
    
    elif(opcao == '0'):
        print(f"Obrigado por usar {tesla_bank.nome_do_banco()}")
        break
    
    else:
        print('Opção inválida, tente novamente!')