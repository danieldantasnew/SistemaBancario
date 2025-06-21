# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:

for _ in range(n):
  linha = input().strip()
  nome, tema = [parte.strip() for parte in linha.split(",")]
  
  if tema not in eventos:
    eventos[tema] = []
  
  eventos[tema].append(nome)

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")