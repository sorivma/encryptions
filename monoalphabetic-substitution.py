from main import *

INFO = """
An example of a one-letter substitution is the Caesar cipher. 
In this case, your seed should be an integer - the step along 
which the original alphabet moves
"""

TEST_MESSAGE = "После приема подписанного сообщения получатель должен проверить, соответствует ли подпись сообщению."


def encrypt_letter(letter, shift, alphabet):
    return alphabet[(alphabet.index(letter) + int(shift)) % len(alphabet)]


def decrypt_letter(letter, shift, alphabet):
    return alphabet[(alphabet.index(letter) - int(shift)) % len(alphabet)]


def encrypt(message, alphabet, shift):
    return "".join(encrypt_letter(letter, shift, alphabet) for letter in message)


def decrypt(message, alphabet, shift):
    return "".join(decrypt_letter(letter, shift, alphabet) for letter in message)


def test():
    encryption = encrypt(TEST_MESSAGE, k_alphabet, 5)
    print(f"Encryption {encryption}")

    decryption = decrypt(encryption, k_alphabet, 5)
    print(f"Decryption {decryption}")


if __name__ == "__main__":
    main_func(encrypt, decrypt, test, INFO)
