from common_operations import *

INFO = """Several values can correspond to one letter in this cipher. 
The key for this cipher is a positive integer and every 
second symbol will be cyphered with the second circuit"""

TEST_MESSAGE = "Однонаправленная функция –это основное понятие в криптографии с открытым ключом."


def encrypt(message: str, alphabet: str, seed: int):
    counter_first_circuit = int(seed)
    counter_second_circuit = int(seed)
    encryption = ""
    for letter in message:
        if message.index(letter) % 2 == 0:
            encryption += alphabet[(alphabet.index(letter) + counter_first_circuit) % len(alphabet)]
            counter_first_circuit += 1
        else:
            encryption += alphabet[(alphabet.index(letter) + counter_second_circuit) % len(alphabet)]
            counter_second_circuit *= 2
    return encryption


def decrypt(message: str, alphabet: str, seed: int):
    counter_first_circuit = int(seed)
    counter_second_circuit = int(seed)
    decryption = ""
    for letter in message:
        if message.index(letter) % 2 == 0:
            decryption += alphabet[(alphabet.index(letter) - counter_first_circuit) % len(alphabet)]
            counter_first_circuit += 1
        else:
            decryption += alphabet[(alphabet.index(letter) - counter_second_circuit) % len(alphabet)]
            counter_second_circuit *= 2
    return decryption


def test():
    encryption = encrypt(TEST_MESSAGE, k_alphabet, 1)
    print(f"Encryption: {encryption}")
    print(f"Decryption: {decrypt(encryption, k_alphabet, 1)}")


if __name__ == "__main__":
    main_func(encrypt, decrypt, test, INFO)
