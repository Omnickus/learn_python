

def string_def(a,b):
	if a != str(a) or b != str(b):
		print("Какой-то из аргументов не является строкой")
		return 0
	elif len(a) == len(b):
		print("Строки одинаковые")
		return 1
	elif a != b and len(a) > len(b):
		print("Первая больше второй")
		return 2 
	elif a != b and b=="learn":
		return 3

print(string_def("vedro", "vedro"))