from tabulate import tabulate

INFO = """
Ключом является последовательность целых положительных чисел, записанных без разделителей
Пример: 312
"""

TEST_MESSAGE = "Экзамен представляет собой ответы на теоретические вопросы."


def encrypt(message: str, key: str):
    splt_key = key.split("-")

    # Создаём массив колонок нашей таблицы и заполняем их в соответствии с ключом
    cols = [""] * len(splt_key)
    message_counter = 0
    for letter in message:
        cols[int(splt_key[message_counter % len(splt_key)]) - 1 % len(cols)] += letter
        message_counter += 1

    # Вычилсяем количество строк таблицы
    if len(message) % len(splt_key) == 0:
        row_len = len(message) // len(splt_key)
    else:
        row_len = len(message) // len(splt_key) + 1

    # Переварачиваем стобцы в строки
    rows = [""] * row_len
    for number in splt_key:
        row_counter = 0
        for letter in cols[int(number) - 1]:
            rows[row_counter] += letter
            row_counter += 1

    print(tabulate(rows, splt_key, tablefmt="outline"))

    return "".join(cols)


def decrypt(message: str, key: str):
    splt_key = key.split("-")
    inner_message = message

    cols_l = [0] * len(splt_key)
    for i in range(len(message)):
        cols_l[i % len(cols_l)] += 1

    cols = [""] * len(splt_key)
    for i in range(len(splt_key)):
        j = 0
        for j in range(cols_l[splt_key.index(str(i + 1))]):
            cols[splt_key.index(str(i + 1))] += inner_message[j]
        inner_message = inner_message[j + 1:]

    output = ""
    for j in range(len(cols[0])):
        for i in range(len(cols)):
            try:
                output += cols[i][j]
            except IndexError:
                pass
    return output


if __name__ == "__main__":
    print()