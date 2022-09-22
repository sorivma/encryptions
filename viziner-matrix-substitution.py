from alphabets import k_alphabet
from common_operations import main_func

INFO = """
    //WORK IN PROGRESS//
"""

TEST_MESSAGE = "Никакой транспорт не будет попутным, если не знаешь, куда идти."


def encrypt(message, alphabet, seed):
    counter = 0
    encryption = ""
    for letter in message:
        encryption += alphabet[(alphabet.index(letter) + alphabet.index(seed[counter % len(seed)])) % len(alphabet)]
        counter += 1
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
    print(f"Encryption: {encryption}")
    print(f"Decryption: {decrypt(encryption, k_alphabet, 'Котики')}")


if __name__ == "__main__":
    main_func(encrypt, decrypt, test, INFO)
