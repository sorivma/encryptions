from alphabets import *


def read_message():
    message = input("Введите сообщение: ")
    seed = input("Введите ключ: ")
    return message, seed


def main_func(encryption_fun, decryption_fun, test, info):
    alphabet = k_alphabet
    while True:
        command = input("""Введите -help для справки
        """)
        if command == "-help":

            print("""
            -encrypt - Зашифровать сообщение
            -decrypt - Расшифровать сообщение
            -try - Зашифровать и расшифровать сообщение
            -stop - Выход из приложения
            -test - Зашифровать и расшифровать тестовое сообщение
            -al - Просмотреть алфавит
            """)

        elif command in ["-encrypt", "-decrypt", "-try"]:
            message, seed = read_message()
            try:
                if command == "-encrypt":
                    result = encryption_fun(message, alphabet, seed)
                    print("Зашифрованное сообщение: " + result)
                elif command == "-decrypt":
                    result = decryption_fun(message, alphabet, seed)
                    print("Расшифрованное сообщение: " + result)
                elif command == "-try":
                    encrypted_message = encryption_fun(message, alphabet, seed)
                    print("Зашифрованное сообщение: " + encrypted_message)

                    decrypted_message = decryption_fun(encrypted_message, alphabet, seed)
                    print("Расшифрованное сообщение: " + decrypted_message)
            except ValueError:
                print("Некорректный символ в сообщении")

        elif command == "-stop":
            break

        elif command == "-ca":
            c_alphabet = input("Введите новый алфавит без пробелов через разделитель [,]: ").split(',')
            if len(c_alphabet) == len(set([letter for letter in c_alphabet])):
                alphabet = c_alphabet
                print(f"Алфавит изменён на {alphabet}")
            else:
                print("Данный алфавит не допускает однозначной дешифровки, присутствуют повторяющиеся буквы")
        elif command == "-ra":
            alphabet = k_alphabet
            print(f"Алфавит возвращён к исходному состоянию {alphabet}")

        elif command == "-info":
            print(info)

        elif command == "-test":
            test()

        elif command == "-al":
            print(alphabet)

        elif command == "-numbers":
            for letter in alphabet:
                print(letter, alphabet.index(letter))

        elif command == "-al sep":
            print(" ".join(letter for letter in k_alphabet))

        else:
            print("""
        NO SUCH COMMAND
            """)
