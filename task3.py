# Напишите программу, которая получает на вход строку и подсчитывает, 
# сколько раз в ней встречается каждый символ (независимо от регистра).
# Результат нужно вывести без фигурных скобок
# Пример. 
# ввод:
# Абракадабра
# Вывод
# а-5 б-2 д-1 к-1 р-2
s = input()
s=s.lower()
l={}
for i in s:
    if i in l:
        l[i]+=1
    else:
        l[i]=1
s=""
for i in l:
    s += str(i) + "-" + str(l[i]) + ", "
print(s)