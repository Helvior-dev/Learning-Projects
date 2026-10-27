def sdvig(symb, num):
    abc = "abcdefghijklmnopqrstuvwxyz"
    symb_index = abc.find(symb.lower())
    if symb_index + num > 25:
        if symb.lower() == symb:
            return abc[symb_index + num - 26]
        else:
            return abc[symb_index + num - 26].upper()
    else:
        if symb.lower() == symb:
            return abc[symb_index + num]
        else:
            return abc[symb_index + num].upper()


text = "Hello, my friend! How are you? =)"
result = ""
test = ""
for i in text:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or i == " ":
        test += i
test = test.split()

step = 0
cnt = 0
for i in text:
    if i.isalpha():
        result += sdvig(i, len(test[step]))
        cnt += 1
    else:
        result += i
    if len(result) == len(text):
        break
    try:
        if cnt == len(test[step]):
            cnt = 0
            step += 1
    except:
        continue


print(result)
