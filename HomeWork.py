def choce_age(old):
	if 0 < old < 3:
		return 5
	elif 3 <= old < 6:
		return  'в таком возрасте ты должен учиться в детском саду'
	elif 6 <= old < 19:
		return 'Ты должен учиться в школе'
	elif 19 <= old <26:
		return 'Наверное ты еще учишься в университете'
	elif 26 <= old :
		return 'Ты уже должен работать'
	elif 120 <= old:
		return 'Да ты оптимист'
	else:
		return 'ты еще совсем малыш'

def main():
	play_again = ""
	print("Сыграем?")
	print('Напишите "да"или "нет"')
	play_again = input().strip()
	play_again = play_again.lower()

	if play_again == "да":
		print("Как тебя зовут?")
		name = input()
		print("Привет " + name)
		print("Сколько тебе лет?")
		age = input()
		age = int(age)
		game = choce_age(age)
		print(game)
	elif play_again == "нет":
		print("До скорого")
	else:
		main()
main()