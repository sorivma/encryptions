from utils import split_array
from prettytable import PrettyTable

INFO = """
Ключом является последовательность целых положительных чисел, записанных без разделителей
Пример: 312
"""

TEST_MESSAGE = "Экзамен представляет собой ответы на теоретические вопросы."


def normalize_message(message, key):
    while len(message) % len(key) != 0:
        message += "#"
    return message


def encrypt(message: str, alphabet, key: str):
    key = key.split("-")
    col_number = len(key)

    if len(message) % col_number == 0:
        row_number = len(message) // col_number
    else:
        row_number = len(message) // col_number + 1

    table = [""] * col_number

    for i in range(len(message)):
        table[i % col_number] += message[i]

    output = ""
    for i in range(1, len(key) + 1):
        table_index = key.index(str(i))
        output += table[table_index]

    table = PrettyTable()
    table.title = "Таблица перестановки"
    table.field_names = list(key)
    rows = split_array(normalize_message(message, key), row_number)
    for row in rows:
        table.add_row(row)
    print(table)

    return output


def decrypt(message: str, alphabet, key: str):
    splt_key = key.split("-")
    colum_num = len(splt_key)
    colum_length = [0] * colum_num

    for i in range(len(message)):
        colum_length[i % colum_num] += 1

    table = []
    for ln in colum_length:
        table.append([""] * ln)
    counter = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = message[counter]
            counter += 1
    output = ""
    for k in range(0, len(message)):
        index = int(splt_key[k % colum_num])
        print(index)
        output += table[index - 1][k // colum_num]
    return output


def test():
    seed = "897564231"
    encryption = encrypt(TEST_MESSAGE, None, seed)
    print(f"Encryption : {encryption}")
    decryption = decrypt(encryption, None, seed)
    print(f"Decryption : {decryption}")


if __name__ == "__main__":
    print(
        "Ключом является последовательность чисел, образованная перестановкой натурального ряда чисел (через разделитель -)"
        "Прример: 1-2-3-4-")
    key = input("Введите ключ: ")
    message = input("Введите сообщение: ")
    command = input("""Введите одну из команд
    сооб - изменить сообщение
    ключ - изменить ключ
    заш - зашифровать сообщение
    рас - расшифровать сообщение
    вых - заврешить работу
    Команда: """)
    message_storage = ""
    while (command != 'вых'):
        if command == 'сооб':
            message = input("Введите сообщение: ")
        elif command == "ключ":
            key = input(f"Введите ключ ( Используемный ключ: {key}): ")
        elif command == "заш":
            message_storage = encrypt(message, "", key)
            print(message_storage)
        elif command == "рас":
            print(decrypt(message_storage, "", key))
        else:
            print("Такой команды нет")
        command = input("Команда: ")
