day=int(input("Enter library attence "))
if day <= 5:
	print("library charge =",day*2)
if day >=6 and day < 10:
	print("library charge =",day*3)
if day >= 10 and day <15:
	print("library charge =",day*4)
if day >=16:
	print("library charge =",day*5)