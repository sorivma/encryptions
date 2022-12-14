from main import *

INFO = """
Unlike the Caesar cipher, 
several values can correspond to one letter in this cipher. 
The key for this cipher is a positive integer
"""

TEST_MESSAGE = "Доступность –это свойство информации, при котором субъекты, имеющие законное право доступа к информации, могут это право осуществить."


def encrypt(message, alphabet, seed):
    counter = int(seed)
    encryption = ""
    for letter in message:
        encryption += alphabet[(alphabet.index(letter) + counter) % len(alphabet)]
        counter *= 2
    return encryption


def decrypt(message, alphabet, seed):
    counter = int(seed)
    decryption = ""
    for letter in message:
        decryption += alphabet[(alphabet.index(letter) - counter) % len(alphabet)]
        counter *= 2
    return decryption


def test():
    encryption = encrypt(TEST_MESSAGE, k_alphabet, 5)
    print(f"Encryption: {encryption}")
    decryption = decrypt(encryption, k_alphabet, 5)
    print(f"Decryption: {decryption}")
    print(len(k_alphabet))


if __name__ == "__main__":
    main_func(encrypt, decrypt, test, INFO)
