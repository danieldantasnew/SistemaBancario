valor_final = 0;
# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
valor_final += preco
cupom = input().strip().upper()

# TODO: Aplique o desconto se o cupom for válido:

if cupom in descontos:
    valor_final = valor_final - (valor_final * descontos[cupom])
else:
    print("Cupom inválido")

print(f"{valor_final:.2f}")