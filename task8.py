# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор
shifr = {
    "a": "1",
    "b": "2",
    "c": "3",
    "d": "4",
    "e": "5",
    "f": "6",
    "g": "7",
    "h": "8",
    "i": "9",
    "j": "0",
    "k": ":",
    "l": "%",
    "m": ";",
    "n": "№",
    "o": "?",
    "p": "*",
    "q": ")",
    "r": "(",
    "s": "-",
    "t": "_",
    "u": "+",
    "v": "=",
    "w": "!",
    "x": "@",
    "y": "/",
    "z": "}",
    " ": "{",
    ",": "[",
    "-": "]",
    "!": ">",
    ".": "<",
    "0": "d",
    "1": "t",
    "2": "w",
    "3": "i",
    "4": "y",
    "5": "f",
    "6": "c",
    "7": "x",
    "8": "z",
    "9": "u",
    ")": "o",
    "(": "p",
    "?": "r",
    "\"": "q",
    "'": "v",
    "=": "b",
    "+": "j",
    "/": "h",
    "*": "g",
}
deshifr={}
for i in shifr:
    deshifr[shifr[i]]=i
d = input("Если нужен шифр: s, если дешифр: d, конец: e: ")
while d!="e":
    if d=="s":
        s=input("Введите предложение для шифрования: ")
        s=s.lower()
        # print(s)
        s_s = ""
        for i in range(len(s)):
            s_s+=shifr[s[i]]
        print(s_s)
    elif d=="d":
        s = input("Введите предложение для дешифрования: ")
        s=s.lower()
        # print(s)
        s_s = ""
        for i in range(len(s)):
            s_s += deshifr[s[i]]
        print(s_s)
    else:
        print("ERROR!")
    d = input("Если нужен шифр: s, если дешифр: d, конец: e: ")