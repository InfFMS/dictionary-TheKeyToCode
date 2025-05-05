# Напишите программу, которая получает на вход две строки, и формирует из них словарь. 
# Ключами служат слова из первой строки, значениями – целые числа из второй.
# Пример ввода
# яблоки сливы груши персики манго киви апельсины
# 34 56 23 89 55 32 11
# a, b = map(str, input().split())
p = list(map(str, input().split()))
n = list(map(int, input().split()))
l={}
# while a!="end":
#     l[a]=0
#     # print(a, b)
#     a, b = map(str, input().split())
for i in range(0, min(len(p), len(n))):
    l[p[i]]=n[i]

s=""
for i in l:
    s += i + ": " + str(l[i]) + ", "
print(s)