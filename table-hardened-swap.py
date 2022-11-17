from utils import split_array
from prettytable import PrettyTable
from main import main_func

INFO = """
//WORK IN PROGRESS
"""
TEST_MESSAGE = "Экзамен представляет собой ответы на теоретические вопросы."


# 10,12-11,13-14,15
def encrypt(message: str, key_1: str, key_2: str):
    col_num = len(key_1.split("-"))
    splt_key = key_1.split("-")
    pos_key_arr = key_2.split("-")
    msg_list = list(message)
    for k in range(0, len(splt_key)):
        j = int(pos_key_arr[k].split(",")[1])
        i = int(pos_key_arr[k].split(",")[0])
        index = j + col_num * i
        print(index)
        msg_list.insert(index, '*')

    if len(message) % col_num == 0:
        row = len(message) // col_num
    else:
        row = len(message) // col_num + 1

    table = [""] * col_num
    for i in range(len(msg_list)):
        table[i % col_num] += message[i]

    output = ""
    key_index = 0
    for i in range(1, len(splt_key) + 1):
        key_index = splt_key.index(str(i))
        output += table[key_index]
