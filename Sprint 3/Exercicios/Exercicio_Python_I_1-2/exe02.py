# Declarando a variável 'numeros' como uma lista usando range()
numeros = list(range(2, 5))  # Adiciona os números 2, 3 e 4 à lista

# Verificando se cada número é par ou ímpar e imprimindo o resultado
for numero in numeros:
    if numero % 2 == 0:
        print(f"Par: {numero}")
    else:
        print(f"Ímpar: {numero}")
