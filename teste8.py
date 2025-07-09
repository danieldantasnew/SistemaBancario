class Pedido:
    def __init__(self):
        self.itens = []  
    
    # TODO: Crie um método chamado adicionar_item que recebe um preço e adiciona à lista de itens:
    def adicionar_item(self, nome, preco):
      self.itens.append({"nome": nome, "preco": preco})  
    
        # TODO: Adicione o preço do item à lista:
          

    # TODO: Crie um método chamado calcular_total que retorna a soma de todos os preços da lista:

    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += float(item["preco"])
    
        # TODO: Retorne a soma de todos os preços
        return f"{total:.2f}"
        

quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    #TODO: Chame o método adicionar_item corretamente: 
    pedido.adicionar_item(nome, preco)

# TODO: Exiba o total formatado com duas casas decimais:

print(pedido.calcular_total())