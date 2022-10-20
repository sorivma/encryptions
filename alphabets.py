START_POSITION = ord('А')
k_alphabet = "".join(chr(letter) for letter in range(START_POSITION, START_POSITION + 64))
SPECIAL_SIGNS = "!.,/?';:[]{}()-–_=+*%^#@|Ёё "
k_alphabet += SPECIAL_SIGNS

l_alphabet = "".join(chr(letter) for letter in range(65, 65 + 26))
l_alphabet += "".join(chr(letter) for letter in range(97, 97 + 26))
