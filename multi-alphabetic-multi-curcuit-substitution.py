from main import *
from prettytable import PrettyTable
from utils import shift_alphabet


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
    first_circuit = PrettyTable()
    second_circuit = PrettyTable()
    first_circuit.add_row(alphabet)
    second_circuit.add_row(alphabet)
    field_names = [str(i) for i in range(len(alphabet))]
    first_circuit.title = "Таблица замены первого контура"
    second_circuit.title = "Таблица замены второго контура"
    first_circuit.field_names = field_names
    second_circuit.field_names = field_names
    check_1_circuit = []
    check_2_circuit = []

    for letter in message:
        if letter_index % 2 == 0:
            encryption += alphabet[(alphabet.index(letter) + counter_first_circuit) % len(alphabet)]
            table.add_row([letter, message.index(letter),
                           alphabet.index(letter),-
                           (alphabet.index(letter) + counter_first_circuit) % len(alphabet),
                           "НЕТ",
                           alphabet[(alphabet.index(letter) + counter_first_circuit) % len(alphabet)],
                           ])
            row = shift_alphabet(alphabet, counter_first_circuit)
            if row[0] not in check_1_circuit:
                first_circuit.add_row(row)
                check_1_circuit.append(row[0])
        else:
            encryption += alphabet[(alphabet.index(letter) + counter_second_circuit) % len(alphabet)]
            table.add_row([letter, message.index(letter),
                           alphabet.index(letter),
                           "НЕТ",
                           (alphabet.index(letter) + counter_second_circuit) % len(alphabet),
                           alphabet[(alphabet.index(letter) + counter_second_circuit) % len(alphabet)]])
            row = shift_alphabet(alphabet, counter_second_circuit)
            if row[0] not in check_2_circuit:
                second_circuit.add_row(row)
                check_2_circuit.append(row[0])
        counter_first_circuit *= 2
        counter_second_circuit += counter_second_circuit
        letter_index += 1

    print(first_circuit)
    print(second_circuit)
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