from prettytable import PrettyTable
from alphabets import k_alphabet


def shift_alphabet(alphabet, shift):
    shifted_alphabet = []
    for letter in alphabet:
        shifted_alphabet.append(alphabet[(alphabet.index(letter) + shift) % len(alphabet)])
    return shifted_alphabet


def generate_viziner_matrix(alphabet, show_matrix=False):
    matrix = [shift_alphabet(alphabet, alphabet.index(letter)) for letter in alphabet]
    if show_matrix:
        table = PrettyTable()
        table.title = "Матрица Вижинера для данного алфавита"
        table.field_names = [str(i) for i in range(len(alphabet))]
        for alphabet in matrix:
            table.add_row(alphabet)
        print(table)
    return matrix


def chunk_list(lst, number):
    list_chunks = []
    for start in range(number):
        chunk = [lst[i] for i in range(start, len(lst), number)]
        list_chunks.append(chunk)
    return list_chunks


def split_array(a, n):
    k, m = divmod(len(a), n)
    return list(a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


def test_generate_viziner_matrix():
    generate_viziner_matrix(k_alphabet, show_matrix=True)


def test_chunk():
    lst = [1, 2, 3, 4, 5, 6]
    print(chunk_list(lst, 2))


def test():
    matrix = generate_viziner_matrix(k_alphabet, show_matrix=True)
    chunks = chunk_list(matrix, 10)
    for chunk in chunks:
        for element in chunk:
            print(element)
        print()


if __name__ == "__main__":
    test()
