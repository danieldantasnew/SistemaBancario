from datetime import datetime

# TODO: Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos:
# TODO: Implemente o método verificar_antiguidade e calcule a diferença entre o ano atual e o ano do veículo:

class Veiculo:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  def verificar_antiguidade(self):
    antiguidade = datetime.now().year - self.ano
    return "Veículo antigo" if antiguidade > 20 else "Veículo novo"
    

# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())