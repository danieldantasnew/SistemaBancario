# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)

    if(status == 'urgente'):
        status = 1
    elif (idade>= 60):
        status = 2
    else:
        status = 3
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:

pacientes.sort(key=lambda item: (item[2], -item[1]))

# TODO: Exiba a ordem de atendimento com título e vírgulas:
resultado = ''

for index, paciente in enumerate(pacientes):
    if(index == 0):
        resultado += paciente[0]
    else:
        resultado += f", {paciente[0]}"

print(f"Ordem de Atendimento: {resultado}")