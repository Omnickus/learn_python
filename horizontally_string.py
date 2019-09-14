import time

def horizontally():
	string= ""
	while string == "":
		print("Напиши слово или предложение")
		string=input()
	for i in string:
		time.sleep(0.03)
		print(i)
horizontally()