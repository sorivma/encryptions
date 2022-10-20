from utils import split_array
from prettytable import PrettyTable
from main import main_func

INFO = """
//WORK IN PROGRESS
"""
TEST_MESSAGE = "Экзамен представляет собой ответы на теоретические вопросы."


def normalize_message(message, seed):
    normalized_message = message
    while len(normalized_message) % len(seed.split("-")) != 0:
        normalized_message += " "
    return normalized_message


def encrypt(message, alphabet, seed):
    message = normalize_message(message, seed)
    splt_seed = seed.split("-")
    matrix_row_num = len(message) // len(splt_seed)
    lines = split_array(message, matrix_row_num)

    table = PrettyTable()
    table.title = "Таблица простой перестановки"
    table.field_names = splt_seed

    for line in lines:
        table.add_row(line)
    print(table)

    encryption = ""
    for index in splt_seed:
        for i in range(matrix_row_num):
            encryption += lines[i][int(index) - 1]

    return encryption


def decrypt(message, alphabet, seed):
    message = normalize_message(message, seed)
    splt_seed = seed.split("-")

    matrix_row_num = len(message) // len(splt_seed)
    lines = split_array(message, len(splt_seed))

    table = PrettyTable()
    table.title = "Таблица простой перестановки (Зашифрованного сообщения с восстановленным порядком строк)"
    table.field_names = [i for i in range(matrix_row_num)]

    reconstructed_table = [""] * len(splt_seed)
    counter = 0
    for label in splt_seed:
        reconstructed_table[int(label) - 1] = lines[counter]
        counter += 1

    for line in reconstructed_table:
        table.add_row(line)

    encryption = ""
    for i in range(matrix_row_num):
        for j in range(len(splt_seed)):
            encryption += reconstructed_table[j][i]

    print(table)

    return encryption.strip()


def test():
    seed = "8-9-7-5-6-4-2-3-1"
    encryption = encrypt(TEST_MESSAGE, None, seed)
    print(f"Encryption : {encryption}")
    decryption = decrypt(encryption, None, seed)
    print(f"Decryption : {decryption}")


if __name__ == "__main__":
    main_func(encrypt, decrypt, test, INFO)
