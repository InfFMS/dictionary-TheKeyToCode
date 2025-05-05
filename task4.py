# Имеется следующий словарь:
numbers = {'dict1': [11, 20, 30, 17, 6, 24, 90, 15, 17],
          	'dict2': [21, 33, 40, 10, 29, 31, 90, 12],
          	'dict3': [52, 34, 20, 21, 44, 22, 10, 87],
          	'dict4': [22, 54, 29, 21, 70, 88, 99, 34],
          	'dict5': [21, 40, 29, 21, 19, 32, 68, 77],
          	'dict6': [14, 60, 70, 10, 55, 61, 84, 99],
          	'dict7': [45, 80, 12, 23, 42, 22, 37, 90],
          	'dict8': [13, 14, 15, 26, 48, 92, 36, 11],
          	'dict9': [12, 70, 18, 28, 18, 28, 53, 91],
          	'dict10': [29, 79, 18, 28, 18, 28, 32, 55]}
# Напишите программу, которая удалит из значений словаря все четные числа.

for i in numbers:
	print(i)
	j=0
	while j < len(numbers[i]):
		print(len(numbers[i]), j)
		if numbers[i][j]%2==0:
			numbers[i].pop(j)
			j -= 1
		j += 1
print(numbers)
for i in numbers:
	s = str(i) + ": "
	j=0
	while j < len(numbers[i]):
		# print(len(numbers[i]), j)
		s += str(numbers[i][j]) + ", "
		j+=1
	print(s)