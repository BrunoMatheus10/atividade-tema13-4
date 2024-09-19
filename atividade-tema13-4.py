# Solicita ao usuário que insira um CPF para validação
cpf = input("Digite o CPF para validação (somente números): ")

# Inicializa a variável de controle
valido = True  # Indica se o CPF é válido

# Verifica se o CPF tem 11 dígitos
if len(cpf) != 11:
    valido = False

# Verifica se todos os caracteres são dígitos
i = 0
while i < len(cpf) and valido:
    if not ('0' <= cpf[i] <= '9'):
        valido = False
    i += 1

# Calcula o primeiro dígito verificador
if valido:
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Verifica o primeiro dígito verificador
    if cpf[9] != str(digito1):
        valido = False

# Calcula o segundo dígito verificador
if valido:
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    # Verifica o segundo dígito verificador
    if cpf[10] != str(digito2):
        valido = False

# Verifica se todas as condições foram atendidas
if valido:
    print(f"'{cpf}' é um CPF válido.")  # CPF é válido
else:
    print(f"'{cpf}' é um CPF inválido.")  # CPF é inválido
