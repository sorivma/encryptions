START_POSITION = ord('А')
k_alphabet = "".join(chr(letter) for letter in range(START_POSITION, START_POSITION + 64))
SPECIAL_SIGNS = "!.,/?';:[]{}()-–_=+*%^#@| "
k_alphabet += SPECIAL_SIGNS
