balance = 5

print(bool(balance<0))
print(bool(balance>0))


if balance < 0:
	print("Пополните баланс")

print("---------------------------------------")

price = 10

print(bool(balance < 0 or price > balance))

print("---------------------------------------")

if balance < price:
	print("Спасибо за покупку")
else:
	print("Пополните баланс")

print("-------------elif-------------------")

temperature = 12

def weather(temperature):
	if 0 < temperature < 15:
		return("на улице холодно")
	elif 1 < temperature <= 15:
		return("На улице прохладно")
	elif 1 <= temperature <=25:
		return("На улице тепло")
	else:
		return("На улице жарко")
print(weather(-2))
print(weather(12))
print(weather(30))