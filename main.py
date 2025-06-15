class Banco:
    saldo: float = 0
    extrato: str = ''
    numero_saques_realizados: int = 0
    LIMITE_DE_SAQUES: int = 3
    limite_por_saque: float = 500

    def __init__(self, nome_banco: str) -> None:
        self.nome_banco = nome_banco

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


def menu(nome_banco: str): 
    return f"""
        BEM-VINDO AO {nome_banco}
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Consultar Saldo
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
    
    elif(opcao == '0'):
        print(f"Obrigado por usar {tesla_bank.nome_do_banco()}")
        break
    
    else:
        print('Opção inválida, tente novamente!')