from main import *
from prettytable import PrettyTable

INFO = """Several values can correspond to one letter in this cipher. 
The key for this cipher is a positive integer and every 
second symbol will be cyphered with the second circuit"""

TEST_MESSAGE = "Однонаправленная функция –это основное понятие в криптографии с открытым ключом."

FIELDS_NAMES = ["Буква сообщения", "№", "№ (В алфавите)", "(x+k*2^i) mod n",
                "(x + k*(i+1)) mod n", "Соответстсвующая буква шифра"]


def encrypt(message: str, alphabet: str, seed: int):
    table = PrettyTable()
    table.field_names = FIELDS_NAMES

    letter_index = 0
    counter_first_circuit = int(seed)
    counter_second_circuit = int(seed)
    encryption = ""

    for letter in message:
        if letter_index % 2 == 0:
            encryption += alphabet[(alphabet.index(letter) + counter_first_circuit) % len(alphabet)]
            table.add_row([letter, message.index(letter),
                           alphabet.index(letter),
                           (alphabet.index(letter) + counter_first_circuit) % len(alphabet),
                           "НЕТ",
                           alphabet[(alphabet.index(letter) + counter_first_circuit) % len(alphabet)],
                           ])
        else:
            encryption += alphabet[(alphabet.index(letter) + counter_second_circuit) % len(alphabet)]
            table.add_row([letter, message.index(letter),
                           alphabet.index(letter),
                           "НЕТ",
                           (alphabet.index(letter) + counter_second_circuit) % len(alphabet),
                           alphabet[(alphabet.index(letter) + counter_second_circuit) % len(alphabet)]])

        counter_first_circuit *= 2
        counter_second_circuit += counter_second_circuit
        letter_index += 1

    print(table)
    return encryption


def decrypt(message: str, alphabet: str, seed: int):
    letter_index = 0
    counter_first_circuit = int(seed)
    counter_second_circuit = int(seed)
    decryption = ""
    for letter in message:
        if letter_index % 2 == 0:
            decryption += alphabet[(alphabet.index(letter) - counter_first_circuit) % len(alphabet)]

        else:
            decryption += alphabet[(alphabet.index(letter) - counter_second_circuit) % len(alphabet)]

        counter_first_circuit *= 2
        counter_second_circuit += counter_second_circuit
        letter_index += 1

    return decryption


def test():
    encryption = encrypt(TEST_MESSAGE, k_alphabet, 5)
    print(f"Encryption: {encryption}")
    print(f"Decryption: {decrypt(encryption, k_alphabet, 5)}")


if __name__ == "__main__":
    main_func(encrypt, decrypt, test, INFO)
