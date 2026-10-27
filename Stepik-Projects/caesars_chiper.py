def caesar_cipher(text, shift, language):
    result = ""

    if language == "ru":
        upper_start = ord("А")
        lower_start = ord("а")
        alphabet_size = 32
    else:
        upper_start = ord("A")
        lower_start = ord("a")
        alphabet_size = 26

    for char in text:
        if char.isupper():
            result += chr(
                upper_start + (ord(char) - upper_start + shift) % alphabet_size
            )
        elif char.islower():
            result += chr(
                lower_start + (ord(char) - lower_start + shift) % alphabet_size
            )
        else:
            result += char

    return result


direction = input("Шифрование или дешифрование? (shifr/deshifr): ").lower()
language = input("Язык? (ru/eng): ").lower()
shift = int(input("Шаг сдвига: "))
text = input("Введите текст: ")

if direction == "deshifr":
    shift = -shift

print(caesar_cipher(text, shift, language))



