from alphabets import k_alphabet
from main import main_func
from utils import shift_alphabet
from prettytable import PrettyTable

INFO = """
Данный шифр заменяет каждый символ открытого текста, соответствующим символом алфавита замены, 
определяемому по символа ключа, символы ключа перебираются циклически. 
"""

TEST_MESSAGE = "Никакой транспорт не будет попутным, если не знаешь, куда идти."


def encrypt(message, alphabet, seed):
    counter = 0
    encryption = ""
    matrix = PrettyTable()
    matrix.title = "Сокращенная матрица Вижинера"
    matrix.field_names = [letter for letter in alphabet]
    for letter in message:
        encryption += alphabet[(alphabet.index(letter) + alphabet.index(seed[counter % len(seed)])) % len(alphabet)]
        counter += 1

    for i in range(len(seed)):
        matrix.add_row(shift_alphabet(alphabet, alphabet.index(seed[i % len(seed)]) % len(alphabet)))

    print(matrix)

    return encryption


def decrypt(message, alphabet, seed):
    counter = 0
    decryption = ""
    for letter in message:
        decryption += alphabet[(alphabet.index(letter) - alphabet.index(seed[counter % len(seed)])) % len(alphabet)]
        counter += 1
    return decryption


def test():
    encryption = encrypt(TEST_MESSAGE, k_alphabet, "Котики")
    print(f"Криптограмма: {encryption}")
    print(f"Расшифровка: {decrypt(encryption, k_alphabet, 'Котики')}")


if __name__ == "__main__":
    main_func(encrypt, decrypt, test, INFO)
