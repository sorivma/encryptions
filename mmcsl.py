from alphabets import k_alphabet
from prettytable import *
from utils import shift_alphabet


def operate(message, alphabet, circuits, encrypt):
    if encrypt:
        multiplier = 1
    else:
        multiplier = -1

    counter = 0
    letter_counter = 0
    output = ""
    for letter in message:
        output += alphabet[(alphabet.index(letter) +
                            multiplier * int(circuits[counter][letter_counter])) % len(alphabet)]
        counter += 1
        letter_counter += 1
        counter %= 3
        letter_counter %= len(circuits[0])
    return output


def parse_key():
    circuits = []
    for i in range(3):
        circuits.append(input(f"""
        Контур №{i}
        Введите не менее двух целых положительных чисел через разделитель [,] 
        для каждого из контуров длина последовательности должна быть одинаковой:  
        """).split(","))
    return circuits


def main():
    command = ""
    print("""Для выхода введите 'стоп'
Для шифрования введите 'зашифровать'
Для расшифрования введите 'расшифровать'
    """)
    while command != 'стоп':
        command = input("Введите команду: ")
        if command == "зашифровать":
            message = input("Введите сообщение: ")
            circuits = parse_key()
            for i in range(len(circuits)):
                table = PrettyTable()
                table.title = f"Контур №{i}"
                table.add_row(k_alphabet)
                for shift in circuits[i]:
                    table.add_row(shift_alphabet(k_alphabet, int(shift)))
                print(table)
            print(f"""Криптограмма:
            {operate(message, k_alphabet, circuits, True)}
            """)
        elif command == "расшифровать":
            message = input("Введите сообщение: ")
            circuits = parse_key()
            print(f"""Расшифровка:
            {operate(message, k_alphabet, circuits, False)}
            """)


if __name__ == "__main__":
    main()
