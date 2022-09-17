from alphabets import *


def read_message():
    message = input("Input your message: ")
    seed = input("Input your seed: ")
    return message, seed


def main_func(encryption_fun, decryption_fun, test, info):
    alphabet = k_alphabet
    while True:
        command = input("""type -help for help
        """)
        if command == "-help":

            print("""
            -encrypt stands for encrypting a message
            -decrypt stands for decrypting a message
            -try stands for encrypting and decrypting a message
            -stop stands for stopping an application
            -ca stands for changing an alphabet
            -ra stands for changing an alphabet back to default
            -info stands for brief cipher info
            -test initializes test case
            -al stands for showing current alphabet
            """)

        elif command in ["-encrypt", "-decrypt", "-try"]:
            message, seed = read_message()
            try:
                if command == "-encrypt":
                    result = encryption_fun(message, alphabet, seed)
                    print("Encrypted message: " + result)
                elif command == "-decrypt":
                    result = decryption_fun(message, alphabet, seed)
                    print("Decrypted message: " + result)
                elif command == "-try":
                    encrypted_message = encryption_fun(message, alphabet, seed)
                    print("Encrypted message: " + encrypted_message)

                    decrypted_message = decryption_fun(encrypted_message, alphabet, seed)
                    print("Decrypted message: " + decrypted_message)
            except ValueError:
                print("Incorrect symbol in line")

        elif command == "-stop":
            break

        elif command == "-ca":
            alphabet = input("Insert your alphabet with [,] separator: ").split(',')

        elif command == "-ra":
            alphabet = k_alphabet

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
