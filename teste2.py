# Entrada do usuário
email = input().strip()

# Verificações básicas
if " " in email:
    print("E-mail inválido")
elif email.startswith("@") or email.endswith("@"):
    print("E-mail inválido")
elif email.count("@") != 1:
    print("E-mail inválido")
elif not (email.endswith("@gmail.com") or email.endswith("@outlook.com")):
    print("E-mail inválido")
else:
    print("E-mail válido")
