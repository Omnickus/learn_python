import random


def cut_cake(peaple):

	try:
		parts = 1/peaple
		print(f'Каждый человек получит по {parts} пирога')
	except ZeroDivisionError:
		print("Не надо делить на ноль")
	except TypeError:
		print("Программа принимает число")
cut_cake(0)


while True:
	p = random.randint(1, 10)
	cut_cake(p)