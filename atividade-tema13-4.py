# Solicita ao usuário que insira um CPF para validação
cpf = input("Digite o CPF para validação (somente números): ")

# Inicializa a variável de controle
valido = True  # Indica se o CPF é válido

# Verifica se o CPF tem 11 dígitos
if len(cpf) != 11:
    valido = False  # Se o CPF não tiver 11 dígitos, marca como inválido

# Verifica se todos os caracteres são dígitos
i = 0
while i < len(cpf) and valido:
    if not ('0' <= cpf[i] <= '9'):
        valido = False  # Se encontrar um caractere que não é dígito, marca como inválido
    i += 1

# Calcula o primeiro dígito verificador
if valido:
    soma = 0  # Inicializa a soma para o cálculo do primeiro dígito verificador
    peso = 10  # Peso inicial para o cálculo
    for i in range(9):
        soma += int(cpf[i]) * peso  # Multiplica cada dígito pelo peso e soma
        peso -= 1  # Decrementa o peso
    resto = soma % 11  # Calcula o resto da divisão por 11
    if resto < 2:
        digito1 = 0  # Se o resto for menor que 2, o dígito verificador é 0
    else:
        digito1 = 11 - resto  # Caso contrário, o dígito verificador é 11 menos o resto

    # Verifica o primeiro dígito verificador
    if cpf[9] != str(digito1):
        valido = False  # Se o dígito verificador não corresponder, marca como inválido

# Calcula o segundo dígito verificador
if valido:
    soma = 0  # Inicializa a soma para o cálculo do segundo dígito verificador
    peso = 11  # Peso inicial para o cálculo
    for i in range(10):
        soma += int(cpf[i]) * peso  # Multiplica cada dígito pelo peso e soma
        peso -= 1  # Decrementa o peso
    resto = soma % 11  # Calcula o resto da divisão por 11
    if resto < 2:
        digito2 = 0  # Se o resto for menor que 2, o dígito verificador é 0
    else:
        digito2 = 11 - resto  # Caso contrário, o dígito verificador é 11 menos o resto

    # Verifica o segundo dígito verificador
    if cpf[10] != str(digito2):
        valido = False  # Se o dígito verificador não corresponder, marca como inválido

# Verifica se todas as condições foram atendidas
if valido:
    print(f"'{cpf}' é um CPF válido.")  # CPF é válido
else:
    print(f"'{cpf}' é um CPF inválido.")  # CPF é inválido
