def drawSquare(side):
	print("")
	print(("*" * side + "\n") * side)
	print("")


def drawRectangle(length,width):
	print("")
	print(("*" * width + "\n") * length)
	print("")	

def drawRightTriangle(height):
	print("")
	for i in range(height):
		print("*" * (i + 1))
	print("")

def drawDiamond(height):
	print("")
	space = height // 2 - (0 if height % 2 == 1 else 1)
	star = 1
	expand = True
	mark = True
	for i in range(height):
		print(" " * space + "*" * star)
		if space == 0:
			expand = False
			if mark and height % 2 == 0:
				mark = False
				continue
		if expand:
			space -= 1
			star += 2
		else:
			space += 1
			star -= 2
	print("")

print("----------------------------Shape Printer----------------------------")
while True:
	resp = 0
	while True:
		print("Which shape do you want to draw?")
		print("[1] - Square")
		print("[2] - Rectangle")
		print("[3] - Right Triangle")
		print("[4] - Diamond")
		print("[5] - Exit")
		try:
			resp = int(input("Response: "))
			if resp >= 1 and resp <= 5:
				break
			else:
				print("Response must be from 1 to 5")
		except ValueError:
			print("Input must be a number")

	if resp == 1:
		side = int(input("Enter side length: "))
		drawSquare(side)
	elif resp == 2:
		length = int(input("Enter length: "))
		width = int(input("Enter width: "))
		drawRectangle(length,width)
	elif resp == 3:
		height = int(input("Enter height: "))
		drawRightTriangle(height)
	elif resp == 4:
		height = int(input("Enter height: "))
		drawDiamond(height)
	elif resp == 5:
		print("Thank you for using the program.")
		break
