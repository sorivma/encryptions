from utils import split_array
from prettytable import PrettyTable
from main import main_func

INFO = """
//WORK IN PROGRESS
"""
TEST_MESSAGE = "Экзамен представляет собой ответы на теоретические вопросы."


def encrypt(message: str, key: str, space_key : str):
    splt_key = key.split("-")
    # Создаём массив колонок нашей таблицы и заполняем их в соответствии с ключом
    cols = [""] * len(splt_key)


    message_counter = 0
    for letter in message:
        cols[int(splt_key[message_counter % len(splt_key)]) - 1 % len(cols)] += letter
        message_counter += 1