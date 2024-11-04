import hashlib
import re

while True:
    # Solicita uma opção do usuário
    option = input("\n Escolha uma opção: \n 1. Mascarar String \n 2. Finalizar \n Opção: ")

    if option == '2':
        print("Programa finalizado. Obrigada.")
        break
    elif option == '1':
        while True:
            # Solicita a string do usuário para mascarar
            data = input("\n Digite a string para mascarar: ")
            
            # Verifica se a entrada contém apenas letras, espaços e acentos
            if re.match(r'^[A-Za-zÀ-ÿ\s]+$', data):

                # Gera o hash SHA-1
                hash_object = hashlib.sha1(data.encode())
                hex_dig = hash_object.hexdigest()

                # Exibe o hash
                print("\nHash SHA-1:", hex_dig)
                break
            else:
                print("Erro: A string deve conter apenas letras. Tente novamente.")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")
