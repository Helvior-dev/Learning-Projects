from random import choice

DIGITS = "0123456789"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
PUNCTUATION = "!#$%&*+-=?@^_"
AMBIGUOUS = "il1Lo0O"

chars = ""

cntPw = int(input("Количество паролей: "))
lenPw = int(input("Длина одного пароля: "))

if input("Включать цифры? (y/n): ").strip().lower() == "y":
    chars += DIGITS
if input("Включать прописные буквы? (y/n): ").strip().lower() == "y":
    chars += UPPERCASE
if input("Включать строчные буквы? (y/n): ").strip().lower() == "y":
    chars += LOWERCASE
if input("Включать символы !#$%&*+-=?@^_? (y/n): ").strip().lower() == "y":
    chars += PUNCTUATION
if input("Исключать неоднозначные символы il1Lo0O? (y/n): ").strip().lower() == "y":
    for c in AMBIGUOUS:
        chars = chars.replace(c, "")

if not chars:
    print("Ошибка: не выбран ни один вид символов!")
    exit()


def generate_password(length, chars, count):
    for _ in range(count):
        password = "".join(choice(chars) for _ in range(length))
        print(password)


generate_password(lenPw, chars, cntPw)
