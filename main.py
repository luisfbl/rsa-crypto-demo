from base64 import b64encode, b64decode
from Crypto.PublicKey import RSA

import rsa
from rsa import generate_keys


def menu():
    round = 0
    priv_key, pub_key = generate_keys()

    while True:
        print('0. Sair')
        print('1. Gerar novas chaves')
        print('2. Encriptar')
        print('3. Descriptar')

        try:
            option = int(input('Digite uma opção: '))
            if option > 3 or option < 0:
                raise Exception
        except Exception:
            print('Opção inválida!')
            continue

        if option == 0:
            break

        elif option == 1:
            if round != 0:
                priv_key, pub_key = generate_keys()

            priv_b64 = b64encode(priv_key).decode('utf-8')
            pub_b64 = b64encode(pub_key).decode('utf-8')
            round += 1

            print(f'Chave privada: {priv_b64}')
            print(f'Chave pública: {pub_b64}')

        elif option == 2:
            message = input("Digite a mensagem a ser encriptada: ").encode()

            inpt = input('Usar chaves personalizadas? (Y/n): ').lower()
            if inpt == 'y':
                pub_b64 = input("Digite a chave pública (em base64): ")
                pub_key = b64decode(pub_b64)

            encrypted = rsa.encode(message, pub_key)

            print(f"Texto encriptado (base64): {b64encode(encrypted).decode('utf-8')}")

        elif option == 3:
            last_encrypted = b64decode(input("Digite a mensagem a ser descriptada: "))
            inpt = input('Usar chaves personalizadas? (Y/n): ').lower()

            if inpt == 'y':
                priv_b64 = input("Digite a chave privada (em base64): ")
                priv_key = b64decode(priv_b64)

            decrypted = rsa.decode(last_encrypted, priv_key)
            print(f"Texto decriptado: {decrypted}")

        print()


if __name__ == '__main__':
    menu()